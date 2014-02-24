from functools import partial
from datetime import datetime

def strptime_wrapper(pattern, value):
    return datetime.strptime(value, pattern)

to_datetime = partial(strptime_wrapper, '%d %b %Y')
print(list(map(to_datetime, ['12 Jan 1989'])))