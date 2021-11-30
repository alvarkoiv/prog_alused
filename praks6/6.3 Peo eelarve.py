def eelarve(x):
    return x*10+55

#def korrutakolmega(x):
#    return round(x*3)

kutsutud = int(input("Mitu inimest on kutsutud? "))
tulevad = int(input("Mitu inimest tuleb? "))


print("Maksimaalne eelarve:",eelarve(kutsutud))
print("Minimaalne eelarve:",eelarve(tulevad))