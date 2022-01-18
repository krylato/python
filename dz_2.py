print('1--------->')
my_int = 8
my_float = 7.23
my_str = 'Всем привет!'
my_bool = 8 < 76
my_list = ['a', '23']
my_tuple = ('b', '32')
my_dict = {'name': 'Антон', 's_name': 'Александров'}

all_list = [my_int, my_float, my_str, my_bool, my_list, my_tuple, my_dict]
for i in all_list:
    print(f'{i} {type(i)}')

print('2--------->')
el_count = int(input('Введите количество элементов списка '))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input('Введите следующее значение списка '))
    i += 1

for elem in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)

print('3--------->')
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
month = int(input('Введите месяц по номеру '))
if month == 1 or month == 12 or month == 2:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])

print('4--------->')
my_str = input('Введите строку: ')
a = my_str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")

print('5--------->')
my_list = [7, 5, 3, 3, 2]
print(f'Рейтинг - {my_list}')
digit = int(input('Введите число (999 для выхода) '))
while digit != 999:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit > my_list[el + 1]:
            my_list.insert(el + 1, digit)
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число "))

print('6--------->')
goods = int(input("Введите количество наименований товара "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
         'ед': my_dict.get('ед')})
print(my_list)
print(my_analys)
