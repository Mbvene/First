proceeds = float(input("Введите значение выручки: "))
costs = float(input("Введите сумму издержек: "))
if proceeds < costs:
    print("Предприятие убыточно")
elif proceeds == costs:
    print("Нулевая прибыль")
else:
    print("Предприятие прибыльно")
    profit = proceeds - costs
    efficiency = profit / proceeds
    print(f"Рентабильность выручки: {efficiency:.2f}")
    staff = int(input("Введите численность сотрудников: "))
    staff_profit = profit / staff
    print(f"Прибыль на сотрудника: {staff_profit:.2f}")