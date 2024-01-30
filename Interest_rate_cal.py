# collect necessary data: principal(intial loan amount borrowed), APR(annual interest rate), years(amount of years t pay the loan back)
# calculate the monthly payment
# show user

def monthly_payment_cal():
    print('Welcome to your monthly payment loan calculator \n')

    principal = float(input('Enter Loan amount taken: '))
    apr = float(input('Enter anual interest rate: '))
    years = int(input('Enter amount of years: '))

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / \
        (1 - (1 + monthly_interest_rate) ** (amount_of_months))

    print('Monthly payment is: %.2f' % monthly_payment)
