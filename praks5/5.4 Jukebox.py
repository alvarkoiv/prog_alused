failinimi = input('Sisestage faili nimi: ')

fail = open(failinimi, encoding = 'UTF-8')

faili_sisu = []

for rida in fail:
    faili_sisu.append(rida.strip())
fail.close()

print('Muusikapalade valik: ')

jk = 1
for muusikapala in faili_sisu:
    print(str(jk) + '. ' + muusikapala)
    jk += 1

'''
for jk in range(0, len(faili_sisu)):
    print(str(jk) + '. ' + faili_sisu[jk])
'''

laulu_jk = int(input('Valige laulu järjekorra number: '))
print('Mängitav muusikapala on ' + faili_sisu[laulu_jk-1])