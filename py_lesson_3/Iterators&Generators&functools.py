# 1
from random import randrange
from datetime import datetime

class Counter:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        return self

    def next(self):
        if self.lst:
            return self.lst.pop(randrange(0, len(self.lst)))
        else:
            raise StopIteration

# 2
def custom_yield(lst, n_max):
    n_sum = 0
    for i in lst:
        n_sum += i
        if n_sum <= n_max:
            yield i
        else:
            raise StopIteration

if __name__ == "__main__":
    # 1
    print(list(Counter(list(range(10)))))
    # 2
    print(list(custom_yield(range(10), 11)))
    print(list(custom_yield(range(10), 99)))
    # 3
    for i in ['12 Jan 1989']:
        print(type(datetime.strptime(i, '%d %b %Y')))