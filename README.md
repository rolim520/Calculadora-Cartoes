# Calculadora de Recarga de Cartões de Transporte

![Project Banner](./image.png)

## 🎯 Sobre o Projeto

A **Calculadora de Recarga** é uma aplicação web inteligente projetada para otimizar o uso de dois cartões de transporte (como Riocard e Jaé). Com base no saldo atual de cada cartão, no valor da recarga e nas tarifas, a ferramenta calcula a distribuição exata da recarga para maximizar o número total de passagens, garantindo o melhor aproveitamento do seu dinheiro.

Chega de fazer contas de cabeça ou desperdiçar saldo!

---

## ✨ Funcionalidades

-   **Cálculo Otimizado:** Garante a melhor distribuição possível da recarga.
-   **Interface Moderna e Responsiva:** Design limpo que funciona perfeitamente em desktops e celulares.
-   **Tarifas Flexíveis:** Permite inserir os valores exatos das tarifas para cada cartão.
-   **Nomes Personalizáveis:** As legendas dos cartões foram atualizadas para "Jaé" e "Riocard".
-   **Persistência de Dados:** O formulário memoriza os últimos valores inseridos para agilizar o uso.

---

## 💡 Lógica de Otimização

Para garantir o resultado **perfeito**, a calculadora implementa um algoritmo de busca focado em eficiência:

1.  **Iteração por Passagens:** O algoritmo testa de forma inteligente as combinações de recarga ao iterar sobre o número de passagens de um cartão. Para cada quantidade de passagens possível, ele calcula a recarga exata necessária.

2.  **Cálculo e Distribuição:** Com base na recarga calculada para o primeiro cartão, o valor restante é alocado ao segundo, e o número de passagens para este é determinado.

3.  **Busca pela Melhor Opção:** O sistema compara a quantidade de passagens entre os dois cartões e armazena a combinação de recarga que resulta no maior equilíbrio (a menor diferença de passagens).

4.  **Análise Completa:** Para assegurar a solução ótima, o processo é repetido, invertendo a perspectiva e começando a iteração a partir do segundo cartão.

5.  **Precisão Financeira:** Todas as operações utilizam o tipo `Decimal` do Python para evitar erros de arredondamento e garantir exatidão nos cálculos de saldo e recarga.

Este método garante que a resposta fornecida é sempre a melhor possível, de forma rápida e precisa.

---

## 🚀 Como Executar

Este projeto é totalmente containerizado com Docker, tornando a execução simples e rápida.

### Pré-requisitos

-   [Docker](https://www.docker.com/get-started)
-   [Docker Compose](https://docs.docker.com/compose/install/)

### Passos

1.  **Clone este repositório:**
    ```bash
    git clone https://github.com/rolim520/Calculadora-Cartoes.git
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd Calculadora-Cartoes
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

