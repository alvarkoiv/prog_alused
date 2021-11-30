def banner(lause):
    return lause.upper()

kordamise_arv = int(input("Mitu korda soovite reklaamlauset kuvada? "))
lause = input("Sisesta reklaamlause: ")


kord = 1
while(kord <= kordamise_arv):
    print(banner(lause))
    kord = kord + 1