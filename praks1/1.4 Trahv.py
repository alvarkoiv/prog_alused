nimi = input("Sisestage oma nimi: ")
lubatud_kiirus = int(input("Sisestage lubatud kiirus km/h: "))
tegelik_kiirus = int(input("Sisestage tegelik kiirus km/h: "))
oled_yletanud = tegelik_kiirus - lubatud_kiirus
arvutatud_trahv = oled_yletanud * 3
trahv = min(arvutatud_trahv, 190)
print(nimi + ", kiiruse ületamise eest on sinu trahv " + str(trahv) + " eurot.")