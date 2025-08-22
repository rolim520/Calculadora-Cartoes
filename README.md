# Calculadora de Recarga de Cartões de Transporte

![Project Banner](./image.png)

## 🎯 Sobre o Projeto

A **Calculadora de Recarga** é uma aplicação web inteligente projetada para otimizar o uso de dois cartões de transporte. Com base nos saldos, no valor da recarga e nas tarifas, a ferramenta calcula a distribuição ideal para atingir um **equilíbrio de passagens personalizável**, permitindo que você decida se prefere um número igual de passagens ou favorecer um dos cartões com uma quantidade específica a mais.

---

## ✨ Funcionalidades

-   **Cálculo Otimizado:** Encontra a melhor distribuição de recarga para atingir seu objetivo.
-   **Diferença Alvo Personalizável:** Defina a diferença exata de passagens que você deseja entre os cartões (ex: 0 para equilíbrio, +2 para favorecer o primeiro, ou -3 para o segundo).
-   **Interface Moderna e Responsiva:** Design limpo que funciona perfeitamente em desktops e celulares.
-   **Tarifas Flexíveis:** Permite inserir os valores exatos das tarifas para cada cartão.
-   **Persistência de Dados:** O formulário memoriza os últimos valores inseridos para agilizar o uso.

---

## 💡 Lógica de Otimização

Para garantir um resultado preciso e com alta performance, a calculadora implementa um algoritmo otimizado:

1.  **Iteração por Passagens (Eficiente):** Para encontrar a solução ideal, o algoritmo itera de forma inteligente sobre o número de passagens possíveis para o primeiro cartão. Essa abordagem garante alta performance.

2.  **Cálculo do "Custo":** Para cada quantidade de passagens do primeiro cartão (`n1`), o algoritmo calcula:
    -   A recarga mínima necessária para atingir `n1`.
    -   A recarga restante para o segundo cartão.
    -   O número de passagens resultante para o segundo cartão (`n2`).

3.  **Busca pelo Menor Custo:** O objetivo é encontrar a combinação que minimiza o **"custo"**, definido como a distância entre a diferença de passagens real (`n1 - n2`) e a **diferença desejada** pelo usuário.

4.  **Seleção da Melhor Opção:** A solução com o menor custo é selecionada como a ideal, garantindo o resultado que mais se aproxima do seu objetivo.

5.  **Exatidão com `Decimal`:** Todas as operações financeiras utilizam o tipo `Decimal` do Python, eliminando os erros de arredondamento de tipos de ponto flutuante e garantindo que o resultado seja matematicamente exato.

---

## 🚀 Como Executar

Este projeto é totalmente containerizado, oferecendo duas maneiras de executá-lo.

### Opção 1: Usando a Imagem Pronta do Docker Hub

Esta é a forma mais rápida e simples. Você não precisa clonar o repositório, apenas ter o Docker e o Docker Compose instalados.

1.  **Crie um arquivo `docker-compose.yml`** com o seguinte conteúdo:

    ```yaml
    services:
      calculadora-web:
        image: rolim520/calculadora-cartoes:latest
        ports:
          - "5000:5000"
        restart: unless-stopped
    ```

2.  **Inicie a aplicação** no mesmo diretório onde você criou o arquivo:

    ```bash
    docker compose up -d
    ```

3.  **Acesse a aplicação:**
    Abra seu navegador e acesse [http://localhost:5000](https://www.google.com/search?q=http://localhost:5000).

### Opção 2: Para Desenvolvimento

Use esta opção se você deseja modificar o código-fonte.

1.  **Clone este repositório:**

    ```bash
    git clone https://github.com/rolim520/Calculadora-Cartoes.git
    ```

2.  **Navegue até o diretório do projeto:**

    ```bash
    cd Calculadora-Cartoes
    ```

3.  **Inicie a aplicação com Docker Compose:**
    Este comando irá construir a imagem localmente a partir do `Dockerfile`.

    ```bash
    docker compose up -d --build
    ```

4.  **Acesse a aplicação:**
    Abra seu navegador e acesse [http://localhost:5000](https://www.google.com/search?q=http://localhost:5000).

-----

## ⚙️ CI/CD com GitHub Actions

Este projeto utiliza um fluxo de trabalho de Integração Contínua e Entrega Contínua (CI/CD) com o GitHub Actions.

  - **Automação:** A cada `push` na branch `main`, uma Action é acionada automaticamente.
  - **Build e Push:** O workflow constrói a imagem Docker da aplicação e a envia para o [Docker Hub](https://www.google.com/search?q=https://hub.docker.com/r/seu-usuario-docker-hub/calculadora-cartoes), garantindo que a tag `:latest` esteja sempre atualizada com a versão mais recente do código.

-----

## 🛠️ Tecnologias Utilizadas

  - **Backend:**
      - [Python](https://www.python.org/)
      - [Flask](https://flask.palletsprojects.com/)
  - **Frontend:**
      - HTML5
      - CSS3
      - [Bootstrap 5](https://getbootstrap.com/)
  - **Containerização e CI/CD:**
      - [Docker](https://www.docker.com/)
      - [GitHub Actions](https://github.com/features/actions)
