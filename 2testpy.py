ticket=int(input("Введите количество человек:"))
preis = 0
for i in range(ticket):
     age = int(input("Введите ваш возраст:"))
     if 0 >= age < 18:
         preis = preis+0
     elif 18 <= age < 24:
           preis = preis+990
     elif 25 <= age:
         preis = preis+1390
if ticket > 3:
    preis = preis * 0.9
print("С Вас %d рублей!" %(preis))