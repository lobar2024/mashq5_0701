# 9. AMALLAR KALKULYATORI
a = float(input("1-son: "))        # birinchi son
b = float(input("2-son: "))        # ikkinchi son
op = input("Amal (+ - * /): ")     # amal kiritish

if op == "+":                      # qo‘shish
    print(a + b)
elif op == "-":                    # ayirish
    print(a - b)
elif op == "*":                    # ko‘paytirish
    print(a * b)
elif op == "/":                    # bo‘lish
    print(a / b)
else:
    print("Noto‘g‘ri amal")        # xato amal
