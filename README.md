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

Para garantir um resultado **perfeito** com a máxima performance, a calculadora implementa um algoritmo híbrido avançado:

1.  **Busca Binária Rápida:** Primeiramente, o algoritmo usa uma busca binária (*binary search*) para encontrar rapidamente a região aproximada onde a solução ótima se encontra. Em vez de testar todas as possibilidades, ele corta o universo de busca pela metade a cada passo, convergindo para a área de interesse de forma quase instantânea.

2.  **Análise de Precisão por Breakpoints:** Uma vez que a busca binária delimita uma pequena faixa de valores, o algoritmo muda para uma análise de "breakpoints". Ele inspeciona apenas os pontos de recarga críticos dentro dessa faixa — os valores exatos onde o número de passagens poderia mudar.

3.  **Seleção da Melhor Opção:** Ao testar apenas esses pontos críticos, o algoritmo identifica a combinação de recarga que resulta no equilíbrio perfeito (a menor diferença possível de passagens entre os cartões).

4.  **Exatidão com `Decimal`:** Todas as operações financeiras utilizam o tipo `Decimal` do Python, eliminando os erros de arredondamento de tipos de ponto flutuante e garantindo que o resultado seja matematicamente exato.

Essa abordagem em duas fases combina a velocidade da busca binária com a precisão da análise de breakpoints, garantindo a melhor solução possível da forma mais eficiente.

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

