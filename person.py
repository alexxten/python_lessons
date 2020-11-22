class Person:
    def __init__(self, name: str):
        self.name = name
        self.age = 1009

    def go(self):
        print(f'Я {self.name} и иду')


p = Person(name='Илья')
a = Person(name='Лена')
print(p.go())
print(a.go())

# Создать проект в pycharm и установить виртуальную среду(не забыть активировать)
# Создать класс танк