import math
from decimal import Decimal, getcontext
from flask import Flask, render_template, request

# Define a precisão para cálculos com Decimal, evitando erros de ponto flutuante
getcontext().prec = 10

# Inicializa a aplicação Flask
app = Flask(__name__)

def calculate_optimal_distribution(balance1_str, balance2_str, total_recharge_str, price1_str, price2_str, desired_difference_str):
    """
    Calcula a distribuição de recarga que mais se aproxima de uma diferença
    desejada no número de passagens entre dois cartões.

    Args:
        balance1_str (str): Saldo atual do cartão 1.
        balance2_str (str): Saldo atual do cartão 2.
        total_recharge_str (str): Valor total da recarga.
        price1_str (str): Preço da passagem para o cartão 1.
        price2_str (str): Preço da passagem para o cartão 2.
        desired_difference_str (str): A diferença desejada de passagens (n1 - n2).

    Returns:
        dict: Um dicionário com a solução ótima encontrada.
    """
    # Converte todas as entradas para o tipo correto
    balance1 = Decimal(balance1_str)
    balance2 = Decimal(balance2_str)
    total_recharge = Decimal(total_recharge_str)
    price1 = Decimal(price1_str) if Decimal(price1_str) > 0 else Decimal('1')
    price2 = Decimal(price2_str) if Decimal(price2_str) > 0 else Decimal('1')
    desired_difference = int(desired_difference_str)

    # 'cost' representa o quão longe a solução atual está do alvo (diferença desejada).
    # O objetivo é minimizar esse custo.
    best_solution = {"cost": float('inf')}

    # Calcula o número máximo de passagens que o cartão 1 poderia ter
    max_tickets_c1 = math.floor((balance1 + total_recharge) / price1)

    # Itera sobre cada quantidade possível de passagens para o cartão 1
    for n1 in range(max_tickets_c1 + 1):
        # Calcula a recarga mínima para o cartão 1 atingir 'n1' passagens
        recharge_c1 = max(Decimal('0'), n1 * price1 - balance1)
        recharge_c1 = math.ceil(recharge_c1 * 100) / Decimal(100)

        if recharge_c1 > total_recharge:
            break

        recharge_c2 = total_recharge - recharge_c1
        n2 = math.floor((balance2 + recharge_c2) / price2)
        
        # Calcula o "custo": a distância entre a diferença atual e a desejada
        cost = abs((n1 - n2) - desired_difference)

        # Se o custo atual for o menor encontrado, atualiza a melhor solução
        if cost < best_solution["cost"]:
            best_solution = {
                "recharge_c1": recharge_c1,
                "recharge_c2": recharge_c2,
                "tickets_c1": n1,
                "tickets_c2": n2,
                "cost": cost
            }
        
        # Otimização: se o custo for 0, a solução perfeita foi encontrada
        if best_solution["cost"] == 0:
            break
            
    return best_solution

@app.route('/', methods=['GET', 'POST'])
def index():
    # Contexto para armazenar os valores do formulário e a solução
    context = {
        "solution": None,
        "r1": "0",
        "r2": "0",
        "total_recharge": "10.00",
        "p1": "4.70",
        "p2": "5.00",
        "desired_difference": "0"  # Valor padrão para a diferença
    }

    if request.method == 'POST':
        try:
            # Obtém os valores do formulário e atualiza o contexto
            context['r1'] = request.form.get('r1', '0')
            context['r2'] = request.form.get('r2', '0')
            context['total_recharge'] = request.form.get('total_recharge', '0')
            context['p1'] = request.form.get('p1')
            context['p2'] = request.form.get('p2')
            context['desired_difference'] = request.form.get('desired_difference', '0')

            # Chama a função de cálculo com o novo parâmetro
            solution = calculate_optimal_distribution(
                context['r1'], context['r2'], context['total_recharge'], 
                context['p1'], context['p2'], context['desired_difference']
            )
            context['solution'] = solution
        except Exception as e:
            context['solution'] = {"error": f"Erro ao processar a solicitação: {e}"}
            
    return render_template('index.html', context=context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
