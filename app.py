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

def find_optimal_distribution(r1_str, r2_str, total_recharge_str, p1_str, p2_str):
    """
    Finds the optimal recharge distribution using Decimal for precision.
    Now accepts ticket prices as arguments.
    """
    # Convert string inputs to Decimal for precise calculations
    r1 = Decimal(r1_str)
    r2 = Decimal(r2_str)
    total_recharge = Decimal(total_recharge_str)
    p1 = Decimal(p1_str)
    p2 = Decimal(p2_str)
    
    best_solution = {
        "recharge_c1": Decimal('0'),
        "recharge_c2": total_recharge,
        "tickets_c1": 0,
        "tickets_c2": 0,
        "difference": float('inf')
    }

    # Iterate over every possible cent
    total_recharge_cents = int(total_recharge * 100)
    
    for i in range(total_recharge_cents + 1):
        recarga_c1 = Decimal(i) / 100
        recarga_c2 = total_recharge - recarga_c1

        tickets_c1 = math.floor((r1 + recarga_c1) / p1) if p1 > 0 else 0
        tickets_c2 = math.floor((r2 + recarga_c2) / p2) if p2 > 0 else 0
        
        difference = abs(tickets_c1 - tickets_c2)

        if difference < best_solution["difference"]:
            best_solution = {
                "recharge_c1": recarga_c1,
                "recharge_c2": recarga_c2,
                "tickets_c1": tickets_c1,
                "tickets_c2": tickets_c2,
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
        "ticket_prices": TICKET_PRICES,
        "r1": "0",
        "r2": "0",
        "total_recharge": "10.00",
        "p1": TICKET_PRICES[0],
        "p2": TICKET_PRICES[1]
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
            solution = find_optimal_distribution(
                context['r1'], context['r2'], context['total_recharge'], context['p1'], context['p2']
            )
            context['solution'] = solution
        except Exception as e:
            context['solution'] = {"error": f"Erro: {e}"}
            
    return render_template('index.html', context=context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
