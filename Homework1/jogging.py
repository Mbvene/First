distance = float(input("Введите количество километров в первый день: "))
last_distance = float(input("Введите количество километров в последний день: "))
day = 1
while last_distance > distance:
    distance = distance + (distance / 10)
    day = day + 1
print(f"На {day}-й день спортсмен достиг результата — не менее {int(last_distance)} км.")

