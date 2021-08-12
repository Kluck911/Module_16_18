class Clients:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_data(self):
        return 'Клиент "{0}". Баланс: {1} руб'.format(self.name, self.balance)


client_1 = Clients('Иван Петров', 50)

print(client_1.get_data())
