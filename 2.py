n=int(input("Введите число n: "))
if n < 0:
    print("Факториал не может быть отрицательным")
else:
    f = 1
    for i in range(1, n + 1):
        f*=i
print(f"Факториал числа {n} равен {f}")
