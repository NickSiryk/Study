'''
Product store program
'''

class Product:
    def __init__(self, p_type, p_name, p_price):
        '''
        :param p_type: type of product
        :param p_name: name of product
        :param p_price: price of one item
        '''
        self.p_type = p_type
        self.p_name = p_name
        self.p_price = p_price

    def p_info(self):
        '''
        :return: info about product
        '''
        return (self.p_type, self.p_name, self.p_price,)

    def change_price(self, percent):
        self.p_price = round(self.p_price * ((100 + percent)/100), 2)


class Store:
    '''
    A class, which have some Products and operate them.
    All methods, in case they can’t perform its action raise ValueError with appropriate error information
    '''
    def __init__(self):
        self.storage = {}
        self.income = 0

    def get_income(self):
        '''
        :return: amount of many earned by ProductStore instance
        '''
        return self.income

    def add_product(self, product, amount):
        '''
        adds a specified quantity of a single product with a predefined price premium for store(30 percent)
        :param product: Product for adding
        :param amount: Amount of Product
        '''
        if product.__class__ != Product:
            raise ValueError('This product is not in class "Product"')
        else:
            product.change_price(30)
            if product in self.storage:
                self.storage[product] += amount
            else:
                self.storage[product] = amount

    def all_products(self):
        '''
        :return: information about all available products in the store.
        '''
        print('____Here_is_Your_Store____')
        for i in self.storage:
            print(f'{i.p_info()}, quant = {self.storage[i]}')
        print('_______End_of_Store_______')

    def get_product_info(self, product_name):
        '''
        :param product_name:
        :return: a tuple with product name and amount of items in the store.
        '''
        if type(product_name) != str:
            raise ValueError('This is not a name')
        else:
            for i in self.storage:
                if getattr(i, 'p_name') == product_name:
                    return (i.p_name, self.storage[i],)

    def get_product_deep_info(self, product_name):
        '''
        :param product_name:
        :return: all info about product
        '''
        if type(product_name) != str:
            raise ValueError('This is not a name')
        else:
            for i in self.storage:
                if getattr(i, 'p_name') == product_name:
                    print(i.p_info())

    def set_discount(self, identifier, percent, identifier_type='p_name'):
        '''
        adds a discount for all products specified by input identifiers
        :param identifier: type or name
        :param percent: amount of discount in percentage
        :param identifier_type:
        '''
        if type(identifier) != str:
            raise ValueError('This is not a name or type')
        if type(percent) != int:
            raise ValueError('Percent should be a digit')
        for i in self.storage:
            if getattr(i, identifier_type) == identifier:
                i.change_price(-percent)

    def sell_product(self, product_name, amount):
        '''
        removes a particular amount of products from the store if available, in other case raises an error
        It also increments income if the sell_product method succeeds.
        '''
        if type(product_name) != str:
            raise ValueError('This is not a name')
        if type(amount) != int:
            raise ValueError('Amount should be a digit')
        if product_name not in (i.p_name for i in self.storage):
            raise ValueError('No such product in store!')
        else:
            for i in self.storage:
                if i.p_name == product_name:
                    if self.storage[i] < amount:
                        print(f'Not enough quantity! Only: {self.get_product_info(product_name)}')
                    elif self.storage[i] == amount:
                        self.income += amount * i.p_price
                        del self.storage[i]
                        print(f'No more {product_name} in the store!')
                    else:
                        self.income += amount * i.p_price
                        self.storage[i] -= amount
                        print(f'In the store left {self.get_product_info(product_name)}')
                    break
            else:
                print('No such product!')


t = Product('Clothes', 'T-Shirt', 10)
t2 = Product('Clothes', 'Hat', 20)
t3 = Product('Clothes', 'Jeans', 100)
t4 = Product('Else', 'Phone', 1000)
t5 = Product('Else', 'Cup', 5)
t6 = Product('Food', 'Coffee', 30)
s = Store()
s.add_product(t, 10)
s.add_product(t2, 30)
s.add_product(t3, 20)
s.add_product(t3, 20)
s.add_product(t3, 10)
s.add_product(t4, 5)
s.add_product(t5, 500)
s.add_product(t6, 25)

print(1)
s.all_products()

print(2)
print(s.get_product_info('Phone'))

print(3)
s.get_product_deep_info('Coffee')

print(4)
s.set_discount('Hat', 50)
s.get_product_deep_info('Hat')

print(5)
s.set_discount('Else', 50, 'p_type')
s.all_products()

print(6)
s.sell_product('Phone', 3)
s.all_products()

print(7)
s.sell_product('Phone', 2)
s.all_products()

print(8)
print(f'You have ${s.get_income()} in total')

