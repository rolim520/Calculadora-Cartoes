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

Para garantir o resultado **perfeito** e não apenas uma boa estimativa, a calculadora implementa um algoritmo de busca exaustiva (ou *brute-force*). A lógica funciona da seguinte forma:

1.  **Iteração Centavo por Centavo:** O valor total da recarga é dividido em centavos. O algoritmo então testa todas as combinações possíveis de divisão desse valor entre os dois cartões. Por exemplo, para uma recarga de R$ 10,00, ele testará (R$ 0,01 para o Cartão 1, R$ 9,99 para o Cartão 2), (R$ 0,02 para o C1, R$ 9,98 para o C2), e assim por diante.

2.  **Cálculo de Passagens:** Para cada combinação, a aplicação calcula quantas passagens podem ser compradas em cada cartão, somando o saldo existente com a fatia da recarga.

3.  **Precisão com `Decimal`:** Todas as operações financeiras utilizam o tipo `Decimal` do Python. Isso é crucial para evitar os minúsculos erros de arredondamento que ocorrem com tipos de ponto flutuante padrão (`float`), garantindo que os cálculos sejam exatos, como em uma calculadora financeira.

4.  **Seleção da Melhor Opção:** O algoritmo armazena a combinação que resulta na menor diferença de passagens entre os dois cartões. Se encontrar uma combinação que zera a diferença, ele para imediatamente, pois o resultado ótimo foi encontrado.

Este método garante que a resposta fornecida é sempre a melhor possível, sem exceções.

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

