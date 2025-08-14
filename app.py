import math
from decimal import Decimal, getcontext
from flask import Flask, render_template, request

# Define a precisão para cálculos com Decimal, evitando erros de ponto flutuante
getcontext().prec = 10

# Inicializa a aplicação Flask
app = Flask(__name__)

def calculate_optimal_distribution(balance1_str, balance2_str, total_recharge_str, price1_str, price2_str):
    """
    Calcula a distribuição ótima de recarga para dois cartões, minimizando a diferença
    no número de passagens que cada um pode comprar.

    A lógica otimizada itera sobre o número de passagens possíveis para o primeiro cartão,
    calcula a recarga mínima necessária para atingir essa quantidade e, em seguida,
    encontra a melhor combinação que equilibra as passagens entre os dois cartões.

    Args:
        balance1_str (str): Saldo atual do cartão 1.
        balance2_str (str): Saldo atual do cartão 2.
        total_recharge_str (str): Valor total da recarga.
        price1_str (str): Preço da passagem para o cartão 1.
        price2_str (str): Preço da passagem para o cartão 2.

    Returns:
        dict: Um dicionário com a solução ótima encontrada.
    """
    # Converte todas as entradas para Decimal para garantir a precisão matemática
    balance1 = Decimal(balance1_str)
    balance2 = Decimal(balance2_str)
    total_recharge = Decimal(total_recharge_str)
    # Garante que o preço nunca seja zero para evitar divisão por zero
    price1 = Decimal(price1_str) if Decimal(price1_str) > 0 else Decimal('1')
    price2 = Decimal(price2_str) if Decimal(price2_str) > 0 else Decimal('1')

    best_solution = {"difference": float('inf')}

    # Calcula o número máximo de passagens que o cartão 1 poderia ter
    # se toda a recarga fosse para ele.
    max_tickets_c1 = math.floor((balance1 + total_recharge) / price1)

    # Itera sobre cada quantidade possível de passagens para o cartão 1.
    for n1 in range(max_tickets_c1 + 1):
        # Calcula a recarga mínima necessária para o cartão 1 atingir 'n1' passagens.
        # O valor é max(0, ...) para garantir que a recarga não seja negativa.
        recharge_c1 = max(Decimal('0'), n1 * price1 - balance1)
        
        # Arredonda para o próximo centavo, garantindo que o valor seja suficiente.
        recharge_c1 = math.ceil(recharge_c1 * 100) / Decimal(100)

        # Se a recarga necessária for maior que o total disponível, podemos parar.
        if recharge_c1 > total_recharge:
            break

        # A recarga para o cartão 2 é o que sobra do total.
        recharge_c2 = total_recharge - recharge_c1

        # Calcula quantas passagens o cartão 2 consegue comprar com a recarga restante.
        n2 = math.floor((balance2 + recharge_c2) / price2)
        
        difference = abs(n1 - n2)

        # Se a diferença atual for menor que a melhor encontrada, atualiza a solução.
        if difference < best_solution["difference"]:
            best_solution = {
                "recharge_c1": recharge_c1,
                "recharge_c2": recharge_c2,
                "tickets_c1": n1,
                "tickets_c2": n2,
                "difference": difference
            }
        
        # Otimização: se a diferença for 0, a solução perfeita foi encontrada.
        if best_solution["difference"] == 0:
            break
            
    return best_solution

@app.route('/', methods=['GET', 'POST'])
def index():
    # Dicionário de contexto para armazenar os valores do formulário e a solução.
    # Isso permite que os valores digitados pelo usuário permaneçam na tela.
    context = {
        "solution": None,
        "r1": "0",
        "r2": "0",
        "total_recharge": "10.00",
        "p1": "4.70",
        "p2": "5.00"
    }

    # Se o formulário for enviado (método POST)
    if request.method == 'POST':
        try:
            # Obtém os valores do formulário e atualiza o contexto
            context['r1'] = request.form.get('r1', '0')
            context['r2'] = request.form.get('r2', '0')
            context['total_recharge'] = request.form.get('total_recharge', '0')
            context['p1'] = request.form.get('p1')
            context['p2'] = request.form.get('p2')

            # Chama a função de cálculo para encontrar a distribuição ótima
            solution = calculate_optimal_distribution(
                context['r1'], context['r2'], context['total_recharge'], context['p1'], context['p2']
            )
            context['solution'] = solution
        except Exception as e:
            # Em caso de erro, exibe uma mensagem amigável na interface
            context['solution'] = {"error": f"Erro ao processar a solicitação: {e}"}
            
    # Renderiza o template HTML, passando o contexto com os dados
    return render_template('index.html', context=context)

if __name__ == '__main__':
    # Executa a aplicação Flask. O host '0.0.0.0' torna a aplicação acessível
    # a partir de outras máquinas na mesma rede (útil para Docker).
    app.run(host='0.0.0.0', port=5000)
