class ParentExeption(Exceptions):
    pass

class ChildExeption(ParentExeption):
    pass

try:
    raise ChildExeption('message')
except ParentExeption as e:
    print(e)