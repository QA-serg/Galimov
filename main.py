# ПЕРЕМЕННЫЕ И ТИПЫ ДАННЫХ
from dataclasses import replace

#Задача 1 Объявление переменных, именование, типы str и int, print()

my_name = "Sergey"
my_age = 20
print (my_name)
print (my_age)

#Задача 2 Переменные + арифметическое сложение +

a = 15
b = 4
result = a + b
print(result)

#Задача 3 Преобразование int → float

number = 25
print (float(number))

#Задача 4 Переопределение переменной

age = 25
age = 30
print(age)

#Задача 5 Сравнение > и получение True/False
a = 10
b = 7
print(a > b)

#Задача 6 Арифметическое вычитание -, работа с несколькими переменными

price = 100
discount = 20
result = price - discount
print(result)

#Задача 7 Преобразование int → str, определение типа через type()

age = 25
age_text = str(age)
print(age_text, type(age_text))

#Задача 8 Сравнение на равенство ==

a = 10
b = 10
print(a == b)

#Задача 9 Типы данных str, int, float + type()

name = "Sergey"
age = 25
height = 1.80
print(name, type(name), age, type(age), height, type(height))

#Задача 10 Арифметическое умножение *

number = 10
result = number * 3
print(result)

#Задача 11 рифметическое деление /

first_number = 20
second_number = 5
result = first_number / second_number
print(result)

#Задача 12 Сравнение <

a = 8
b = 12
print(a < b)


# СТРОКИ

#Задание 1 - Доступ к символам — получение символа по индексу.

name = "Sergey"
first_char = name[0]
print(first_char)

#Задание 2 - Конкатенация — объединение строк через +.

first_name = "Sergey"
last_name = "Galimov"
full_name = first_name + " " + last_name
print(full_name)

#Задание 3 - Срезы — получение части строки.

text = "Python"
avg_text = text[0:4]
print(avg_text)

#Задание 4 - len() — определение длины строки.

text = "Automation"
lenght = len(text)
print(lenght)

#Задание 5 F-строки — подстановка переменных в строку.

name = "Sergey"
age = 25
massage = f"Меня зовут {name}, мне {age} лет"
print(massage)

#Задание 6 .upper() — перевод строки в верхний регистр.

text = "python automation"
result = text.upper()
print(result)

#Задание 7 Срезы — получение последних символов строки.

text = "Hello Python"
result = text[6:12]
print(result)

#Задание 8 .strip() — удаление пробелов по краям строки.

text = "  Python  "
trimmed_text = text.strip()
print(trimmed_text)

#Задание 9 lower() — нижний регистр

text = "PYTHON"
trimmed_text = text.lower()
print(trimmed_text)

#Задание 10 replace(old, new) — замена части строки

text = "Я изучаю Java"
trimmed_text = text.replace("Java", "Python")
print(trimmed_text)

#Задание 11 split(separator) — разделение строки

text = "Python,Java,SQL"
trimmed_text = text.split(",")
print(trimmed_text)

#Задание 12 startswith() / endswith() — проверка начала и конца строки

text = "Python automation"
start_result = text.startswith("Python")
end_result = text.endswith("automation")
print(start_result, end_result)

# CПИСКИ

#Задание 1 Создание списка + добавление в конец — append()

lang_name = ["Python", "Java", "SQL"]
lang_name.append("Git")
print(lang_name)

#Задание 2 Получение элемента — обращение к элементу по индексу, индексация с 0

numbers = [10, 20, 30, 40, 50]
first_number = numbers[2]
print(first_number)

#Задание 3 Замена элемента — изменение значения по индексу через =

languages = ["Python", "Java", "SQL"]
languages[1] = "JavaScript"
print(languages)

#Задание 4 Добавление в конкретное место — insert(index, value)

languages = ["Python", "Java", "SQL"]
languages.insert(1,"JavaScript")
print(languages)

#Задание 5 Удаление элемента по значению — remove(value); дополнительно различие int и str

numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
print(numbers)

#Задание 6 Срез списка — [начало:конец], правая граница не включается

languages = ["Python", "Java", "SQL", "Git", "Docker"]
slice1 = languages[1:4]
print(slice1)

#Задание 7 Слияние списков — оператор +

languages = ["Python", "Java"]
tools = ["Git", "Docker"]
combined = languages + tools
print(combined)

#Задание 8 Удаление элемента по индексу — del

numbers = [10, 20, 30, 40, 50]
del numbers [4]
print(numbers)

#Задание 9 Полная очистка списка — clear()

languages = ["Python", "Java", "SQL"]
languages.clear()
print(languages)

#Задание 10 Срез списка — получение первых элементов через [начало:конец]

numbers = [10, 20, 30, 40, 50]
clice2 =numbers[0:3]
print(clice2)


# УСЛОВНЫЕ ОПЕРАТОРЫ

#Задание 1 and — объединение двух условий; if/else; сравнение >=; True/False; отступы

