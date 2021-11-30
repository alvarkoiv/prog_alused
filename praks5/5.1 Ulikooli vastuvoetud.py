fail = open("rebased.txt", encoding="UTF-8")

aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))

vastuvõetud = []

for rida in fail:
    
    vastuvõetud.append(int(rida))
    
fail.close()

print(aasta,". aastal oli vastuvõetuid", vastuvõetud[aasta-2011])