class Cheltuiala:
    def __init__(self,nr_apartament,suma,data,tip):
        '''
        Initializeaza un obiect de tip cheltuiala
        :param nr_apartament:int
        :param suma:int
        :param data:string
        :param tip:string
        '''
        self.__nr_apartament=nr_apartament
        self.__suma=suma
        self.__data=data
        self.__tip=tip
    def get_nrap(self):
        return self.__nr_apartament
    def get_suma(self):
        return self.__suma
    def get_data(self):
        return self.__data
    def get_tip(self):
        return self.__tip
    def set_nrap(self,value):
        self.__nr_apartament=value
    def set_suma(self,value):
        self.__suma=value
    def set_data(self,value):
        self.__data=value
    def set_tip(self,value):
        self.__tip=value
    def __eq__(self,other):
        '''
        Testeaza daca 2 obiecte de tipul cheltuiala sunt egale.
        :param other:Cheltuiala
        :return:bool
        '''
        return self.get_nrap()==other.get_nrap() and self.get_suma()==other.get_suma() and self.get_data()==other.get_data() and self.get_tip()==other.get_tip()
    def __str__(self):
        return "Nr ap: "+str(self.get_nrap())+" - Suma: "+str(self.get_suma())+" - Data: "+self.get_data()+" - Tip: "+ self.get_tip()
def test_init():
    c=Cheltuiala(123,900,"2/10/2020","intretinere")
    assert c.get_nrap()==123
    assert c.get_suma()==900
    assert c.get_data()=="2/10/2020"
    assert c.get_tip()=="intretinere"
def test_set():
    c = Cheltuiala(123, 900, "2/10/2020", "intretinere")
    c.set_nrap(140)
    assert c.get_nrap()==140
    c.set_suma(600)
    assert c.get_suma()==600
    c.set_data("4/12/2021")
    assert c.get_data()=="4/12/2021"
    c.set_tip("canal")
    assert c.get_tip()=="canal"
def test_eq():
    c1 = Cheltuiala(123, 900, "2/10/2020", "intretinere")
    c2 = Cheltuiala(123, 900, "2/10/2020", "intretinere")
    assert c1==c2
    c2 = Cheltuiala(124, 900, "2/10/2020", "intretinere")
    assert c1!=c2
test_eq()
test_set()
test_init()