import numpy as np

class BitcoinSimulatorGBM:
    def __init__(self, initial_price=92287, drift_rate=0.0002, volatility=0.01):
        """
        Initialize the Bitcoin simulator with Geometric Brownian Motion.

        Parameters:
        - initial_price (float): The starting price of Bitcoin.
        - drift_rate (float): The expected return of Bitcoin, per time unit.
        - volatility (float): The volatility of the returns (standard deviation).
        """
        self.current_price = initial_price
        self.drift_rate = drift_rate
        self.volatility = volatility

    def simulate_next_price(self):
        """
        Simulate the next price using the GBM formula.

        Returns:
        - float: The next simulated price.
        """
        # Calculate the random shock using a standard normal distribution
        shock = np.random.normal()
        # Calculate the change in price
        price_change = (self.drift_rate - 0.5 * self.volatility ** 2) + self.volatility * shock
        # Update the current price
        self.current_price *= np.exp(price_change)
        return self.current_price

# Example usage:
simulator = BitcoinSimulatorGBM()
for _ in range(10):
    print(simulator.simulate_next_price())