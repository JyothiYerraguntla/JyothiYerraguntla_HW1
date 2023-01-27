import re
from currency import validate_currency
from date import validate_date
from phone import validate_phone
from tags import validate_tags

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print('Input:', line)
        print('Currency:', validate_currency(line))
        print('Date:', validate_date(line))
        print('Phone:', validate_phone(line))
        print('Tags:', validate_tags(line))
        print()
