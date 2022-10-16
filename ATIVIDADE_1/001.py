from FakeDB import FakeDB

db = FakeDB()

numebuscar = input("Insira um inicio do primeiro nome: ").lower()

for item in db.listFuncionarios:
    if (item.nome.lower().startswith(numebuscar)):
        print(item.nome)
