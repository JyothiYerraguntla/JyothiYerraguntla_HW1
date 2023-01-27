import re


def validate_currency(string):
    mathches = [i for i in re.finditer(r"[-|+]?[$|USD]+([0-9]{1,3}(\,[0-9]{3})*|([0-9]+))(\.[0-9]{2})?((?:M|B|K)?)", string)]
    return mathches != []


# string= "this is $4B"
# print(check_valid_currency(string))