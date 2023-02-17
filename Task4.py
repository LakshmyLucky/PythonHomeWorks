# petr = sergy
# katy = 2 * 2 * (petr + sergy)
# count = petr + 4 * petr + petr
# count = 6 * petr
# petr = count / 6
# katy = count / 6 * 4
# sergy = count / 6

count = input("Введите количество журавликов: ")

if int(count) % 6 != 0:
    print("Общее количество журавликов должно быть кратно 6!")
else:
    print("Петя сделал {:0.0f}".format(int(count)/6), "журавликов(ка)")
    print("Катя сделала {:0.0f}".format(int(count)/6 * 4), "журавликов(ка)")
    print("Сережа сделал {:0.0f}".format(int(count)/6), "журавликов(ка)")