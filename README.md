# 📈 Python Correlations Trading Strategy

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-2.2.3-blue.svg)
![YFinance](https://img.shields.io/badge/yfinance-0.2.57-green.svg)
![Matplotlib](https://img.shields.io/badge/matplotlib-3.10.1-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🎯 Overview

A correlation-based trading strategy using Python, analyzing the relationship between two assets to generate trading signals. The strategy is based on the concept of mean reversion in correlation between assets.

## ✨ Features

- 📊 Real-time stock data fetching with retry logic
- 🔄 Correlation analysis between two assets
- 📈 Rolling correlation calculations
- 🎯 Signal generation based on correlation thresholds
- 📉 Visualization of correlation patterns and trading signals
- ⚡ Rate limiting and error handling

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/pakagronglb/python-correlations-trading-strategy.git
cd python-correlations-trading-strategy
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📋 Requirements

- Python 3.13+
- pandas
- yfinance
- matplotlib
- numpy

## 🚀 Usage

1. Import the necessary functions:
```python
from stock_data import fetch_stock_data
from correlation_strategy import calculate_correlation_signals, plot_correlation_signals
```

2. Fetch stock data:
```python
asset1_prices = fetch_stock_data('AAPL')
asset2_prices = fetch_stock_data('MSFT')
```

3. Calculate correlation signals:
```python
result = calculate_correlation_signals(data, 'AAPL', 'MSFT', window=50, wide_window=100, std_factor=1)
```

4. Visualize the results:
```python
plot_correlation_signals(result)
```

## 📊 Strategy Details

The strategy works by:
1. Calculating a rolling correlation between two assets
2. Computing a longer-term average correlation
3. Identifying significant deviations from the average
4. Generating signals when correlations move outside normal ranges

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Credits

This project was inspired by the tutorial from [CodeTrading](https://www.youtube.com/watch?v=O13aUVSs5pQ&ab_channel=CodeTrading).

Special thanks to:
- [CodeTrading](https://www.youtube.com/@CodeTrading) for the original concept and tutorial
- The yfinance team for providing the stock data API
- The pandas and matplotlib teams for their excellent data analysis tools

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## 📈 Disclaimer

This project is for educational purposes only. Trading stocks involves risk, and past performance is not indicative of future results. Always do your own research and consult with a financial advisor before making investment decisions. 