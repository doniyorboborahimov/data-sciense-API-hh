import sys

def all_stocks():
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

    # Check if there is exactly one argument
    if len(sys.argv) != 2:
        return

    # Get the input string and strip any extra spaces
    input_string = sys.argv[1].strip()

    # If there are two consecutive commas, do nothing
    if ',,' in input_string:
        return

    # Split the string by commas and clean up spaces
    expressions = [expr.strip() for expr in input_string.split(',')]

    # Iterate through each expression
    for expression in expressions:
        if expression == '':
            continue  # Ignore empty expressions

        expression_upper = expression.upper()  # Make case-insensitive for ticker comparison
        expression_lower = expression.lower()  # Make case-insensitive for company name comparison

        # Check if the expression is a ticker symbol
        if expression_upper in STOCKS:
            # Find the company name associated with the ticker
            company_name = [company for company, symbol in COMPANIES.items() if symbol.upper() == expression_upper][0]
            print(f"{expression_upper} is a ticker symbol for {company_name}")
        elif expression_lower in [company.lower() for company in COMPANIES.keys()]:
            # Find the ticker and stock price for the company
            company_name = [company for company in COMPANIES.keys() if company.lower() == expression_lower][0]
            ticker_symbol = COMPANIES[company_name]
            print(f"{company_name} stock price is {STOCKS[ticker_symbol]}")
        else:
            print(f"{expression} is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    all_stocks()
