a = int(input("Введи целое число"))
s = 0
a = abs(a)
while a > 0 :
s += a % 10
a //= 10
print(f"Сумма цифр: {s}")
