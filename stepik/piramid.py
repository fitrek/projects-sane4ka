import math

x_a = float(input("Введите координату X точки A "))
y_a = float(input("Введите координату Y точки A "))


x_b = float(input("Введите координату X точки B "))
y_b = float(input("Введите координату Y точки B "))

a = (x_a - x_b)**2

b = (y_a - y_b)**2

c = round(math.sqrt(a+b), 3)


 
print(a)
print(b)
print(c)