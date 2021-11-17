class Console:
    def __init__(self,service):
        '''
        Initializeaza consola
        :param service: CService
        '''
        self.__service=service
    def __add(self):
        n=input("nr apartament: ")
        s=input("suma: ")
        d=input("data: ")
        t=input("tip: ")
        self.__service.add(n,s,d,t)
    def __update(self):
        n = input("nr apartament: ")
        s = input("suma: ")
        d = input("data: ")
        t = input("tip: ")
        suma=input("noua suma: ")
        data=input("noua data: ")
        tip=input("noul tip: ")
        self.__service.update(n,s,d,t,suma,data,tip)
    def __delete(self):
        n = input("nr apartament: ")
        s = input("suma: ")
        d = input("data: ")
        t = input("tip: ")
        self.__service.delete(n,s,d,t)
    def __delete_ap(self):
        n = input("nr apartament: ")
        self.__service.delete_ap(n)
    def __print(self):
        print (self.__service.get_repo())
    def __print_menu(self):
        print ("1.Adauga o cheltuiala")
        print ("2.Actualizeaza o cheltuiala")
        print("3.Sterge o cheltuiala")
        print("4.Sterge toate cheltuielile de la un apartament")
        print("P.Afiseaza toate cheltuielile")
        print("E.Exit")
    def start(self):
        while True:
            self.__print_menu()
            cmd=input("Comanda dvs este: ")
            if cmd == "1":
                self.__add()
            elif cmd == "2":
                self.__update()
            elif cmd == "3":
                self.__delete()
            elif cmd == "4":
                self.__delete_ap()
            elif cmd == "p" or cmd == "P":
                self.__print()
            elif cmd == "e" or cmd =="E":
                return
            else:
                print("Comanda invalida")
