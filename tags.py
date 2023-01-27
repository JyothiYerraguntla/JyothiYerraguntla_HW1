import re

def validate_tags(string):
    matches = [i for i in re.finditer(r"<\/?[a-z][a-z0-9]*[^<>]*>", string)]
    return matches != []