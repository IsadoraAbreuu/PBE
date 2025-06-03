class Pessoa:
    #define Pessoa (nome e idade)
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá \nMeu nome é {self.nome} e tenho {self.idade} anos.")

    #transforma em string e printa o nome
    def __str__(self):
        return f"{self.nome}"

    #compara - equals
    def __eq__(self, other):
        if isinstance(other, Pessoa):
            #se nome e a idade é igual ao nome e idade de outra coisa
            #pessoa1 == pessoa2
            if self.nome == other.nome and self.idade == other.idade:
                return True
        return False

    #def __ge__(self, other): maior igual (>=)
    #def __gt__(self, other): maior (>)
    #def __lt__(self, other): menor (<)
    #def __le__(self, other): menor igual (<=)
    #def __eq__(self, other): igual (==)

    def __len__(self):
        return self.idade

    #transformar em dicionário
    def to_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade
                }

pessoa1 = Pessoa("Fernanda Scanacapra", 35)
pessoa1.apresentar()
print(pessoa1)


pessoa2 = Pessoa("Fernanda Abreu", 35)
if pessoa1 == pessoa2:
    print("Pessoas são iguais")
else:
    print("Pessoas não são iguais")


dicionario = pessoa1.to_dict()
print(dicionario)


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        #acima dele
        super().__init__(nome,idade)
        self.cargo = cargo
    def apresentar(self):
        #chama o print da primeira função apresentar (chama do pai)
        #super().apresentar()
        print(f"Olá, eu sou {self.nome}, tenho {self.idade} anos e sou {self.cargo}")

funcionario = Funcionario("ABC", 25, "Aprendiz")
funcionario.apresentar()

lista_pessoas = [pessoa1, pessoa2, funcionario]
for pessoa in lista_pessoas:
    pessoa.apresentar()

#ENCAPSULAMENTO
class ContaBancaria:
    def __init__(self, titular, saldo):
        #qualquer um pode acessar
        self.titular = titular
        #escondido
        self.__saldo = saldo

    """#geter e seter (pegar e alterar o valor)
    def get_saldo(self):
        return self.__saldo #-5000
    def set_saldo(self, valor):
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo")
        self.__saldo = valor"""

    # outra maneira de geter e seter
    @property  # propriedade de um atributo
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo")
        self.__saldo = valor

minha_conta = ContaBancaria("Dorival", - 5000)

from abc import ABC, abstractmethod
#cria uma interface
#abstração, colocar uma lei, uma obrigatoriedade

class Pagamento(ABC):

    #classe abstrata
    @abstractmethod
    def autorizar(self, valor):
        pass
    @abstractmethod
    def estornar(self, valor):
        pass

class Pix(Pagamento):
    def autorizar(self, valor):
        print(f"Transferindo R$ {valor} via PIX...")

    def estornar(self, valor):
        print(f"Devolvendo R$ {valor} via PIX...")

Pix().autorizar(122)