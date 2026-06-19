# 🛒 Robô Monitor de Preços - Web Scraping com Python & Playwright

Este projeto consiste em um robô automatizado de extração de dados (**Web Scraping**) desenvolvido em Python. O objetivo principal é monitorar o mercado de tecnologia, realizando buscas dinâmicas no e-commerce da **Amazon Brasil**, extraindo títulos e preços reais de produtos (Notebooks) e estruturando essas informações em uma planilha Excel automatizada.

---

## 🚀 Funcionalidades

* **Automação de Navegação Comercial:** Inicialização e controle do navegador utilizando o Google Chrome real instalado no sistema (`channel="chrome"`).
* **Modo Híbrido Avançado:** Sistema de pausa estratégica (`input()`) para permitir interações humanas ou resoluções de Captcha se necessário, unindo a velocidade do script com a tomada de decisão humana.
* **Filtro Dinâmico de Dados:** Varredura inteligente baseada em tags HTML puras (`h2`), aplicando filtros de palavras-chave para ignorar anúncios patrocinados ou produtos fora do escopo.
* **Tratamento de Strings Monetárias:** Sanetização de dados textuais extraídos da web (remoção de caracteres invisíveis, pontos e vírgulas) para conversão segura em números decimais (`float`).
* **Persistência em Excel:** Geração automática de relatórios formatados em planilhas (`.xlsx`) utilizando a biblioteca `openpyxl`.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12+** (Linguagem base)
* **Playwright** (Framework moderno de automação web e renderização de JavaScript)
* **OpenPyXL** (Manipulação e criação de planilhas Excel)
* **Plataforma Alvo:** Amazon Brasil

---

## 🧠 Arquitetura do Robô: Contornando Bloqueios Reais

Durante o desenvolvimento, o projeto enfrentou sistemas anti-bot extremamente agressivos (como os loops de Captcha e redirecionamentos para login do Mercado Livre). A arquitetura foi refatorada seguindo boas práticas de engenharia de dados:
1. **Migração Estratégica:** Substituição da plataforma alvo para a Amazon, garantindo acesso público aos dados sem a necessidade de autenticação forçada.
2. **Disfarce Nativo:** Em vez de navegadores emulados em modo *headless*, o script utiliza o binário do Chrome legítimo da máquina, reduzindo drasticamente a pegada (*footprint*) do robô.
3. **Seletores Robustos:** Abandono de classes CSS dinâmicas (que mudam a cada hora) em prol de estruturas semânticas rígidas baseadas em blocos de resultados (`data-component-type`) e tags textuais (`h2`).

---
## Prints
<img width="959" height="635" alt="Código Monitor de preços Amazon rodando" src="https://github.com/user-attachments/assets/1e0ffcb0-2360-494c-a1f2-4604a0b4fe66" />
<img width="1366" height="380" alt="Arquivo Excel" src="https://github.com/user-attachments/assets/ec9fad96-1b5e-4f21-91c0-572caac27457" />

---
## 📦 Como Instalar e Rodar o Projeto

### 1. Clonar o Repositório
```bash
git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
cd NOME_DO_REPOSITORIO
