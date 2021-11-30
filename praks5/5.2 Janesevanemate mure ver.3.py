ringide_arv = int(input("Sisesta ringide arv: "))
porgandid = 0

for ring in range(1, ringide_arv + 1, 1):
    if(ring % 2 == 0):
        porgandid += ring
    ring += 1
print("Porgandite koguarv on " + str(porgandid))