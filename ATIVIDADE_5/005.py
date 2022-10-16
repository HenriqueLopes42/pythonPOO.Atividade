#POO_05 - Crie um programa que busque e liste os funcionários que tenham as 3
#letras determinadas no sobrenome, informadas pelo usuário. Por exemplo, procure
#todos funcionários que tenham as letras SAN no sobrenome.

from FakeDB import FakeDB

db = FakeDB()

sobrenomeBuscar = input("Insira as tres primeira letras do sobrenome: ").lower()

for item in db.listFuncionarios:
    if (item.sobrenome.lower().startswith(sobrenomeBuscar)):
        print(item.nome+" "+item.sobrenome)