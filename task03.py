class First:
    number = 1

    def __init__(self):
        self.total = ''

    def set(self, number):
        self.total = number

    def show(self):
        print(self.total)  # класс в конструктор которого передается одно число с методом show


try:
    1/0
except ZeroDivisionError:
    print('STOP DIVIDING AT 0')
else:
    print('at your table')
finally:
    print("AT DE END OF DA WORLD")  # блок try/except/else/finally с ошибкой деления на 0


def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner


@trace
def heh(x):
    return x  # Декоратор показывающий аргументы функции


class Decor:
    def __init__(self, value):
        self._data = value


@property
def data(self):
    return self._data


d = Decor(3)
d.data  # класс с декоратором


def generator(n):
    a = 1
    while a < n:
        yield a
        a += 1


for q in generator(11):
    print(q)  # генератор от 1 до 10


from collections import namedtuple

coordinates = namedtuple('coordinates', 'a b c')
coordinates = coordinates(7, 6, 2)
print(coordinates)  # точка в трёхмерном пространстве через namedtuple

