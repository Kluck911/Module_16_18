"""
Команда проекта «Дом питомца» планирует большой корпоратив для своих волонтеров.
Вам необходимо написать программу, которая позволяла бы составлять список нескольких гостей.
Решите задачу с помощью метода конструктора и примените один из принципов наследования.

При выводе в консоль вы должны получить:  “Иван Петров, г.Москва, статус "Наставник"
-----------------------------------------------------------------------------------------

Решение не совсем удовлетворяет условию. В программе уже есть небольшой список волонтеров
и пользователю предлагается выбрать, кто из них идет на корпоратив.
Мне показалось, что так будет интереснее в рамках учебного задания :)
"""


class People:
    def __init__(self, name='', surname='', address='', status=''):
        self.name = name
        self.surname = surname
        self.address = address
        self.status = status

    def get_description(self):
        return '{0} {1}, {2}, статус: {3}'.format(self.name, self.surname, self.address, self.status)


class Volunteer(People):
    like_animals = True
    like_meat = False
    like_nature = True


# спрашиваем у пользователя пригласить ли волонтера
def is_guest(volon):
    print(volon.get_description())
    verification = input('Пригласите его на корпоратив? да/нет\n')
    if verification.lower() == 'да':
        return True


# если волонтер приглашен, то добавляем в список list_guests
def make_list_guests(volunteer):
    if is_guest(volunteer):
        list_guests.append(volunteer.get_description())


# База волонтеров проекта
volunteer_1 = Volunteer("Антон", "Антонов", "Минск", "укладчик-наладчик")
volunteer_2 = Volunteer("Степан", "Степанов", "Гродно", "сегодня не пьет")
volunteer_3 = Volunteer("Кузьма", "Кузьмин", "Брест", "леcник-международник")
volunteer_4 = Volunteer("Энтони", "Антонов", "Гомель", "слесарь VI- го разряда, в руках ключ на 32")
volunteer_5 = Volunteer("Святослав", "Джугашвилли", "Могилев", "прожект менеджер по перетаскиванию кнопки")


list_guests = []

make_list_guests(volunteer_1)
make_list_guests(volunteer_2)
make_list_guests(volunteer_3)
make_list_guests(volunteer_4)
make_list_guests(volunteer_5)

# если список существует, то выводим его
if list_guests:
    print(f'На корпоративе будут присутствовать следующие волонтеры:')
    print('\n'.join(list_guests))
else:
    print(f'На корпоратив никто не приглашен :(')
