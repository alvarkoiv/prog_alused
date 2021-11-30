def kuu_nimi(jk):
    kuu_nimi = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    return kuu_nimi[jk-1]

def kuupäev_sõnena(kuupaev):
    kuupaev_nimekiri = kuupaev.split(".")
    kuu_nr = int(kuupaev_nimekiri[1])
    kuu = kuu_nimi(kuu_nr)
    päev = kuupaev_nimekiri[0]
    aasta = kuupaev_nimekiri[2]
    lause = päev + ". "  + kuu + " " + aasta + ". a"
    return lause
    
   
    
kuupäev = input("Sisesta kuupäev kujul DD.MM.YYYY: ")
print(kuupäev_sõnena(kuupäev))