from random import randint
lumivalgekesele = 14

arv = int(input("Mitu pöialpoissi tahab õunu? "))

kord = 1

while kord <= arv:
    õunad = randint(1,2)
    lumivalgekesele -= õunad
    print(õunad)
    kord = kord + 1
print("Lumivalgekesele jäi",lumivalgekesele)