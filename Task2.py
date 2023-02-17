num = input("Введите трехзначное число: ")

if len(num) != 3: 
    print("Число должно состоять из 3 цифр!")
else:
    sum = 0
    while int(num) > 0:
        sum += int(num) % 10
        num = int(num) // 10
        
    print("Сумма цифр заданного числа =", sum)