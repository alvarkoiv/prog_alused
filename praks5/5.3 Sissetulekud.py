fail = open("konto.txt", encoding = 'UTF-8')

konto = []

for rida in fail:
    konto.append(float(rida))
fail.close()

for tehing in konto:
    if(tehing >= 0):
        print(tehing)