eggs = 1
cost = 3
print(f"Стоимость омлета из 1 яйца - {cost} руб.")
eggs = int(input("Введите количество яиц для омлета: "))
bill = eggs * cost
print(f"Стоимость составит {bill} руб.")
wishes = input("Укажите пожелания к заказу: ")
print(f"Ваш заказ:\nОмлет из {eggs} яиц\nПожелания:'{wishes}'\nСпасибо!")

