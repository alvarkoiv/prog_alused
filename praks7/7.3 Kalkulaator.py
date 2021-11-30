from easygui import *

arv1 = integerbox("Sisesta esimene täisarv lõigus 1-10",lowerbound=0, upperbound=99)
arv2 = integerbox("Sisesta teine täisarv lõigus 1-10",lowerbound=0, upperbound=99)

def liitmine(arv1, arv2):
    return arv1 + arv2

def lahutamine(arv1, arv2):
    return arv1 - arv2
    
def korrutamine(arv1, arv2):
    return arv1 * arv2

jk = ["liitmine", "lahutamine", "korrutamine"]

valik = buttonbox("Valige tehe: ", choices = jk)

if valik == "liitmine":
    msgbox(str(arv1) + " + " + str(arv2) + " = " + str(liitmine(arv1, arv2)))

elif valik == "lahutamine":
    msgbox(str(arv1) + " - " + str(arv2) + " = " + str(lahutamine(arv1, arv2)))

elif valik == "korrutamine":
    msgbox(str(arv1) + " * " + str(arv2) + " = " + str(korrutamine(arv1, arv2)))