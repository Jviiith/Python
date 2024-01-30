
def currency_converter():
    print('Welcome to Currency Converter\n')
    print('This converts US Dollars into UK Pounds Sterling\n')

    # evaluates the expression as a str and returns value as an int
    dollars = eval(input('Enter amount in dollars: '))
    pounds = convert_to_pounds(dollars)
    print('Amount In Pounds: %.2f' % pounds)


def convert_to_pounds(dollars): return dollars * 0.82  # or
# convert_to_pounds = lambda dollars: dollars * 0.82 (the exchange rate)


currency_converter()
