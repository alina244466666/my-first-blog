from pyexpat.errors import messages

message = lambda: print("hello")
message()

def message():
    print("hello")  #функция деф это аналог лямбды

square = lambda n: n * n    #Если лямбда-выражение возвращает какой-то результат, то он указывается после двоеточия
print(square(4))
print(square(5))

def square2(n): return n * n

sum = lambda a, b: a + b
print(sum(4, 5))
print(sum(5, 6))

def do_operation(a, b, operation):  #они могут выполнять только одно выражение
    result = operation(a, b)
    print(f"result = {result}")
do_operation(5, 4, lambda a, b: a + b)
do_operation(5, 4, lambda a, b: a * b)


def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b


operation = select_operation(1)
print(operation(10, 6))  # 16

operation = select_operation(2)
print(operation(10, 6))  # 4

operation = select_operation(3)
print(operation(10, 6))