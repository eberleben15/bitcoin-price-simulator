from flask import Flask, jsonify, render_template
from simulator import generate_price_series
from logger import get_logger

app = Flask(__name__, static_folder='web', template_folder='web')
logger = get_logger()

# Initialize with a reasonable starting base price
current_price = 20000


app = Flask(__name__, static_folder='web', template_folder='web')

@app.route('/')
def home():
    # Ensure that Flask is looking in the correct directory
    print("Template folder:", app.template_folder)
    return render_template('index.html')

@app.route('/price')
def get_price():
    global current_price
    current_price = generate_price_series(last_price=current_price)
    logger.debug(f"Current simulated price fetched: ${current_price:.2f}")  # Log the price fetched
    return jsonify({'price': current_price})

if __name__ == '__main__':
    logger.info("Starting the Bitcoin price simulator server...")
    app.run(debug=True, host='0.0.0.0', port=5000)