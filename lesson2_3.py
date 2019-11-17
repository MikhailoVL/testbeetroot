from abc import ABC, abstractmethod
# Студент, Преподаватель Персона, Зав. кафедрой.


class Vehicle:

    def __init__(self, name):
        self.name = name


class Person:

    def __init__(self, last_name, name, date_berth):
        self.last_name = last_name
        self.name = name
        self.date_berth = date_berth

#    def __str__(self):
#        return f"Меня зовут {self.last_name} {self.name} мне испольнилось {self.date_berth}"

    def __repr__(self):
        return self.last_name, self.name, self.date_berth


class Student(Person):

    def __init__(self, last_name, name, date_berth):
        super().__init__(last_name, name, date_berth)

st = Student("vasil", "hyi", "28.07.15")
print(st)

class Teacher(Person):

    def __init__(self, last_name, name, date_berth):
        super().__init__(last_name, name, date_berth)


class HeadOfDepartment(Teacher):

    def __init__(self, last_name, name, date_berth):
        super().__init__(last_name, name, date_berth)


class Car(Vehicle):

    def __init__(self, name):
        super().__init__(name)


class Train(Vehicle):

    def __init__(self, name):
        super().__init__(name)


class Motorcycle(Vehicle):

    def __init__(self, name):
        super().__init__(name)


 # Республика, Монархия, Королевство, государство.
class State:

    def __init__(self, name, kind_of_management):
        self.name = name
        self.kind_of_management = kind_of_management


class Republic(State):

    def __init__(self, name, kind_of_management):
        super().__init__(name, kind_of_management)


class Monarchy(State):

    def __init__(self, name, kind_of_management):
        super().__init__(name, kind_of_management)


class Kingdom(Monarchy):

    def __init__(self, name, kind_of_management):
        super().__init__(name, kind_of_management)

# Деталь, Механизм, Изделие.


class Product:

    def __init__(self, name):
        self.name = name

class Detail(Product):

    def __init__(self, name):
        super().__init__(name)

class Mechanism(Detail):

    def __init__(self, name):
        super().__init__(name)

# Magazine, Book, Printed Edition, Textbook
# Журнал, Книга, Печатное издание, Учебник
class PrintedEdition:

    def __init__(self, name):
        self.name = name


class Book(PrintedEdition):

    def __init__(self, name):
        super().__init__(name)


class Textbook(Book):

    def __init__(self, name):
        super().__init__(name)


class Magazine(Book):

    def __init__(self, name):
        super().__init__(name)

# Тест, Экзамен, Выпускной экзамен, Испытания.
# Test, Exam, Final Exam, Testing.


class Testing:

    def __init__(self, sub):
        self.sub = sub

class Exam(Testing):

    def __init__(self, sub):
        super().__init__(sub)

class FinalExam(Exam):

    def __init__(self, sub):
        super().__init__(sub)


class Test(Exam):

    def __init__(self, sub):
        super().__init__(sub)

#Employee, Person, Worker, Engineer
# Служащий, Персона, Рабочий, Инженер


class Worker(Person):
    def __init__(self, last_name, name, date_berth):
        super().__init__(last_name, name, date_berth)


class Engineer(Worker):

    def __init__(self, last_name, name, date_berth):
        super().__init__(last_name, name, date_berth)


class Employee(Worker):

    def __init__(self, last_name, name, date_berth):
        super().__init__(last_name, name, date_berth)

# Toy, Product (Food), Product, MilkProduct. (multiple legacy)
#Игрушка, Продукт(Еда), товар, Молочный продукт. (множественное наслед)


class Product:

    def __init__(self, name):
        self.name = name


class ProductFood:

    def __init__(self, food=True):
        self.food = food


class MilkProduct(Product, ProductFood):

    def __init__(self, name, food):
        super(MilkProduct, self).__init__(name)
        ProductFood.__init__(self, food)

milk = MilkProduct('jogurt', False)
print(milk.name)
print(milk.food)

class Toy(Product):

    def __init__(self, name):
        super().__init__(name)


# Объявить абстрактный класс Судно с абстрактными методами. Создать иерархию классов: Корабль, Пароход, Катер, Парусник.
class Vessel(ABC):

    def __init__(self, name, length, carrying, team_people):
        self.name = name
        self.length = length
        self.carrying = carrying
        self.team_people = team_people

    def i_am_boot(self):
        return "Я мог бы быть крейсером"

    @abstractmethod
    def up_swim(self):
        raise NotImplementedError

    @abstractmethod
    def carrying_capacity(self):
        raise NotImplementedError


# Корабль, Пароход, Катер, Парусник.
# Classes: Ship, Steamboat, Boat, Sailboat.
class Ship(Vessel):

    def __init__(self, name, length, carrying, team_people, speed):
        super().__init__(name, length, carrying, team_people)
        self.speed = speed

    def up_swim(self):
        return f"my speed {self.speed}"

    def carrying_capacity(self):
        return f"my carrying capacity {self.carrying}"


class Steamboat(Vessel):

    def __init__(self, name, length, carrying, team_people, speed):
        super().__init__(name, length, carrying, team_people)
        self.speed = speed

    def up_swim(self):
        return f"my speed {self.speed}"

    def carrying_capacity(self):
        return f"my carrying capacity {self.carrying}"


class Boat(Ship):

    def __init__(self, name, length, carrying, team_people, speed):
        super().__init__(name, length, carrying, team_people, speed)


class Sailboat(Ship):

    def __init__(self, name, length, carrying, team_people, speed, count_sails):
        super().__init__(name, length, carrying, team_people, speed)
        self.count_sails = count_sails


# Создать абстрактный класс Device, создать от него два класса наследника Scanner, Printer.
# Создать класс Copier наследуясь от классов Scanner, Printer.

class Device(ABC):

    def __init__(self, name, power_consumption):
        self.name = name
        self.power_consumption = power_consumption

    def what(self):
        return "I need people"

    @abstractmethod
    def what_i_can(self):
        raise NotImplementedError

    @abstractmethod
    def energy(self):
        raise NotImplementedError


class Scanner(Device):

    def __init__(self, name, power_consumption, count_scan=0):
        super().__init__(name, power_consumption)
        self.count_scan = count_scan

    def what_i_can(self):
        return "I can copy document from paper"

    def energy(self):
        return f"I work and it enrgy {self.power_consumption}"


class Printer(Device):

    def __init__(self, name, power_consumption, count_copy=0):
        super().__init__(name, power_consumption)
        self.count_copy = count_copy

    def what_i_can(self):
        return "I can write document from pc to paper"

    def energy(self):
        return f"I work and it enrgy {self.power_consumption}"


class Copier(Scanner, Printer):

    def __init__(self, name, power_consumption, count_copy):
        super().__init__(name, power_consumption)
        self.count_copy = count_copy

