import re
from currency import validate_currency
from date import validate_date
from phone import validate_phone
from tags import validate_tags

with open('input.txt', 'r') as file:
    inputs = file.readlines()
    for input in inputs:
        print('Input:', input)
        print('Currency:', validate_currency(input))
        print('Date:', validate_date(input))
        print('Phone:', validate_phone(input))
        print('Tags:', validate_tags(input))
        print()
