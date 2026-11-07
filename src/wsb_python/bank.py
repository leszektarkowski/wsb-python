class BankAccount:
    def __init__(self, name, vault=0):
        self.__name = name
        self.__vault = vault
        print(f"Constructor for: {name}, {vault}")

    def info(self):
        print(f"Info: {self.__name}, {self.__vault}")

    def deposit(self, value):
        self.__vault += value

    def withdraw(self, value):
        if self.__vault - value > 0:
            self.__vault -= value
        else:
            raise ValueError("not enough money")
        return value


c = {'name': "Cecylia", 'vault': 10000}
d = {'name': "Daniel", 'vault': 10000}
e = {'name': "Edward"}

a = BankAccount("Adam")
b = BankAccount("Beata", 1000)

clients = [a, b, BankAccount("Celina", 500)]
d_clients = [c, d, e]


for c in d_clients:
    print(c["name"])
    #c.method()
    # print(c["vault"] )

print("------")

for c in clients:
    c.info()
    # print(c.name)

a.deposit(123)
# print(a.vault)
# a.__vault = 100
clients[2].deposit(987)

for c in clients:
    try:
        c.withdraw(1000)
    except ValueError:
        print(f"not enough money")
    c.info()

class A:
    pass

simple = A()
## print(simple.something)
simple.something = 100
print(simple.something)



