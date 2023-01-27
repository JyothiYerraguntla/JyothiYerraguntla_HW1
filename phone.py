import re

def validate_phone(string):
    matches = [i for i in re.finditer(r'^(\+1\s|\d{3}-)?\(?\d{3}\)?[-\s.]?\d{3}[-\s.]?\d{4}',string)]
    return matches != []