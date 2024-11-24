import numpy as np

class BitcoinSimulatorGBM:
    def __init__(self, initial_price=20000, drift_rate=0.00002, volatility=0.001, sma_period=60, ema_period=60):
        self.current_price = initial_price
        self.drift_rate = drift_rate
        self.volatility = volatility
        self.prices = [initial_price] * sma_period
        self.sma_period = sma_period
        self.ema = initial_price
        self.ema_period = ema_period
        self.ema_smoothing = 2

    def simulate_next_price(self):
        shock = np.random.normal()
        price_change = (self.drift_rate - 0.5 * self.volatility ** 2) + self.volatility * shock
        self.current_price *= np.exp(price_change)
        self.current_price = max(0, self.current_price)
        self.prices.append(self.current_price)
        if len(self.prices) > self.sma_period:
            self.prices.pop(0)
        return self.current_price

    def get_sma(self):
        if len(self.prices) >= self.sma_period:
            return sum(self.prices[-self.sma_period:]) / self.sma_period
        return None  # Or handle lack of data appropriately

    def get_ema(self):
        if not hasattr(self, 'ema'):  # Check if EMA is already initialized
            self.ema = self.prices[0]  # Initialize with the first price or an average of initial prices
        for price in self.prices:
            self.ema = (price * (2 / (1 + self.ema_period))) + (self.ema * (1 - (2 / (1 + self.ema_period))))
        return self.ema

# Example usage:
simulator = BitcoinSimulatorGBM()
for _ in range(100):
    next_price = simulator.simulate_next_price()
    sma = simulator.get_sma()
    print(f"Next Price: {next_price}, SMA: {sma}")