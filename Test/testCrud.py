from Domain.cheltuiala import getId, getNr_apartament, getSuma, getData, getTip
from Logic.Crud import adaugaCheltuiala, getById, stergeCheltuiala, modificaCheltuiala


def testAdaugaCheltuiala():
    lista = []
    lista = adaugaCheltuiala("1", 2, 200, 2000, "apa", lista)

    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getNr_apartament(getById("1", lista)) == 2
    assert getSuma(getById("1", lista)) == 200
    assert getData(getById("1", lista)) == 2000
    assert getTip(getById("1", lista)) == "apa"


def testStergeCheltuiala():
    lista = []
    lista = adaugaCheltuiala("1", 2, 200, 2000, "apa",  lista)
    lista = adaugaCheltuiala("2", 3, 450, 1999, "caldura",  lista)

    lista = stergeCheltuiala("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

    lista = stergeCheltuiala("3", lista)

    assert len(lista) == 1
    assert getById("2", lista) is not None

def testModificaCheltuiala():
    lista = []
    lista = adaugaCheltuiala("1", 2, 200, 2000, "apa",  lista)
    lista = adaugaCheltuiala("2", 3, 450, 1999, "caldura",  lista)

    lista = modificaCheltuiala("1", 4, 220, 2020, "caldura",  lista)

    cheltuialaUpdatata = getById("1", lista)
    assert getId(cheltuialaUpdatata) == "1"
    assert getNr_apartament(cheltuialaUpdatata) == 4
    assert getSuma(cheltuialaUpdatata) == 220
    assert getData(cheltuialaUpdatata) == 2020
    assert getTip(cheltuialaUpdatata) == "caldura"


    cheltuialaNeupdatata = getById("2", lista)
    assert getId(cheltuialaNeupdatata) == "2"
    assert getNr_apartament(cheltuialaNeupdatata) == 3
    assert getSuma(cheltuialaNeupdatata) == 450
    assert getData(cheltuialaNeupdatata) == 1999
    assert getTip(cheltuialaNeupdatata) == "caldura"


    lista = []
    lista = adaugaCheltuiala("1", 2, 200, 2000, "apa",  lista)

    lista = modificaCheltuiala("3", 5, 150, 2018, "electricitate", lista)

    cheltuialaNeupdatata = getById("1", lista)
    assert getId(cheltuialaNeupdatata) == "1"
    assert getNr_apartament(cheltuialaNeupdatata) == 2
    assert getSuma(cheltuialaNeupdatata) == 200
    assert getData(cheltuialaNeupdatata) == 2000
    assert getTip(cheltuialaNeupdatata) == "apa"