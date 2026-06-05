import os
from openpyxl import Workbook
from playwright.sync_api import sync_playwright


def salvar_em_excel(dados_produtos):
    """Salva os produtos reais coletados no Excel."""
    print("\n[Excel] Criando planilha com dados reais da Amazon...")
    wb = Workbook()
    aba_ativa = wb.active
    aba_ativa.title = "Ofertas Amazon"

    aba_ativa.append(["Produto", "Preço Real (R$)"])

    for item in dados_produtos:
        aba_ativa.append([item["produto"], item["preco_reais"]])

    nome_arquivo = "notebooks_amazon.xlsx"
    wb.save(nome_arquivo)
    print(f"✅ [Excel] Planilha salva com sucesso como: {nome_arquivo}")


def rodar_robo_amazon():
    print("=== INICIANDO ROBÔ MONITOR DE PREÇOS REAIS (AMAZON) ===")

    with sync_playwright() as p:
        print("Abrindo navegador Chrome...")
        navegador = p.chromium.launch(headless=False, channel="chrome")

        contexto = navegador.new_context(
            viewport={"width": 1366, "height": 768},
            locale="pt-BR",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        )
        pagina = contexto.new_page()

        url_alvo = "https://www.amazon.com.br/s?k=notebook"
        print(f"Acessando: {url_alvo}")
        pagina.goto(url_alvo)

        print("\n" + "=" * 60)
        print("PAUSA DE SEGURANÇA (MODO HÍBRIDO):")
        print("Aguarde a página carregar os notebooks completamente.")
        print("Quando os produtos e PREÇOS aparecerem na tela, volte aqui.")
        print("=" * 60)

        input(
            "\n--> Quando a página mostrar os notebooks, aperte ENTER aqui para extrair: "
        )

        print("\nIniciando varredura e extração de dados reais...")

        # Captura os blocos de produtos
        blocos_produtos = pagina.locator(
            "div[data-component-type='s-search-result']"
        ).all()

        lista_produtos = []
        print(
            f"Analisando {len(blocos_produtos)} blocos de produtos encontrados..."
        )

        for bloco in blocos_produtos:
            try:
                # Captura o título
                tag_titulo = bloco.locator("h2")
                titulo = tag_titulo.inner_text().strip()

                # Filtro de palavras-chave
                if len(titulo) > 25 and any(
                    k in titulo.lower()
                    for k in [
                        "notebook",
                        "laptop",
                        "intel",
                        "amd",
                        "asus",
                        "lenovo",
                        "dell",
                    ]
                ):

                    try:
                        # 💵 LIMPEZA AVANÇADA DO PREÇO REAIS
                        texto_reais = (
                            bloco.locator(".a-price-whole").first.inner_text()
                        )

                        # Remove tudo que não for número: pontos, vírgulas, espaços e quebras de linha
                        texto_reais = (
                            texto_reais.replace(".", "")
                            .replace(",", "")
                            .replace("\n", "")
                            .strip()
                        )

                        # Captura os centavos
                        try:
                            texto_centavos = (
                                bloco.locator(".a-price-fraction")
                                .first.inner_text()
                                .strip()
                            )
                        except Exception:
                            texto_centavos = "00"

                        # Une e converte com segurança
                        preco_final = float(f"{texto_reais}.{texto_centavos}")

                    except Exception as e_preco:
                        # Se falhar na conversão, ignoramos este item e continuamos
                        continue

                    # Evita duplicados na lista
                    if not any(p["produto"] == titulo for p in lista_produtos):
                        lista_produtos.append(
                            {"produto": titulo, "preco_reais": preco_final}
                        )
                        print(
                            f"-> Capturado: {titulo[:45]}... | R$ {preco_final}"
                        )

                # Limitamos a captura aos 5 primeiros válidos
                if len(lista_produtos) >= 5:
                    break
            except Exception:
                continue

        # Salvando os dados reais na planilha
        if lista_produtos:
            salvar_em_excel(lista_produtos)
        else:
            print(
                "❌ O robô não conseguiu extrair os preços. Verifique se os valores estavam visíveis na tela."
            )

        print("\n🏁 Processo concluído com sucesso!")
        navegador.close()
        os._exit(0)


if __name__ == "__main__":
    rodar_robo_amazon()