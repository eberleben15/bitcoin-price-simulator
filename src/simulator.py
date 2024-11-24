import numpy as np
import logging

logger = logging.getLogger('BitcoinTrader')


def generate_price_series(base_price, last_price=None, drift_rate=0.0001, shock_stddev=0.02):
    if last_price is None:
        last_price = base_price
    # Randomly choose upward or downward drift
    drift = np.random.choice([drift_rate, -drift_rate])
    # Generate a random shock based on the standard deviation
    shock = np.random.normal(0, shock_stddev) * last_price
    # Update the price, ensuring it does not go negative
    new_price = max(0, last_price + drift * last_price + shock)
    return new_price