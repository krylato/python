print('1--------->')
name = 'Anton'
second_name = 'Aleksanrov'
age = 31
print(name)
print(second_name)
print(age)
user_name = input('Ваше имя?: ')
user_sec_name = input('Ваша фамилия?: ')
print('Привет,', user_name, user_sec_name)

print('2--------->')
sec = int(input('Введите время в секундах: '))
hour = sec / 3600
minut = sec / 60
time_str = 'Что составляяет {} часов или {} минут или {} секунд'.format(hour, minut, sec)
print(time_str)

print('3--------->')
n = input('Введите число: ')
nn = int(n + n)
nnn = int(n + n + n)
n = int(n)
print(n + nn + nnn)

print('4--------->')
a = int(input('Введите число '))
m = a % 10
a = a // 10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a // 10
print(m)

print('5--------->')
cost = int(input('Укажите издержки фирмы '))
revenue = int(input('Укажите выручку фирмы '))
if revenue < cost:
    print('Фирма имеет убыток')
else:
    print('Фирма имеет прибыль')
    profit = revenue - cost
    print('Рентабельность выручки - ', profit / revenue * 100)
    people = int(input('Укажите численность сотрудников '))
    print('Прибыль фирмы в расчете на одного сотрудника - ', profit / people)
