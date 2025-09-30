'''nu = int(input("введите кол-во элементов списка: "))
sp = []
for n in range(1, nu + 1):
    v = int(input(f"введи {n} число списка: "))
    sp.append(v)
    ss = [n for n in sp if n + 1]
    d = [x for x in sp if x % 2 == 0]
    print("\nСписок чисел: ", sp)
    print("сумма чисел списка: ", ss)
    print("четные числа списка: ", d)'''

'''for i in range(3):
    for j in range(3):
        print(i*j, end=" ")'''

a = input("введите числа: ")


s = 1
while s != 0:
    print(x for x in a if x + 1)
    s += 1
    print("сумма чисел: ", a)