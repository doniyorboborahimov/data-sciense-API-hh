import sys

def search_stock_price(company_name):
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

    # Check if the company is in the COMPANIES dictionary
    if company_name in COMPANIES:
        stock_symbol = COMPANIES[company_name]
        print(STOCKS[stock_symbol])
    else:
        print("Unknown company")

if __name__ == '__main__':
    # Check if exactly one argument is passed
    if len(sys.argv) == 2:
        company_name = sys.argv[1].capitalize()  # Capitalize the company name to match keys
        search_stock_price(company_name)
    else:
        # Do nothing if no argument or more than one argument is passed
        pass
