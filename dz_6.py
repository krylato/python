print('1--------->')

from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()

print('2--------->')


class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width


class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume


r = MassCount(25, 10000, 125)
print(r.mass())

print('3--------->')


class Worker:
    name = None
    surname = None
    position = None
    profit = None
    bonus = None

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)
        self.__income = None

    def get_full_name(self):
        return self.name + self.surname

    def get_full_profit(self):
        self.__income = {'Оклад': self.profit, 'Премия': self.bonus}
        return self.__income


manager = Position('Иван ', 'Иванов', 'Менеджер', 500, 100)
print(manager.get_full_name(), manager.get_full_profit())

print('4--------->')


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость лимузина {self.name} - {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} высокая для лимузина'
        else:
            return f'Скорость {self.name} нормальная для лимузина'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость служебной машины {self.name} - {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} высокая для служебной машины'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полиции'
        else:
            return f'{self.name} не из полиции'


audi = SportCar(100, 'Красная', 'Audi', False)
lincoln = TownCar(30, 'Белый', 'Lincoln', False)
gaz = WorkCar(70, 'Чёрная', 'Газель', True)
ford = PoliceCar(110, 'Синий', 'Ford', True)
print(gaz.turn_left())
print(f'Когда {lincoln.turn_right()}, тогда {audi.stop()}')
print(f'{gaz.go()} с точной скоростью {gaz.show_speed()}')
print(f'{gaz.name} - {gaz.color}')
print(f'{audi.name} машина полиции? {audi.is_police}')
print(f'{gaz.name} машина полиции? {gaz.is_police}')
print(audi.show_speed())
print(lincoln.show_speed())
print(ford.police())
print(ford.show_speed())

print('5--------->')

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки карандашом'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
