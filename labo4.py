import math
x = float(input("Введите значение x: "))
chislitel = math.copysign(abs(x + x**2 + x**3 + math.sin(x)) ** (1/3), x + x**2 + x**3 + math.sin(x))
znamenatel = 2.27 * math.log(abs(x + 100))
f = chislitel / znamenatel
print("f(x) = " + str(f))