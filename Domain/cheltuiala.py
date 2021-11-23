def creeazaCheltuiala(id, nr_apartament, suma, data, tip):
    '''
    creaza un dictionar ce reprezinta o cheltuiala
    :param id: string
    :param nr_apartament: int
    :param suma: float
    :param data: int
    :param tip: string
    :return: un dictionar ce contine o cheltuiala
    '''
    return {
        "id": id,
        "nr_apartament": nr_apartament,
        "suma": suma,
        "data": data,
        "tip": tip,
    }

def getId(cheltuiala):
    '''
    da id-ul unei cheltuieli
    :param cheltuiala: dictionar ce contine o cheltuiala
    :return: id-ul cheltuielii
    '''
    return cheltuiala["id"]

def getNr_apartament(cheltuiala):
    return cheltuiala["nr_apartament"]

def getSuma(cheltuiala):
    return cheltuiala["suma"]

def getData(cheltuiala):
    return cheltuiala["data"]

def getTip(cheltuiala):
    return cheltuiala["tip"]


def toString(cheltuiala):
    return "Id: {}, Nr_apartament: {}, Suma: {}, Data: {}, Tip: {}".format(
        getId(cheltuiala),
        getNr_apartament(cheltuiala),
        getSuma(cheltuiala),
        getData(cheltuiala),
        getTip(cheltuiala)
    )