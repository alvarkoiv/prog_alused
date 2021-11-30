failinimi = input("Sisesta failinimi: ")

fail = open(failinimi, encoding="UTF-8")

for rida in fail:
    rida = rida.upper().replace("\n", "")
    
    rida = rida.replace("Ä", "AE")
    
    rida = rida.replace("Õ", "OE")
    
    rida = rida.replace("Ö", "OE")
    
    rida = rida.replace("Ü", "UE")
	
    print(rida)

fail.close