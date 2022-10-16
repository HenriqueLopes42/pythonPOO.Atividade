#POO_04 - Crie um programa que sorteie e liste um determinado número de
#funcionários. Por exemplo, sortear aleatoriamente e listar 5 funcionários, SEM
#REPETIR.

from FakeDB import FakeDB
import random

numero = int(input("Insira a quantidade a ser randomizada: "))

db = FakeDB()

lista = []
while len(lista) < numero:
    func = random.choice(db.listFuncionarios)

    inserirNaLista = True

    for item in lista:
        if (lista.__contains__(func)):
            inserirNaLista = False

    if(inserirNaLista):
        lista.append(func)


for func in lista:
    print(func.nome + " " + func.sobrenome)

