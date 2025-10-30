n = int(input("Введите простое число"))
for i in range(2,n):
    if n % i == 0:
        print("число не простое")
        break
else:
        print("Число простое")


