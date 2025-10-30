num = input("Ведите число")
mx = 10
for i in range(len(num)):
    if int(num[i]) < mx:
           mx = int(num[i])
print(f"наименьшее число: {mx}")
