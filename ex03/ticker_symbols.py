import sys

def search_by_ticker(ticker_symbol):
    # Dictionaries with company names and stock prices
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    # Check if the ticker symbol exists in the STOCKS dictionary
    ticker_symbol = ticker_symbol.upper()  # Normalize to uppercase for consistent comparison
    if ticker_symbol in STOCKS:
        # Find the company name associated with the ticker symbol
        company_name = [company for company, symbol in COMPANIES.items() if symbol == ticker_symbol][0]
        print(f"{company_name} {STOCKS[ticker_symbol]}")
    else:
        print("Unknown ticker")

if __name__ == '__main__':
    # Check if exactly one argument is passed
    if len(sys.argv) == 2:
        ticker_symbol = sys.argv[1]
        search_by_ticker(ticker_symbol)
    else:
        # Do nothing if no argument or more than one argument is passed
        pass
