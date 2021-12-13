from Logic.functionalitate import ordonareDupaSuma ,sumaPerApartament
from Domain.cheltuiala import toString
from Logic.Crud import adaugaCheltuiala, stergeCheltuiala, modificaCheltuiala
from Utils.general import undo, redo


def printMenu():
    print("1. Adaugare cheltuiala")
    print("2. Stergere cheltuiala")
    print("3. Modificare cheltuiala")
    print("4. Ordonarea cheltuielilor descrescător după sumă.")
    print("5. Afișarea sumelor lunare pentru fiecare apartament.")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare cheltuieli")
    print("x. Iesire")


def uiAdaugaCheltuiala(lista):
    try :

        id = input("Dati id-ul: ")
        nr_apartament = int(input("Dati nr_apartamentului: "))
        suma = float(input('Dati suma: '))
        data =int(input("Dati data: "))
        tip = input("Dati tipul: ")
        if tip!="intretinere"and tip!="canal" and tip!="alte cheltuieli":
            raise(ValueError)
        return adaugaCheltuiala(id, nr_apartament, suma, data, tip, lista)
    except ValueError:
        print("Date gresite")


def uiStergeCheltuiala(lista):
    id = input("Dati id-ul cheltuielii de sters: ")
    return stergeCheltuiala(id, lista)


def uiModificaCheltuiala(lista):
    try:

        id = input("Dati id-ul cheltuielii de modificat: ")
        nr_apartament = int(input("Dati noul nr de apartament: "))
        suma = float(input("Dati noua suma: "))
        data = int(input("Dati data:"))
        tip = input("Dati noul tip: ")
        return modificaCheltuiala(id, nr_apartament, suma, data, tip, lista)
    except ValueError:
        print("Date gresite")

def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))

def uiOrdonareDupaSuma(lista):
    showAll(ordonareDupaSuma(lista))


def uiSumaPerApartament(lista):
    rezultat = sumaPerApartament(lista)
    for nr_apartament in rezultat:
        print("Apartamentul {} are suma preturilor {}".format(nr_apartament, rezultat[nr_apartament]))

def runMenu(lista):
    undo_lista=[]
    redo_lista = []
    lista=[]
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista1 = uiAdaugaCheltuiala(lista)
            if lista1 :
                lista =lista1
                redo_lista = [lista]
                undo_lista.append([el for el in lista])
        elif optiune == "2":
            lista = uiStergeCheltuiala(lista)
            redo_lista = [lista]
            undo_lista.append([el for el in lista])
        elif optiune == "3":
            lista1 = uiModificaCheltuiala(lista)
            if lista1:
                lista=lista1
                redo_lista = [lista]
                undo_lista.append([el for el in lista])
        elif optiune == "4":
            uiOrdonareDupaSuma(lista)
        elif optiune == "5":
            uiSumaPerApartament(lista)
        elif optiune == "u":
            try:

                [lista,undo_lista,redo_lista]=undo(lista,undo_lista,redo_lista)
            except ValueError:
                print("Nu se poate face Undo")
        elif optiune == "r":
            try:
                [lista, undo_lista, redo_lista] = redo(lista, undo_lista, redo_lista)
            except ValueError:
                print("Nu se poate face redo")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
