# This takes an email and slices it into it's username, domain name & extension
# collect email from user
# split the email using the @, save the first part as username, the second part as domani
# then split domian using .


def slicer():
    print('Welcome to the email slicer')
    print('')

    email_input = input('Enter your email address: ')

    (username, domain) = email_input.split('@')
    (domain, extension) = domain.split('.')

    print('Username: ', username)
    print('Domain: ', domain)
    print('Extension: ', extension)
