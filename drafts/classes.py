class N:
    sum1 = 0
    def __init__(self, name):
        self.name = name

    def __setattr__(self, key, value):
        if key == 'name':
            try:
                self.__class__.sum1 -= getattr(self, key)
                self.__class__.sum1 += value
                self.__dict__[key] = value
            except AttributeError:
                self.__class__.sum1 += value
                self.__dict__[key] = value

    def __repr__(self):
        return str(self.name)

class M:
    def __init__(self):
        self.lister = []

    def app(self, j):
        self.lister.append(N(j))


m = M()
for i in range(3):
    m.app(i)

print(m)
print(m.lister)
print(N.sum1)
m.lister[1].name = 10
print(m.lister)
print(N.sum1)
