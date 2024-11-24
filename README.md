# bittcoin-price-simulator

This project simulates Bitcoin price movements using Geometric Brownian Motion (GBM), a common stochastic process used in the financial industry to model stock prices, commodities, and cryptocurrencies. The simulator is designed to provide a realistic emulation of Bitcoin price fluctuations over time, offering a valuable tool for testing trading strategies or financial applications.

## Features

- **Realistic Price Simulation**: Utilizes GBM to generate price paths that reflect the volatility and drift characteristic of Bitcoin.
- **Flask API**: Includes a Flask server that provides real-time simulated price data via a REST API.
- **Dynamic Adjustment**: Allows users to adjust volatility and drift parameters to simulate different market conditions.

## Prerequisites

To run this project, you will need Python and Flask installed on your machine. The project is developed using Python 3.12.

## Setup

Follow these steps to set up and run the simulator:

1. **Clone the repository**
git clone https://yourrepository.com/bitcoin-price-simulator.git
cd bitcoin-price-simulator

2. **Build the Docker image**
docker build -t bitcoin-simulator .

3. **Run the Docker container**
docker run -p 5000:5000 bitcoin-simulator

This will start the Flask server on `http://localhost:5000`, serving the simulated Bitcoin prices.

This will start the Flask server inside a Docker container on `http://localhost:5000`, serving the simulated Bitcoin prices.

## API Usage

The Flask server exposes a single API endpoint to retrieve the latest simulated Bitcoin price:

- **GET `/price`**
- **Description**: Fetches the latest simulated Bitcoin price.
- **Response**: JSON object containing the price.
 ```json
 {
   "price": 23456.78
 }
 ```

## Customization

You can customize the simulation parameters by editing the `BitcoinSimulatorGBM` class initialization values in `src/simulator.py`. Available parameters include:

- `initial_price`: Starting price of Bitcoin.
- `drift_rate`: Expected return rate, controlling the average trend.
- `volatility`: Volatility of returns, affecting price fluctuations.

## Contributing

Contributions to enhance the simulator or extend its capabilities are welcome. Please follow standard pull request procedures to submit your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.