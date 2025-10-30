l = 0
while True:
    print("Если вы хотите посчитать сумму всех ичсел нажмите 0")
    t = int(input("Введите любое число"))
    l = l + t
    if t == 0:
        print(l)
        break
