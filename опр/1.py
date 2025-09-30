from ast import Param

from pyexpat.errors import messages
#циклы
'''
number = 1

while number < 10:
    print(f"number = {number}")
    number += 1
print("Работа программы завершена")

number = 1

while number < 7:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}. Работа цикла завершена")
print("Работа программы завершена")

number = 12

while number < 7:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}. Работа цикла завершена")
print("Работа программы завершена")

message = "Alina"

for c in message:
    print(c)


for n in range(5, 18):
    print(n, end=", ")


for n in range(0, 15, 3):
    print(n, end=", ")
'''

message = "Hello"
for c in message:
    print(c)
else:
    print(f"Последний символ: {c}. Цикл завершен");
print("Работа рограммы завершена")

i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i +=1

for c1 in "ab":
    for c2 in "ba":
        print(f"{c1}{c2}")

'''
number = 0
while number < 5:
    number += 1
    if number == 3 :
        break
    print(f"number = {number}")
'''

number = 0
while number < 5:
    number += 1
    if number == 3 :
        continue
    print(f"number = {number}")