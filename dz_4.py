print('1--------->')


def sal():
    try:
        time = float(input('Выработка в часах '))
        salary = int(input('Ставка '))
        bonus = int(input('Премия '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Введите число')


sal()

print('2--------->')
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for el in my_list if el > my_list[my_list.index(el) - 1]]
print(new_list)

print('3--------->')
print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

print('4--------->')
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)

print('5--------->')

from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, my_list))

print('6--------->')
from itertools import count

for el in count(int(input('Введите стартовое число '))):
    print(el)

from itertools import cycle

my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    print(el)

print('7--------->')
from itertools import count
from math import factorial


def fibo_gen():
    for el in count(1):
        yield factorial(el)


gen = fibo_gen()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break
