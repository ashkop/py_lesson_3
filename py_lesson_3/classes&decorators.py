from itertools import groupby
from datetime import date


def htmlize(cls=''):
    if cls: cls = 'class="%s"' % cls
    def wrapper_params(fn):
        def wrapper(self):
            res = fn(self)
            return '<a %s href="%s">%s</a>' % (cls, res, res)
        return wrapper
    return wrapper_params

class Order(list):
    _total_orders = 0

    def append(self, item):
        self.date = date.today()
        self.__class__._total_orders += 1
        super(Order, self).append(item)

    def __init__(self, discount):
        if 0 <= discount <= 99:
            self._discount = discount
        else:
            self._discount = 0

    @classmethod
    def get_total_orders(cls):
        return cls._total_orders

    @property
    def discount(self):
        return self._discount

    @property
    def total_price(self):
        price = float(0)
        for i in self:
            price += i.price
        return price / 100 * self._discount

    def get_files(self):
        yield self

    def __str__(self):
        result = ''
        sorted_orders = sorted(self, key=lambda x: x.name)
        for name, group in groupby(sorted_orders, key=lambda x: x.name):
            lst = list(group)
            result += 'Item name: %s, quantity of items: %d, total price: %d\n'\
                      % (name, len(lst), sum(row.price for row in lst))
        return result

class Item(object):
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

class DownloadableItem(Item):
    downloads_count = 0

    def __init__(self, id, name, description, price, filename):
        self.filename = filename
        super(DownloadableItem, self).__init__(id, name, description, price)

    @htmlize('my_class')
    def get_url(self):
        self.__class__.downloads_count += 1
        return self.filename


if __name__ == "__main__":
    item1 = Item(1, 'htc', 'sux1', 1)
    item2 = Item(2, 'nokia', 'dead', 10)
    item3 = DownloadableItem(3, 'iphone', 'gold', 99, 'file3')
    item4 = DownloadableItem(4, 'htc', 'sux2', 1, 'file4')

    print('Url: %s' % item3.get_url())
    print('Url: %s' % item3.get_url())
    print('Url: %s' % item4.get_url())
    print('Downloads count: %d' % DownloadableItem.downloads_count)

    order = Order(50)
    order.append(item1)
    order.append(item2)
    order.append(item3)
    order.append(item4)

    print('Orders: \n%s' % order)
    print('Total price: %d' % order.total_price)
    print('Total orders: %d' % order.get_total_orders())
    print('Order date: %s' % order.date)
    print(order.get_files())


