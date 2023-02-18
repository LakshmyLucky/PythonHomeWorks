num = input("Введите трехзначное число: ")
if len(num) != 3: 
    print("Число должно состоять из 3 цифр!")
else:
    sum = 0
    num = int(num)
    while num > 0:
        sum += num % 10
        num = num // 10
    print("Сумма цифр заданного числа =", sum)
