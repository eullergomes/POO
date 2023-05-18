class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

livro1 = Livro('titulo-1', 'autor-1', 99)
livro2 = Livro('titulo-2', 'autor-2', 66)
livro3 = Livro('titulo-3', 'autor-3', 77)

print(f'Qtd páginas do {livro1.titulo}')