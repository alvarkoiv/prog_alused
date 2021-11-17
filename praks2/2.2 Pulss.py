# sisendid
vanus =  int(input("Sisesta enda vanus: "))
sugu = input("Sisesta oma sugu: ")
treening = int(input("Sisesta treeningu tüüp: "))
# sugu kontroll ja max_pulsi_sageduse arvutamine
if sugu == "M" or sugu == "m":
    max_pulsi_sagedus = 220 - vanus
if sugu == "N" or sugu == "n":
    max_pulsi_sagedus = 206 - vanus * 0.88
# treeningu tüübi kontroll ja min ning max pulsi arvutamine
if treening == 1:
    min_puls = max_pulsi_sagedus * 0.5
    max_puls = max_pulsi_sagedus * 0.7
elif treening == 2:
    min_puls = max_pulsi_sagedus * 0.7
    max_puls = max_pulsi_sagedus * 0.8
elif treening == 3:
    min_puls = max_pulsi_sagedus * 0.8
    max_puls = max_pulsi_sagedus * 0.87
# min ja max pulsi ümmardamine täisarvuks
min_puls = round(min_puls)
max_puls = round(max_puls)
# väljund
print("Pulsisagedus peab olema vahemikus " + str(min_puls) + " ja " + str(max_puls) + " vahel.")