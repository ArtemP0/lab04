import math as m
def calculate(a, b, t):
    R = 8.81 * t * a + m.asin(m.cos(a + b)) + m.sqrt(t + b)
    return R
a = float(input("Введите значение a: ")) 
b = float(input("Введите значение b: ")) 
t = float(input("Введите значение t: ")) 
result = calculate(a, b, t)
print("Результат: " + str(result))
