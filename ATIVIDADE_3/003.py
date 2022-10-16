#POO_03 - Crie um programa que liste os funcionários de determinado sexo,
#informado pelo usuário.

from FakeDB import FakeDB

sexo = input("Insira 'M' para masculino e 'F' para feminino: ").lower()

db = FakeDB()


for item in db.listFuncionarios:
    if (item.sexo.lower() == sexo[0]):
        print(item.nome + " " +item.sobrenome)