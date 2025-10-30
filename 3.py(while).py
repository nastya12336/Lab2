a = 12345
while True:
    j = int(input("Введи пароль"))
    if j == a:
        print("Вы ввели правильный пароль")
        break
    elif j != a:
        print("Пароль не верный , попробуйте снова")
        
