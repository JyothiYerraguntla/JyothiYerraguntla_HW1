import re

def validate_date(string):
    matches = [i for i in re.finditer((r'^(January|February|March|April|May|June|July|August|September|October|November|December)\s([0-9]?[0-9]), ([1-2][0-9][0-9][0-9])|^(0[1-9]|[12][0-9]|3[01])-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec),\s(19|20)\d{2}$|^\d{4}-(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])$|^(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01])/(\d{2})$'),string)]
    return matches != []

