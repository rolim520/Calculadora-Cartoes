# Calculadora de Recarga de Cartões de Transporte  баланс

![Project Banner](./image.png)

## 🎯 Sobre o Projeto

A **Calculadora de Recarga** é uma aplicação web inteligente projetada para otimizar o uso de dois cartões de transporte (como Riocard e Jaé). Com base no saldo atual de cada cartão, no valor da recarga e nas tarifas, a ferramenta calcula a distribuição exata da recarga para maximizar o número total de passagens, garantindo o melhor aproveitamento do seu dinheiro.

Chega de fazer contas de cabeça ou desperdiçar saldo!

---

## ✨ Funcionalidades

-   **Cálculo Otimizado:** Utiliza um algoritmo preciso para encontrar a melhor divisão da recarga, sem arredondamentos ou estimativas.
-   **Interface Moderna e Responsiva:** Design limpo e amigável que funciona perfeitamente em desktops e dispositivos móveis.
-   **Tarifas Flexíveis:** Permite inserir os valores exatos das tarifas para cada cartão.
-   **Nomes Personalizáveis:** As legendas dos cartões foram atualizadas para "Jaé" e "Riocard" para fácil identificação.
-   **Persistência de Dados:** O formulário memoriza os últimos valores inseridos para agilizar o uso recorrente.

---

## 🚀 Como Executar

Este projeto é totalmente containerizado com Docker, tornando a execução simples e rápida em qualquer ambiente.

### Pré-requisitos

-   [Docker](https://www.docker.com/get-started)
-   [Docker Compose](https://docs.docker.com/compose/install/)

### Passos

1.  **Clone este repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd calculadora-cartoes
    ```

3.  **Inicie a aplicação com Docker Compose:**
    ```bash
    docker compose up -d
    ```

4.  **Acesse a aplicação:**
    Abra seu navegador e acesse [http://localhost:5000](http://localhost:5000).

Pronto! A calculadora já está funcionando.

---

## 🛠️ Tecnologias Utilizadas

-   **Backend:**
    -   [Python](https://www.python.org/)
    -   [Flask](https://flask.palletsprojects.com/)
-   **Frontend:**
    -   HTML5
    -   CSS3
    -   [Bootstrap 5](https://getbootstrap.com/)
-   **Containerização:**
    -   [Docker](https://www.docker.com/)

