#from audioop import reverse

s = int(input("введите кол-во элементов списка: "))
sp=[]
for n in range(1, s + 1):
    nu = int(input(f"введи {n} число в список: "))
    sp.append(nu)
    total = sum(sp)
    sr = total/len(sp) if sp else 0
    otr = sum(1 for x in sp if x < 0)

print(sp)
print("сумма чисел равна: ", total)
print("среднее арифметическое равно: ", sr)
print("макс. число: ", max(sp))
print("мин. число: ", min(sp))
print("кол-во отрицательных чисел: ", otr)
print("список в обратном порядке: ", list(reversed(sp)))
print("только четные числа: ", )

def condition(number): return number % 2 == 0
result = filter(condition, sp)
for i in result: print(i, end=" ")

