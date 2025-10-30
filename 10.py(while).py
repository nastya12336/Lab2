a = 1000
e = 0.05
m = a * 2
c = a
y = 0
while c < m:
    c *= ( 1 + e )
    y += 1
print(f"Сумма удвоится через {y} лет.")
print(f"Итоговая сумма :{round(c)} руб")
