while True:
    y = int(input("введите первое число: "))
    o = input("выбирете действие (/; *; +; -; %; //):")
    u = int(input("выбирите второе число: "))
    if o == '/' and u == 0:
        print("на ноль делить нельзы")
    if o == '/' and u > 0:
        print(y/u)
    if o == '*':
        print(y*u)
    elif o == '+':
        print(y+u)
    elif o == '-':
        print(y-u)
    elif o == '%':
        print(y%u)
    elif o == '//':
        print(y//u)
    else:
        print("что-то пошло не так")
    print("хотите снова использовать калькулятр\n1)да\n2)нет")
    i = input("введите 1 если хотите, 2 если нет: ")
    if i == "1":
        continue
    else:
        print("вы выбрали нет")
        break
