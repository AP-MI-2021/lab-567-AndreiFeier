from Domain.cheltuiala import creeazaCheltuiala, getId


def adaugaCheltuiala(id, nr_apartament, suma, data, tip, lista):
    '''
    adauga o prajitura intr-o lista
    :param id: string
    :param nr_apartament: int
    :param suma: float
    :param data: int
    :param tip: string
    :param lista: lista de cheltuieli
    :return: o lista continand atat elementele vechi, cat si noua cheltuiala
    '''
    cheltuiala = creeazaCheltuiala(id, nr_apartament, suma, data, tip)
    return lista + [cheltuiala]

def getById(id, lista):
    '''
    gaseste o cheltuiala cu id-ul dat intr-o lista
    :param id: string
    :param lista: lista de cheltuieli
    :return: cheltuiala cu id-ul dat din lista sau None, daca aceasta nu exista
    '''
    for cheltuiala in lista:
        if getId(cheltuiala) == id:
            return cheltuiala
    return None

def stergeCheltuiala(id, lista):
    """
    sterge o cheltuiala cu id-ul dat din lista
    :param id: id-ul cheltuielii care se va sterge
    :param lista: lista de cheltuieli
    :return: o lista de cheltuieli fara elementul cu id-ul dat
    """
    return [cheltuiala for cheltuiala in lista if getId(cheltuiala) != id]

def modificaCheltuiala(id, nr_apartament, suma, data, tip, lista):
    """
    modifica o cheltuiala cu id-ul dat
    :param id: id-ul cheltuielii
    :param nr_apartament: numarul apartamentului
    :param suma: suma cheltuielii
    :param data: data cheltuielii
    :param tip: tipul cheltuielii
    :param lista: O lista de cheltuieli.
    :return: lista modificata.
    """
    listaNoua = []
    for cheltuiala in lista:
        if getId(cheltuiala) == id:
            CheltuialaNoua = creeazaCheltuiala(id, nr_apartament, suma, data, tip)
            listaNoua.append(CheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua