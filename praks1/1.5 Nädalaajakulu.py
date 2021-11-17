ekap = int(input("Sisestage EKAPide arv: "))
nadalad = int(input("Sisestage nädalate arv: "))
tunnid = ekap * 26
nadalaajakulu = tunnid / nadalad
print(round(nadalaajakulu))