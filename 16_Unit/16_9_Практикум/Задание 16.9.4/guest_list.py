class People:
    def __init__(self, name, surname, address, status):
        self.name = name
        self.surname = surname
        self.address = address
        self.status = status


class Guest(People):
    invite_confirmed = True


print('Заполните базу сотрудников')
amount_employees = int(input('Введите количество сотрудников\n'))

name_employee = []
surname_employee = []
address_employee = []
status_employee = []

for i in range(amount_employees):
    name_employee[i] = input("Введите имя гостя \n")
    surname_employee[i] = input("Введите фамилию гостя \n")
    address_employee[i] = input("Введите место проживания гостя  \n")
    status_employee[i] = input("Введите статус гостя \n")

print(name_employee)