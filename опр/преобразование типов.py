from pyexpat.errors import messages

a = 2   #int (но преобразовался к float)
b = 2.5    #float
c = a + b
print(c)

a = "2"
b = 3
c = int(a) + b
print(c)

a = int(15)
b = int(3.7)
c = int("4")
e = int(False)
f = int(True)
#b = int("a1c")
#c = int("4.7")    # Ошибки

a = "2.7"
b = 3
c = float(a) + b
print(c)

a = float(15)
b = float(3.7)
c = float("4.7")
d = float("5")
e = float(False)
f = float(True)
#d = float("abc")  # Ошибка

a = str(False)
b = str(True)
c = str(5)
d = str(5.7)

age = 22
message = "Age: " + str(age)
print(message)