from domain.entity import Cheltuiala


class CRepo:
    def __init__(self):
        '''
        Initializeaza un repository gol
        '''
        self.__cheltuieli=[]
    def store(self,cheltuiala):
        '''
        Adauga o noua cheltuiala in repo
        :param cheltuiala:Cheltuiala
        :return:none
        '''
        self.__cheltuieli.append(cheltuiala)
    def find(self,n,s,d,t):
        '''
        Gaseste o cheltuiala  in lista
        :param n:int
        :param s:int
        :param d:string
        :param t:string
        :return:Cheltuiala
        '''
        for c in self.__cheltuieli:
            if c.get_nrap()==n and c.get_suma()==s and c.get_data()==d and c.get_tip()==t:
                return c
    def update(self,n,s,d,t,suma,data,tip):
        '''
        Actualizeaza o cheltuiala din lista
        :param n:int
        :param s:int
        :param d:string
        :param t:string
        :param suma: int
        :param data: string
        :param tip: string
        :return: Cheltuiala
        '''
        c=self.find(n,s,d,t)
        if c:
            if suma!="":
                c.set_suma(suma)
            if data!="":
                c.set_data(data)
            if tip!="":
                c.set_tip(tip)
        return c
    def delete(self,n,s,d,t):
        '''
        Seterge o cheltuiala din lista
        :param n: int
        :param s: int
        :param d: string
        :param t: string
        :return: Cheltuiala
        '''
        c=self.find(n,s,d,t)
        if c:
            self.__cheltuieli=[el for el in self.__cheltuieli if el != c]
        return c
    def delete_ap(self,nrap):
        '''
        Sterge toate cheltuielile de la nr ap
        :param nrap: int
        :return: none
        '''
        self.__cheltuieli=[el for el in self.__cheltuieli if el.get_nrap()!=nrap]
    def get_all(self):
        return self.__cheltuieli
    def size(self):
        return len(self.__cheltuieli)
    def __str__(self):
        a=[]
        for el in self.__cheltuieli:
            a.append(str(el))
        return "\n".join(a)
def test_store():
    ch=CRepo()
    c=Cheltuiala(123,900,"2/10/2020","intretinere")
    ch.store(c)
    assert ch.get_all()[0]==c
    assert ch.size()==1
def  test_update():
    ch = CRepo()
    c = Cheltuiala(123, 900, "2/10/2020", "intretinere")
    ch.store(c)
    c=ch.update(123,900,"2/10/2020","intretinere",600,"5/1/2018","canal")
    assert ch.get_all()[0]==c
    assert ch.size()==1
    assert c.get_nrap()==123
    assert c.get_suma()==600
    assert c.get_data()=="5/1/2018"
    assert c.get_tip()=="canal"
def test_delete():
    ch = CRepo()
    c = Cheltuiala(123, 900, "2/10/2020", "intretinere")
    ch.store(c)
    c2 = ch.delete(123, 900, "2/10/2020", "intretinere")
    assert c2==c
    assert ch.size() == 0
def test_delete_ap():
    ch = CRepo()
    c = Cheltuiala(123, 900, "2/10/2020", "intretinere")
    ch.store(c)
    c = Cheltuiala(123, 300, "1/10/2020", "canal")
    ch.store(c)
    c = Cheltuiala(140, 400, "3/10/2020", "alte cheltuieli")
    ch.store(c)
    ch.delete_ap(123)
    assert ch.get_all()[0]==c
    assert ch.size()==1
test_store()
test_update()
test_delete()
test_delete_ap()





