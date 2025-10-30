n = int(input("Введите целое число: "))
g =  -1 if n < 0 else 1
n = abs(n)
y = 0
while n > 0 :
    y = y * 10 + n % 10
    n //= 10
    y *= g
    print(f"ЧИсло в обратном порядке:{y}")
