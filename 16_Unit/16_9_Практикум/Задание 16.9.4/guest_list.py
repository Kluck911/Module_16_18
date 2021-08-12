class Volunteer:
    def __init__(self, name='', surname='', address='', status=''):
        self.name = name
        self.surname = surname
        self.address = address
        self.status = status

    def get_description(self):
        return '{0} {1}, {2}, статус: {3}'.format(self.name, self.surname, self.address, self.status)


class Invited(Volunteer):
    invite_confirmed = True


def is_guest(volon):
    print(volon.get_description())
    verification = input('Данный волонтер приглашен на корпорат? да/нет\n')
    verification = verification.lower()
    if verification == 'да':
        return True
    else:
        return False


def make_list_guests(volunteer):
    if is_guest(volunteer):
        volunteer = Invited(volunteer)
        list_guests.append(volunteer.get_description())
    return volunteer


# База волонтеров проекта


volunteer_1 = Volunteer("Антон", "Антонов", "Минск", "укладчик-наладчик")
volunteer_2 = Volunteer("Степан", "Степанов", "Гродно", "сегодня не пьет")
volunteer_3 = Volunteer("Кузьма", "Кузьмин", "Брест", "леcник-международник")
volunteer_4 = Volunteer("Энтони", "Антонов", "Гомель", "слесарь VI- го разряда, в руках ключ на 32")
volunteer_5 = Volunteer("Святослав", "Аганесян", "Могилев", "прожект менеджер по перетаскиванию кнопки")


list_guests = []

volunteer_1 = make_list_guests(volunteer_1)
volunteer_2 = make_list_guests(volunteer_2)
volunteer_3 = make_list_guests(volunteer_3)
volunteer_4 = make_list_guests(volunteer_4)
volunteer_5 = make_list_guests(volunteer_5)

print(volunteer_1.get_description())