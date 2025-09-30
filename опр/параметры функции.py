'''def say_hello(name):
    print(f"Hello, {name}")

say_hello("Tom")
say_hello("Bob")
say_hello("Alice")

def print_person(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

print_person("Tom", 37)

def say_hello(name="Tom"):
    print(f"Hello, {name}")

say_hello()
say_hello("Bob")

def print_person(name, age = 18):
    print(f"Name: {name} Age: {age}")

print_person("Bob")
print_person("Tom", 37)

def print_person(name = "Tom", age = 18):
    print(f"Name: {name} Age: {age}")

print_person()
print_person("Bob")
print_person("Sam", 37)


def print_person(name, age):
    print(f"Name: {name} Age: {age}")

print_person(age = 22, name = "Tom")


def print_person(name, *, age, company):
    print(f"Name: {name} Age: {age} Company: {company}")

print_person("Bob", age = 41, company = "Microsoft")

def print_person(*, name, age, company):
    print(f"Name: {name} Age: {age} Company: {company}")'''

def print_person(name, /, age, company="Microsoft"):
    print(f"Name: {name}  Age: {age}  Company: {company}")

print_person("Tom", company="JetBrains", age = 24)
print_person("Bob", 41)


def print_person(name, /,  age = 18, *, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")

print_person("Sam", company ="Google")
print_person("Tom", 37, company="JetBrains")
print_person("Bob", company ="Microsoft", age = 42)


def sum(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(f"sum = {result}")

sum(1, 2, 3, 4, 5)
sum(3, 4, 5, 6)