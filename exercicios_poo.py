#EXERCICIOS DE PROGRAMAÇÃO ORIENTADA A OBJETO
#exercício1
class ItemBiblioteca:
    def __init__(self, titulo:str, ano_publicacao:int, disponivel:bool):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel:
            print(f"O livro {self.titulo} foi emprestado com sucesso.")
            self.disponivel = False
        else:
            print(f"O livro {self.titulo} já está emprestado.")

    def devolver(self):
        if not self.disponivel:
            print(f"O livro {self.titulo} foi devolvido com sucesso.")
            self.disponivel = True
        else:
            print(f"O livro {self.titulo} não foi emprestado.")

    def obter_info(self):
        print(f"Título do livro: {self.titulo} | Ano de publicação: {self.ano_publicacao} | Status de disponibilidade: {self.disponivel}")


class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, disponivel):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.lista_livros = []

    def adicionar_livro(self, livro:ItemBiblioteca):
        self.lista_livros.append(livro)

    def verificar_disponibilidade_colecao(self):
        for livro in self.lista_livros:
            #todos os livros precisam estar disponiveis
            if not livro.disponivel:
                print(f"Livro {livro.titulo} não está disponível.")
                return False
        return True


class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, disponivel):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.numero_edicao = numero_edicao

    def atualizar_edicao(self):