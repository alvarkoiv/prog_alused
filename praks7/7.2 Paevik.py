from datetime import datetime

sõne1 = input("Sisesta sissekande tekst: ")

fail = open("paevik.txt", "a", encoding="UTF-8")
kuupäev_kellaaeg = datetime.today()
fail.write(str(kuupäev_kellaaeg) + "\n")
fail.write(sõne1 + "\n")
fail.close()