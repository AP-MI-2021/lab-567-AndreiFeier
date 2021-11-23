from Domain.cheltuiala import getSuma, getId
from Logic.Crud import adaugaCheltuiala, getById
from Logic.functionalitate import  ordonareDupaSuma, sumaPerApartament

def testOrdonareDupaSuma():
    lista = []
    lista = adaugaCheltuiala("1", 2, 100, 2000, "apa", lista)
    lista = adaugaCheltuiala("2", 3, 320, 2010, "caldura", lista)
    lista = adaugaCheltuiala("3", 5, 175, 2010, "gaz", lista)

    rezultat = ordonareDupaSuma(lista)

    assert getId(rezultat[0]) == "2"
    assert getId(rezultat[1]) == "3"
    assert getId(rezultat[2]) == "1"

def testSumaPerApartament():
    lista = []
    lista = adaugaCheltuiala("1", 2, 100, 2000, "apa" , lista)
    lista = adaugaCheltuiala("2", 3, 200, 2010, "gaz" , lista)
    lista = adaugaCheltuiala("3", 3, 300, 2010, "gaz" , lista)

    rezultat = sumaPerApartament(lista)

    assert len(rezultat) == 2
    assert rezultat[3] == 500
    assert rezultat[2] == 100