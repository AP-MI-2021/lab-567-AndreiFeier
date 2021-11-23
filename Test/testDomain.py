from Domain.cheltuiala import creeazaCheltuiala, getId, getNr_apartament, getSuma, getData, getTip


def testCheltuiala():
    cheltuiala = creeazaCheltuiala("1", 1, 10, 20, "caldura")

    assert getId(cheltuiala) == "1"
    assert getNr_apartament(cheltuiala) == 1
    assert getSuma(cheltuiala) == 10
    assert getData(cheltuiala) == 20
    assert getTip(cheltuiala) == "caldura"