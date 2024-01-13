# This project is a weight converter
weight = int(input('Enter your weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
    convert_in_kg = weight * 0.45
    print(f'Weight converted into kilograms: {convert_in_kg}')
else:
    convert_in_lbs = weight / 0.45
    print(f'Weight converted into pounds: {convert_in_lbs}')

# Same code but written as a function():
def kg_to_lbs(weight):
    return weight * 0.45
def lbs_to_kg(weight):
    return weight / 0.45
