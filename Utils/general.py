def undo(lista,undo_lista,redo_lista=[]):
    '''
    Face un undo la lista .
    :param lista: lista data
    :param undo_lista: lista de undo
    :return: o lista de liste,cele 2 liste data ca parametru modificate
    '''
    if len(undo_lista) > 0:
        new_lista = []
        redo_lista.append(lista)
        for i, el in enumerate(undo_lista):
            if i != len(undo_lista) - 1:
                new_lista.append(el)
        undo_lista = new_lista
        if len(undo_lista) > 0:
            lista = undo_lista[-1]
        else:
            lista = []
        return [lista,undo_lista,redo_lista]
    else :
        raise (ValueError)
def redo(lista,undo_lista,redo_lista):
    '''
    Face redo la lista .
    :param lista: list,lista data
    :param undo_lista: lista de liste,lista de undo
    :param redo_lista: lista de liste ,lista de redo
    :return: lista de liste ,cele 3 liste modificate
    '''
    if len(redo_lista)>0:
        redo_lista.pop()
        if len(redo_lista)>0:
            lista=redo_lista[-1]
        else:
            lista=[]
        undo_lista.append(lista)
        return[lista,undo_lista,redo_lista]
    else:
        raise (ValueError)

def test_undo():
    lista = [5,6]
    undo_lista=[[1],[1,2],[],[5,6]]
    redo_lista=[]
    [lista,undo_lista,redo_lista]=undo(lista,undo_lista,redo_lista)
    assert lista==[]
    assert undo_lista==[[1],[1,2],[]]
    lista = [5, 6]
    undo_lista = [[1], [1, 2], [10,11], [5, 6]]
    [lista, undo_lista,redo_lista] = undo(lista, undo_lista,redo_lista)
    assert lista==[10,11]
    assert undo_lista == [[1], [1, 2], [10,11]]
def test_redo():
    lista = [5, 6]
    undo_lista = [[1], [1, 2], [], [5, 6]]
    redo_lista = [[8,9],[10],[5,6]]
    [lista, undo_lista, redo_lista] = redo(lista, undo_lista, redo_lista)
    assert lista == [10]
    assert undo_lista == [[1], [1, 2], [],[5,6],[10]]
    assert redo_lista==[[8,9],[10]]
    lista = [5, 6]
    undo_lista = [[1], [1, 2], [], [5, 6]]
    redo_lista = [[8, 9], [11,12,13,14], [5, 6]]
    [lista, undo_lista, redo_lista] = redo(lista, undo_lista, redo_lista)
    assert lista == [11,12,13,14]
    assert undo_lista == [[1], [1, 2], [], [5, 6], [11,12,13,14]]
    assert redo_lista == [[8, 9], [11,12,13,14]]
test_undo()
test_redo()
