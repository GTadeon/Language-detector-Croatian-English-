__author__ = 'GTadeon'

from Tkinter import *
from tkFileDialog import*
from funkcije import *
import tkMessageBox

def UcitajDatotekuIPrepoznajJezik():
    #datoteka ciji jezik ne znam jos uvijek:
    datoteka=askopenfilename()
    SekvencaKojuIspitujemo=open(datoteka).read().decode("utf8").lower()

    #training set za ovaj program:
    hr=open("hr.txt").read().decode("utf8").lower()
    en=open("en.txt").read().decode("utf8").lower()

    #na razini znakovi -> jer su hr i en udaljeni jezici!
    fd_hr=frek_distr(opojavnici(hr))
    fd_en=frek_distr(opojavnici(en))

    model_rijeci={"hrvatski":fd_hr, "engleski":fd_en}
    model_rijeci=zagladi(model_rijeci)

    odgovor= klasificiraj(opojavnici(SekvencaKojuIspitujemo),model_rijeci)
    lejbl.configure(text="jezik te datoteke jest: "+odgovor)
    return



def info():
    tkMessageBox.showinfo("O autoru programa i programu", "Program sam napisao koristeci algoritme machine learninga i statisticke obrade teksta (frekvencijska distribucija, opojavnicivanje teksta koristeci regularne izraze, itd). Program radi na principu dvoklasnog modela,odnsono moze prepozanti samo ili engleski ili hrvatski tekst, s obzirom da sam na takvim jezicnim korpusima <<trenirao>> sustav. Moji kontak podaci: ivgroben@ffzg.hr,  github: https://github.com/GTadeon), Ivan Grobenski")
    return

root =Tk()
root.geometry("500x200+200+200")
root.title("Prepoznavatelj jezika ")


#izbornik:
menubar = Menu(root)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="O programu i autoru programa", command=info)
menubar.add_cascade(label="Info", menu=helpmenu)

# display the menu
root.config(menu=menubar)

Btn= Button(root, text="odaberi tekstnu datoteku ",command=UcitajDatotekuIPrepoznajJezik).grid(row=1,column=2)
lejbl=Label(root,text="jezik te datoteke jest: ")
lejbl.grid(row=2,column=2)




root.mainloop()