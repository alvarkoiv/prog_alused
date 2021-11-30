from tkinter import *
raam = Tk()
raam.title("Tühi tahvel")
# loome tahvli laiusega 600px
tahvel = Canvas(raam, width=600)


# seest tühi ristkülik (ruut) mustade servadega
tahvel.create_rectangle(0,0,400,200, fill="#00b8e6")

tahvel.create_rectangle(0,100,400,200, fill="white")

# paigutame tahvli raami ja teeme nähtavaks
tahvel.pack()
# siseneme põhitsüklisse
raam.mainloop()
