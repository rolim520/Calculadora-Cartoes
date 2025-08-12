import math
from decimal import Decimal, getcontext
from flask import Flask, render_template, request

# Set precision for Decimal calculations
getcontext().prec = 10

# Initialize the Flask application
app = Flask(__name__)

# --- New Feature: Define a list of common ticket prices ---
TICKET_PRICES = [
    '4.70', '5.00', '3.80', '6.20', '7.50'
]

def find_optimal_by_tickets(r1_str, r2_str, total_recharge_str, p1_str, p2_str):
    """
    Finds the optimal distribution by iterating through the number of possible tickets.
    """
    # Convert all inputs to Decimal for precision
    r1 = Decimal(r1_str)
    r2 = Decimal(r2_str)
    total_recharge = Decimal(total_recharge_str)
    p1 = Decimal(p1_str) if Decimal(p1_str) > 0 else Decimal('1')
    p2 = Decimal(p2_str) if Decimal(p2_str) > 0 else Decimal('1')

    best_solution = {"difference": float('inf'), "recharge_c1": Decimal('0'), "recharge_c2": total_recharge, "tickets_c1": math.floor(r1/p1), "tickets_c2": math.floor((r2+total_recharge)/p2)}

    # Iterate from card 1's perspective
    current_n1 = math.floor(r1 / p1)
    max_n1 = math.floor((r1 + total_recharge) / p1)
    for n1 in range(int(current_n1), int(max_n1) + 2):
        recharge_c1 = (n1 * p1) - r1
        if recharge_c1 < Decimal('0'):
            recharge_c1 = Decimal('0')
        
        if recharge_c1 > total_recharge:
            continue

        recharge_c1 = recharge_c1.quantize(Decimal('0.01'))
        recharge_c2 = total_recharge - recharge_c1

        n2 = math.floor((r2 + recharge_c2) / p2)
        difference = abs(n1 - n2)

        if difference < best_solution["difference"]:
            best_solution = {
                "recharge_c1": recharge_c1,
                "recharge_c2": recharge_c2,
                "tickets_c1": n1,
                "tickets_c2": n2,
                "difference": difference
            }
        if best_solution["difference"] == 0:
            break
    
    # Iterate from card 2's perspective to ensure full coverage
    current_n2 = math.floor(r2 / p2)
    max_n2 = math.floor((r2 + total_recharge) / p2)
    for n2 in range(int(current_n2), int(max_n2) + 2):
        recharge_c2 = (n2 * p2) - r2
        if recharge_c2 < Decimal('0'):
            recharge_c2 = Decimal('0')

        if recharge_c2 > total_recharge:
            continue
            
        recharge_c2 = recharge_c2.quantize(Decimal('0.01'))
        recharge_c1 = total_recharge - recharge_c2

        n1 = math.floor((r1 + recharge_c1) / p1)
        difference = abs(n1 - n2)

        if difference < best_solution["difference"]:
            best_solution = {
                "recharge_c1": recharge_c1,
                "recharge_c2": recharge_c2,
                "tickets_c1": n1,
                "tickets_c2": n2,
                "difference": difference
            }
        if best_solution["difference"] == 0:
            break
            
    return best_solution

@app.route('/', methods=['GET', 'POST'])
def index():
    # --- New Feature: Use a context dictionary to manage state ---
    context = {
        "solution": None,
        "r1": "0",
        "r2": "0",
        "total_recharge": "10.00",
        "p1": "4.70",
        "p2": "5.00"
    }

    if request.method == 'POST':
        try:
            # Get values from the form and update context to persist state
            context['r1'] = request.form.get('r1', '0')
            context['r2'] = request.form.get('r2', '0')
            context['total_recharge'] = request.form.get('total_recharge', '0')
            context['p1'] = request.form.get('p1')
            context['p2'] = request.form.get('p2')

            # Call the optimal calculation function
            solution = find_optimal_by_tickets(
                context['r1'], context['r2'], context['total_recharge'], context['p1'], context['p2']
            )
            context['solution'] = solution
        except Exception as e:
            context['solution'] = {"error": f"Erro: {e}"}
            
    return render_template('index.html', context=context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
