def mahlapakkide_arv(õunte_kogus):
    mahlapakkide_arv = float(õunte_kogus) * 0.4 / 3
    return round(mahlapakkide_arv)
    
õunte_kogus = input("Sisestage õunte kogus kilogrammides: ")



print(mahlapakkide_arv(õunte_kogus))