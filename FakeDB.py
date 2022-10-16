from Funcionario import Funcionario
import random
from datetime import date

class FakeDB:
    listFuncionarios = []

    def __init__(self):
        self.listFuncionarios = self.GerarRegistros()

    def GerarRegistros(self):
        funcionarioList = []

        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Fernando", "Mendes", "M", date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Juan", "Costa", "M", date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Cauã", "Cardoso", "M", date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Yuri", "Rosa", "M", date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Noah", "Rosa", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Davi", "Lima", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Juan", "Cavalcanti", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Lucca", "Castro", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Heitor", "Silveira", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Calebe", "Sales", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Thales", "Moraes", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Diego", "Vieira", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Murilo", "Caldeira", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Gabriel", "Caldeira", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Benício", "Nascimento", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Pietro", "Nunes", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Marcelo", "Souza", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Thomas", "Nascimento", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "João", "Moraes", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Enzo", "Luz", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Thales", "Jesus", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Ryan", "Farias", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Marcos", "Moraes", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Henrique", "Fernandes", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Bruno", "Paz", "M",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Heloísa", "Rocha", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Helena", "Oliveira", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Bruna", "Correia", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Stella", "Barros", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Alexia", "Teixeira", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Carolina", "Lima", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Catarina", "Carvalho", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Clara", "Pinto", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Julia", "Rocha", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Sarah", "AraÃºjo", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Evelyn", "Alves", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Clarice", "Sales", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Luiza", "Peixoto", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Kamilly", "Mota", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Fernanda", "Porto", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Cecília", "Cardoso", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Maria", "Costa", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Isadora", "Moura", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Lara", "Monteiro", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Valentina", "Vieira", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Alexia", "Novaes", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Isabelly", "Mendes", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Sophia", "Rocha", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))
        funcionarioList.append(Funcionario(len(funcionarioList) + 1, "Fernanda", "Luz", "F",date(year=random.randrange(1989, 2010), month=random.randrange(1, 12), day=random.randrange(1, 28))))

        return funcionarioList
