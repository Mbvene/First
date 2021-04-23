seconds = int(input("Enter seconds: "))
hours = seconds // 3600
h = seconds % 3600
minutes = int(h // 60)
m = minutes % 60
seconds = int(m % 60)
# print("{}:{}:{}".format('%02d' % hours, '%02d' % minutes, '%02d' % seconds))
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
# перевод секунд в чч:мм:сс
