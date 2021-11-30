def eelarve(x):
    return x*10+55

tuleb = 0
kutsutud = 0

failinimi = input("Sisesta failinimi: ")

fail = open(failinimi, encoding="UTF-8")
for rida in fail:
    kutsutud += 1
    if(rida[0] == "+"):
        tuleb += 1





print("Kutsutud on", kutsutud ,"inimest")
print(tuleb, "inimest tuleb")

print("Maksimaalne eelarve:",eelarve(kutsutud))
print("Minimaalne eelarve:",eelarve(tuleb))

fail.close