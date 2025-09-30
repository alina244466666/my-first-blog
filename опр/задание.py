'''name = input("введите ваше имя")
print("Привет," name)'''

'''a = input("Ведите первое число")
b = input("Введите второе число")

print(a, b)


print("Операции с числами")
print("Сложение", (float(a) + float(b)))
print("Вычитание", (float(a) - float(b)))
print("Умножение", (float(a) * float(b)))
print("Деление", (float(a) / float(b)))'''

p = float(input("Начальная сумма вклада: "))
r = float(input("Процент по вкладу: "))
t = float(input("Количество лет: "))
a = (p * r * t) /100
print("Начисленные проценты: ", a)


a = float(input("Введите температуру в градусах Цельсия: "))
f = (9/5)*a + 32
print(a, " градусов Цельсия равны ", f,  " градусам Фаренгейта")
