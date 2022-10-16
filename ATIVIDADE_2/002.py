#POO_02 - Crie um programa que liste os funcionários que fazem aniversário em
#determinado ano, informado pelo usuário.

from FakeDB import FakeDB

ano = int(input("Insira o ano de nascimento: "))

db = FakeDB()


for item in db.listFuncionarios:
    if (item.dataNascimento.year == ano):
        print(item.nome + " " +item.sobrenome)