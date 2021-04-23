number = int(input("Введите целое положительное число: "))
box = 0
while number > 10:
    a = number % 10
    number = number // 10
    if a >= box:
        box = a
print(box)

