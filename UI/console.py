from Logic.functionalitate import ordonareDupaSuma ,sumaPerApartament
from Domain.cheltuiala import toString
from Logic.Crud import adaugaCheltuiala, stergeCheltuiala, modificaCheltuiala



def printMenu():
    print("1. Adaugare cheltuiala")
    print("2. Stergere cheltuiala")
    print("3. Modificare cheltuiala")
    print("6. Ordonarea cheltuielilor descrescător după sumă.")
    print("7. Afișarea sumelor lunare pentru fiecare apartament.")
    print("u. Undo")
    print("a. Afisare cheltuieli")
    print("x. Iesire")


def uiAdaugaCheltuiala(lista):
    id = input("Dati id-ul: ")
    nr_apartament = int(input("Dati nr_apartamentului: "))
    suma = float(input('Dati suma: '))
    data =int(input("Dati data: "))
    tip = input("Dati tipul: ")
    return adaugaCheltuiala(id, nr_apartament, suma, data, tip, lista)


def uiStergeCheltuiala(lista):
    id = input("Dati id-ul cheltuielii de sters: ")
    return stergeCheltuiala(id, lista)


def uiModificaCheltuiala(lista):
    id = input("Dati id-ul cheltuielii de modificat: ")
    nr_apartament = int(input("Dati noul nr de apartament: "))
    suma = float(input("Dati noua suma: "))
    data = int(input("Dati data:"))
    tip = input("Dati noul tip: ")
    return modificaCheltuiala(id, nr_apartament, suma, data, tip, lista)


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
    lista=[]
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaCheltuiala(lista)
            undo_lista.append([el for el in lista])
        elif optiune == "2":
            lista = uiStergeCheltuiala(lista)
            undo_lista.append([el for el in lista])
        elif optiune == "3":
            lista = uiModificaCheltuiala(lista)
            undo_lista.append([el for el in lista])
        elif optiune == "6":
            uiOrdonareDupaSuma(lista)
        elif optiune == "7":
            uiSumaPerApartament(lista)
        elif optiune == "u":
            if len(undo_lista)>0:
                new_lista=[]
                for i,el in enumerate(undo_lista):
                    if i!=len(undo_lista)-1:
                        new_lista.append(el)
                undo_lista=new_lista
                if len(undo_lista)>0:
                    lista = undo_lista[-1]
                else:
                    lista=[]
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")