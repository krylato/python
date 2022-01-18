print('1--------->')


def my_func(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "Нельзя делить на 0"


print(my_func(int(input('Введите первое число ')), int(input('Введите второе число '))))

print('2--------->')


def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname=input('Имя '), name=input('Фамилия '), year=input('Год рождения '), city=input('Город '),
              email=input('Email '),
              telephone=input('Телефон ')))

print('3--------->')


def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg2 < arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


print(
    f'Результат - {my_func(int(input("Введите первый аргумент ")), int(input("Введите второй аргумент ")), int(input("Введите третий аргумент ")))}')

print('4--------->')


def my_func(x, y):
    return 1 / x ** abs(y)


print(my_func(3, -2))

print('5--------->')


def my_sum():
    sum_res = 0
    ex = False
    while not ex:
        number = input('Введите числа или нажмите Q для выхода ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма чисел {sum_res}')
    print(f'Итоговая сумма чисел {sum_res}')


my_sum()

print('6--------->')


def my_func(a):
    separate_word = a.split(' ')
    total = []
    for i in separate_word:
        string_element = str(i)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        total.append(word)
    return total


print(my_func(input('Введите слова ')))
