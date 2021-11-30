from random import randint


arv = int(input("Sisesta täisarv: "))

kord= 1

while kord <= arv:
    suvaline_täisarv = randint(1,6)
    print(suvaline_täisarv)
    kord = kord + 1