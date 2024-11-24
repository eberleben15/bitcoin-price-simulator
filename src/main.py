from flask import Flask, jsonify, render_template
from simulator import generate_price_series
from logger import get_logger
from BitcoinSimulatorGBM import BitcoinSimulatorGBM
import os

# Set up the directory path relative to the main.py file
current_directory = os.path.dirname(os.path.abspath(__file__))
template_directory = os.path.join(current_directory, '../web')

app = Flask(__name__, static_folder=template_directory, template_folder=template_directory)

logger = get_logger()

# Create an instance of the BitcoinSimulatorGBM
simulator = BitcoinSimulatorGBM()

@app.route('/')
def home():
    # Ensure that Flask is looking in the correct directory
    print("Template folder:", app.template_folder)
    return render_template('index.html')

@app.route('/price')
def get_price():
    # Generate the next price using the GBM model
    price = simulator.simulate_next_price()
    # Return the new price as a JSON response
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)