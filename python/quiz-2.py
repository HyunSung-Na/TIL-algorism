import string
import csv

a_sum = 0

with open('./resource/a.csv', 'r') as f:
    reader = csv.reader(f)
    for read in reader:
        for index in range(len(read)):
            a_sum += int(read[index])


class Median:

    stack = []

    def __init__(self):
        self.stack = []

    def get_item(self, item):
        self.stack.append(item)

    def clear(self):
        del self.stack

    def show_result(self):
        self.stack.sort()
        mid = 0
        if not len(self.stack) % 2:
            mid_first = len(self.stack) // 2
            mid_second = mid_first - 1
            mid = (self.stack[mid_first] + self.stack[mid_second]) / 2
            return print(mid)
        mid_value = int(len(self.stack) / 2)
        mid = self.stack[mid_value]
        return print(mid)


median = Median()
for x in range(10):
    median.get_item(x)
median.show_result()

median.clear()
for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
    median.get_item(x)
median.show_result()


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' cannot speak.')

    def move(self):
        print(self.name + ' cannot move.')


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def move(self):
        print(self.name + " moves like a jagger.")


class Retriever(Dog):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " is smart enough to speak.")


dog = Dog('Nancy')
dog.speak()
dog.move()

super_dog = Retriever('Michael')
super_dog.speak()
super_dog.move()


class Foo:
    """
    Foo Class
    Author : HyunSung
    Date : 2020.07.18
    """

    data = list(string.ascii_uppercase)
    index = 0

    @classmethod
    def __str__(cls):
        return cls.data[cls.index + 1]

    @classmethod
    def bar(cls):
        print(cls.data[cls.index])

    @classmethod
    def func(cls):
        cls.index += 1
        print(cls.data[cls.index])

    @classmethod
    def Bar(cls):
        return cls()


Foo.bar()
Foo.func()
Foo.Bar().func()
print(Foo())
