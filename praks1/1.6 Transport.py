inimeste_arv = int(input("Sisesta inimeste arv: "))
kohtade_arv = int(input("Sisesta kohtade arv ühes bussis: "))
bussid = inimeste_arv // kohtade_arv
mahajaanud = inimeste_arv % kohtade_arv
if mahajaanud > 0:
    bussid = bussid + 1
print("Tuleb tellida " + str(bussid) + " bussi.")