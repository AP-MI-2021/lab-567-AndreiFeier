from Domain.cheltuiala import getNr_apartament, creeazaCheltuiala, getId, getSuma, getData, getTip

def ordonareDupaSuma(lista):

    '''
    :param lista:
    :return:
    '''
    return sorted(lista, key=lambda cheltuiala: getSuma(cheltuiala), reverse = True)


def sumaPerApartament(lista):
    '''
    :param lista:
    :return:
    '''
    rezultat = {}
    for cheltuiala in lista:
        nr_apartament = getNr_apartament(cheltuiala)
        suma = getSuma(cheltuiala)
        if nr_apartament in rezultat:
            rezultat[nr_apartament] = rezultat[nr_apartament] + suma
        else:
            rezultat[nr_apartament] = suma
    return rezultat