age = 25
has_ticket = True
if has_ticket == True and age >= 18:
    print("Yes")
else :
     print("No")

#Задание 2 if → elif → else; проверка диапазона; сравнения <, <=; порядок условий

age = 20
if age < 18:
    print("Child")
elif 17 < age <= 65:
    print("Adult")
else:
     print("Senior")

#Задание 3 Тернарный оператор: значение_if if условие else значение_else; условие >=

age = 20
result = "abult" if age >= 18 else "Child"
print(result)

#Задание 4 or — выполнение логического условия, если подходит хотя бы один вариант; вывод True/False через print()

age = 25
has_ticket = False
print (age >= 18 or has_ticket == True)

#Задание 5 and в условии; проверка диапазона через два отдельных сравнения; if/else

temperature = 25
if temperature > 19 and temperature < 31:
    print("Comfortable")
else:
    print("Uncomfortable")

#Задание 6 Базовый if; выполнение кода только при True; простое сравнение >

number = 10
if number > 0:
    print("Positive")

#Задание 7 if/else; понимание, что else не содержит условия; сравнение >=

number = -5
if number >= 0:
    print("Positive")
else:
    print("Negative")

#Задание 8 not; отрицание булевого значения; вывод результата логического выражения

age = 25
is_student = True
print(not is_student)

#Задание 9 if/elif/else; несколько диапазонов; составные сравнения; последовательность условий

score = 75
if score < 50:
    print("Fail")
elif 50 <= score < 80:
    print("Pass")
else:
    print("Excellent")

#Задание 10 Тернарный оператор; % для проверки чётности; ==; условие в одну строку

number = 7
result = "Even" if number % 2 == 0 else "Odd"
print(result)

#Задание 11 and внутри if; if/else; >=; работа с булевым значением

age = 25
has_permission = True
if age >= 18 and has_permission == True:
    print("Access granted")
else:
    print("Access denied")

#Задание 12 or; логическое выражение без if/else; >=; True/False; правильное использование переменных

age = 16
has_parent = True
print (age >= 18 or has_parent == True)


# СЛОВАРИ

#Задание 1 Создание словаря + доступ к значению по ключу — создание {ключ: значение}, обращение словарь["ключ"].

student = {
    "name": "Alex",
    "age": 20,
    "city": "Moscow"
}
keys = student["age"]
print(keys)

#Задание 2 Обновление элемента — изменение значения существующего ключа через словарь["ключ"] = новое_значение.

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020
}
car["year"] = 2022
print(car)

#Задание 3 Добавление элемента — создание новой пары ключ: значение через словарь["новый_ключ"] = значение.

user = {
    "name": "Sergey",
    "age": 25,
    "city": "Moscow"
}
user["profession"] = "QA"
print(user)

#Задание 4 Удаление элемента через del — удаление пары по ключу.

book = {
    "title": "Python",
    "author": "Ivan",
    "year": 2024
}
del book["year"]
print(book)

#Задание 5 Проверка наличия ключа — оператор in для поиска ключа в словаре.

product = {
    "name": "Laptop",
    "price": 1000,
    "brand": "Lenovo"
}
if "price" in product:
    print(True)
else:
    print(False)

#Задание 6 Получение значений — метод .values().

person = {
    "name": "Alex",
    "age": 30,
    "city": "Berlin"
}
values = person.values()
print(values)

#Задание 7 Получение ключей — метод .keys().

phone = {
    "brand": "Apple",
    "model": "iPhone 15",
    "price": 900
}
keys = phone.keys()
print(keys)

#Задание 8 Проверка наличия значения — .values() + in.

movie = {
    "title": "Inception",
    "year": 2010,
    "genre": "sci-fi"
}
if "sci-fi" in movie.values():
    print(True)
else:
    print(False)

#Задание 9 Получение пар ключ-значение — метод .items().

employee = {
    "name": "Alex",
    "position": "QA",
    "experience": 2
}
print(employee.items())

#Задание 10 Удаление элемента через pop() — удаление по ключу с помощью метода словаря.

user = {
    "name": "Alex",
    "age": 25,
    "city": "Berlin"
}
city = user.pop("city")
print(user)

#Задание 11 Добавление + обновление элементов — новый ключ и изменение существующего значения.

settings = {
    "theme": "dark",
    "language": "ru",
    "notifications": True
}
settings["font_size"] = 14
settings["theme"] = "light"
print(settings)

#Задание 12 Проверка наличия ключа через .keys() + in — закрепление работы с ключами.

account = {
    "login": "alex",
    "email": "alex@mail.com",
    "active": True
}
if "email" in account.keys():
    print(True)
else:
    print(False)



# ЦИКЛЫ

#Задание 1 for + итерация списка

fruits = ["apple", "banana", "orange", "kiwi"]
for fruit in fruits:
    print(fruit)

#Задание 2 for + итерация строки

text = "Python"
for char in text:
    print(char)

#Задание 3 while + итерация списка через индекс

numbers = [10, 20, 30, 40, 50]
index = 0
while index < 5:
    print (numbers[index])
    index += 1

#Задание 4 for + break

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        break
    print(number)

#Задание 5 for + итерация элементов

names = ["Anna", "Bob", "Alex", "Kate"]
for name in names:
    print(name)

#Задание 6 for + range()

for number in range(1,6):
    print(number)

#Задание 7

numbers = [10, 20, 30, 40, 50]
index = 0
while index < 5:
    if numbers[index] == 30:
        break
    print(numbers[index])
    index += 1

#Задание 8

numbers = [2, 4, 6, 8, 10]
for number in range(4,-1,-1):
    print(numbers[number])

#Задание 9

numbers = [10, 20, 30, 40, 50]
index = 0
while index < 3:
    print(numbers[index])
    index += 1


# ФАЙЛЫ

#Задание 1

with open("test.txt", "w") as file:
    file.write("Python automation")

#Задание 2

with open("test.txt", "r") as file:
    print(file.read())

#Задание 3

with open("test.txt", "a") as file:
    file.write("Selenium")

#Задание 4

with open("test.txt", "r") as file:
    readlines = file.readlines()
    for line in readlines:
        print(line)

#Задание 5

with open("test.txt", "r") as file:
    readline = file.readline()
    print(readline)

#Задание 6

with open("test.txt", "w") as file:
    file.write("Hello Python")

#Задание 7

with open("skills.txt", "w") as file:
    file.write("Python\nSelenium\nPytest")

#Задание 8

with open("skills.txt", "r") as file:
    readlines = file.read()
    if "Selenium" in readlines:
        print(True)
    else:
        print(False)

#Задание 9

with open("skills.txt", "a") as file:
    file.write("\nPlaywright")

#Задание 10

with open("skills.txt", "r") as file:
    readlines = file.read()
    print(readlines)

# Функции

#Задание 1

def greeting():
    print("Привет!")
greeting ()

#Задание 2

def show_name(name):
    print(f"Привет, {name}!")
show_name("Сергей")

#Задание 3

def greet(name,age):
    print (f"Привет, {name}, твой возраст {age}!")
greet(name="Сергей",age=25)

#Задание 4

def greet(name="Гость"):
    print(f"Привет, {name}!")
greet(name="Сергей")
greet()

#Задание 5

def add_numbers(a,b):
    return a+b
result = add_numbers(10,5)
print(result)

#Задание 6


def my_decorator(func):
    def wrapper():
        print("начало")
        func()
        print("конец")
    return wrapper
@my_decorator
def hello():
    print("Привет!")
hello ()

#Задание 7

def square(number):
    return number * number
print(square(5))

#Задание 8

def greet(name, message="Привет"):
    return (name  +  message)
user_info = greet("Сергей ")
print(user_info)
user_inform = greet("Сергей",  "Добрый день")
print(user_inform)

# ООП ч.1

#Задание 1

class User:
    role = "QA"
my_user = User()
print(my_user.role)

#Задание 2

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
my_car = Car("BMW", "M5")
print(my_car.brand)
print(my_car.model)

#Задание 3

class Dog:
    def bark(self):
        print("Гав-гав!")
my_dog = Dog()
my_dog.bark()

#Задание 4

class Student:
    school = "IT School"
student1=Student()
student2=Student()
print(student1.school)
print(student2.school)

#Задание 5

class Person:
    def __init__(self, name):
        self.name = name
my_person = Person("Сергей")
print(my_person.name)

#Задание 6

class Phone:
    brand = "Apple"
    def show_brand(self):
        print(self.brand)
phone = Phone()
phone.show_brand()

#Задание 7

class Book:
    def info(self, title):
        print(title)
my_book = Book()
my_book.info("Python для начинающих")

#Задание 8

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
my_employee = Employee("Alex", "QA")
print(my_employee.name)
print(my_employee.position)

#Задание 9

class Cat:
    color = "Белый"
    def meow(self):
        print("Мяу!")
my_cat = Cat()
my_cat.meow()

#Задание 10

class QA:
    profession = "Tester"
    def show_info(self):
        print("Я тестировщик")
qa = QA()
print(qa.profession)
qa.show_info()

#Задание 11

class Tester:
    def __init__(self, name):
        self.name = name
    def say_name(self):
        print(self.name)
my_test = Tester("Сергей")
my_test.say_name()

#Задание 12

class Car:
    def __init__(self, brand):
        self.brand = brand
    def show_brand(self):
        print(self.brand)
my_car = Car("BMW")
my_car.show_brand()

#Задание 13

class User:
    def __init__(self, name):
        self.name = name
    def say_name(self):
        print(self.name)
my_user = User("Сергей")
my_user.say_name()

#Задание 14

class Phone:
    def __init__(self, brand):
        self.brand = brand
        print("Apple")
    def show_brand(self, model):
my_model = Phone.show_brand("iPhone 17")
print(my_model)
Phone.brand()

