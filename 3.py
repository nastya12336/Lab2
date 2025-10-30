num = int(input("Ведите число для таблицы умножения"))
if num < 1 or num > 10:
    print("Введите число от 1 до 10")
else:
    for i in range(1,11):
        res = num * i
        print(f"{res} = {num} * {i}")
           
    
