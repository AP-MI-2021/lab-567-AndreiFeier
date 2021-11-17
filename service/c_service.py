from domain.entity import Cheltuiala


class CService:
    def __init__(self,repo,validator=False):
        '''
        Initializeaza service
        :param repo: BRepo
        :param validator:
        '''
        self.__repo=repo
        self.__validator=validator
    def add(self,n,s,d,t):
        '''
        Adauga o cheltuiala
        :param n: int
        :param s: int
        :param d: string
        :param t: string
        :return: Cheltuiala
        '''
        c=Cheltuiala(n,s,d,t)
        self.__repo.store(c)
        return c
    def update(self,n,s,d,t,suma,data,tip):
        '''
        Actualizeaza o cheltuiala
        :param n: int
        :param s: int
        :param d: string
        :param t: string
        :param suma: int
        :param data: string
        :param tip: string
        :return: Cheltuiala
        '''
        self.__repo.update(n,s,d,t,suma,data,tip)
        return Cheltuiala(n,s,d,t)
    def delete(self,n,s,d,t):
        '''
              Sterge o cheltuiala
              :param n: int
              :param s: int
              :param d: string
              :param t: string
              :return: Cheltuiala
              '''
        self.__repo.delete(n, s, d, t)
        return Cheltuiala(n, s, d, t)
    def delete_ap(self,n):
        '''
              Sterge o cheltuiala
              :param n: int
              :return: none
              '''
        self.__repo.delete_ap(n)
    def get_repo(self):
        return self.__repo

