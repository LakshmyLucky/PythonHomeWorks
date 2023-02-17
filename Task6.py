num = input("Введите номер билета: ")

if len(num) != 6: 
    print("Номер должен содержать 6 цифр!")
else:
    i = sumR = sumL = 0
    
    while i < 6:
        if i < 3:
            sumR += int(num) % 10
        else:
            sumL += int(num) % 10
        num = int(num) // 10
        i += 1
        
    if sumR == sumL:
        print("Приятного аппетита!")
    else:
        print("Когда-нибудь и тебе повезет!")