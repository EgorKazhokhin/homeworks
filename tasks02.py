
a = [1, 2, 'TRI']   # список
a[1]  # элемент из списка с индексом 1

b = {'KLUCH': 'go', 'KLUCH2': 'stop', 'KLUCH3': 'continue'}   # словарь ключ-значение

c1 = {5, 6, 7}
c2 = {7, 8, 9}   # два множества

d = 8
e = 7
if d == 1 or e == 2:
    print('raz')
elif e == 3:
    print('dva')
elif d == 4:
    print('tri')
else:
    print('chetire')  # блок с if, elif и else

f = 100
while f > 5:
    f //= 10  # блок с while

for g in ['VPERED', 'NAZAD', 'STOP']:
    print(g)  # список из 3 элементов и их распечатка через for

for h in range(6):
    print(h)  # распечатка чисел от 0 до 5

i = 'TEST'
if 'E' in i:
    print('pass')  # поиск в строке TEST символа E, при нахождении распечатка "pass"

j = input('enter something here:')
print('you have entered:', j, 'so nice of {}'.format('you'))
# запрос данных у пользователя и вывод их через форматированную строку

with open('Text.txt') as k:
    print(k.read()) # Распечатка содержимого файла


def fun1(arg1, arg2):
    print(arg1 + arg2)

    fun1(1, 2)  # функция с двумя аргументами, возвращающая сумму


def fun2(**kwargs):
    print(kwargs)

    fun2(parameter=1, parameter2=2, parameter3=3)  # функция с любым количеством параметров
