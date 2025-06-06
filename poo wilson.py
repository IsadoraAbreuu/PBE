#dentro de uma classe (objeto) podemos criar métodos (funções = 'andar', 'bater ponto') para esse objeto e aributos (valores = 'idade', 'cpf') que referem a esse objeto
#classe forma de bolo
#objeto proprio bolo
#metodo o que o bolo faz, cresce, esquenta
#atributo sabor do bolo, cor

#criar classe
"""class Bolo():
    def __init__(self, cobertura: str, recheio: str, qtd_fatias: int, sabor = 'chocolate'):
        self.recheio = recheio
        self.cobertura = cobertura
        self.qtd_fatias = qtd_fatias
        lista_de_sabores = ['chocolate', 'morango', 'laranja']
        if sabor in lista_de_sabores:
            self.sabor = sabor
        else:
            print("Sabor inválido.")

    def comer_bolo(self):
        if self.qtd_fatias <= 0:
            print("O bolo acabou ;-;")
        else:
            print("O bolo de ", self.sabor, "foi comido")
            self.qtd_fatias -= 1

    def comer_n_fatias(self, qtd_fatias_comidas):
        if self.qtd_fatias < qtd_fatias_comidas:
            print("Não tem tudo isso de bolo")
        elif self.qtd_fatias == 0:
            print("Não tem bolo")
        else:
            print(qtd_fatias_comidas, "foram comidas do bolo", self.sabor)
            self.qtd_fatias -= qtd_fatias_comidas


bolo_chocolate = Bolo('chocolate', 'chocolate','chocolate', 8)
bolo_morango = Bolo('morango', 'morango', 'morango', 6)
bolo_laranja = Bolo('chocolate', 'laranja', 8, 'laranja')


bolo_laranja.comer_n_fatias(8)
print(bolo_laranja.qtd_fatias)"""

#exercicio1
class Cookie():
    def __init__(self, recheio: str, massa: str, qtd_comprada: int, complemento: str, tamanho: str, numero_mordidas: int = 7):
        self.recheio = recheio
        self.massa = massa
        self.qtd_comprada = qtd_comprada
        complementos = ['gotas de chocolate branco', 'gotas de chocolate ao leite', 'MMs', 'amendoim', 'granulado']
        tamanhos = ['pequeno', 'médio', 'grande']
        self.numero_mordidas = numero_mordidas

        if complemento in complementos:
            self.complemento = complemento
        else:
           print("Complemento inválido.")

        if tamanho in tamanhos:
            self.tamanho = tamanho
        else:
            print("Tamanho inválido.")

    def comprar(self, qtd_comprada):
        qtd_no_estoque = 40
        if qtd_comprada > qtd_no_estoque:
            print("Não é possível comprar tudo isso de cookies.")
        elif qtd_comprada < qtd_no_estoque:
            print("Obrigada pela compra, volte sempre!")
        else:
            print("Você zerou nosso estoque, volte sempre para nos deixar ricos <3")


    def comer(self, mordidas):
        if mordidas >= self.numero_mordidas:
            print("O cookie de", self.massa, "com", self.recheio, "e complementos de", self.complemento, "acabou!")
        elif mordidas < self.numero_mordidas:
            self.numero_mordidas -= mordidas
            print("faltam",self.numero_mordidas, "mordidas para o cookie de",self.massa, "com",self.recheio, "e complementos de",self.complemento,"acabar")
        else:
            print("Você não comeu nada")

cookie1 = Cookie('chocolate', 'baunilha', 8, 'MMs', 'médio')
cookie2 = Cookie('baunilha', 'red velvet', 4, 'gotas de chocolate branco', 'pequeno')

cookie2.comer(5)
cookie1.comprar(40)
