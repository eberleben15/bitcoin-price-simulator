import numpy as np
import logging

logger = logging.getLogger('BitcoinTrader')

def generate_price_series(base_price=20000, last_price=None, drift=0.0002, daily_volatility=0.04):
    """ Generate the next price based on previous price with more realistic fluctuation. """
    if last_price is None:
        last_price = base_price
    
    # Calculate seconds in a day for volatility adjustment
    seconds_in_day = 86400
    shock_stddev = daily_volatility / (seconds_in_day ** 0.5)
    
    # Calculate a random shock based on adjusted volatility
    shock = np.random.normal(0, shock_stddev) * last_price
    
    # Apply the shock and drift to the last price
    new_price = last_price + last_price * drift + shock
    
    # Ensure the price does not go negative
    new_price = max(0, new_price)
    
    logger.debug(f"Generated price: {new_price}")
    return new_price