n = input("Введите n шоколадки: ")
m = input("Введите m шоколадки: ")
k = input("Введите количества долек шоколадки, чтобы сделать один разлом по прямой: ")

if int(k) % int(n) == 0 or int(k) % int(m) == 0:
    print("От шоколадки", n, "x", m, "МОЖНО отломить", k, "дольки(ек) за один разлом")
else:
    print("От шоколадки", n, "x", m, "НЕЛЬЗЯ отломить", k, "дольки(ек) за один разлом")    