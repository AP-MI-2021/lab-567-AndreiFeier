from Logic.Crud import adaugaCheltuiala
from Test.testAll import runAllTests
from UI.console import runMenu

def main():
    runAllTests()
    lista = []
    lista = adaugaCheltuiala("1", 2, 10, 10, "caldura", lista)
    lista = adaugaCheltuiala("2", 3, 12, 30, "apa", lista)
    runMenu(lista)

main()