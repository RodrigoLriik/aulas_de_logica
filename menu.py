biblioteca = []
 
def mostrar_menu():
    print("\nMenu principal Biblioteca:")
    print("1. Adicionar Livro")
    print("2. Remover Livro")
    print("3. Buscar Livro") #Função em Teste
    print("4. Listar Livros")
    print("5. Verificar Disponibilidade")
    print("6. Emprestimo de Livro") #Função em Contrução 
    print("7. Sair")
 
 
def adicionar_livro(titulo, autor, genero):
    #dicionario
    livro = {'titulo': titulo,'autor': autor, 'genero': genero, 'disponivel': True}
    biblioteca.append(livro)
    print(f"Livro '{titulo}' adicionado com sucesso.")
 
def remover_livro(titulo):
    for livro in biblioteca:
        if livro['titulo'].lower() == titulo.lower():
            biblioteca.remove(livro)
            print(f"Livro '{titulo}' removido com sucesso.")
            return
    print(f"Livro '{titulo}' não encontrado.")
 
#BUSCAR --- SOLUÇÃO PARA O ESSA FUNÇÃO
def buscar_livro(titulo):
    for livro in biblioteca:
        if livro['titulo'].lower() == titulo.lower():
            disponivel = "disponível" if livro['disponivel'] else "indisponível"
            print(f"Livro encontrado: '{livro['titulo']}' - {disponivel}")
            return
    print(f"Livro '{titulo}' não encontrado.")
 
def listar_livros():
    if not biblioteca:
        print("Nenhum livro na biblioteca.")
    else:
        print("Lista de livros:")
        for livro in biblioteca:
            disponivel = "disponível" if livro['disponivel'] else "indisponível"
            print(f" - {livro['titulo']} ({disponivel})")
 
def verificar_disponibilidade(titulo):
    for livro in biblioteca:
        if livro['titulo'].lower() == titulo.lower():
            if livro['disponivel']:
                print(f"Livro '{titulo}' está disponível.")
            else:
                print(f"Livro '{titulo}' está indisponível.")
            return
    print(f"Livro '{titulo}' não encontrado.")
 
 
while True:
    mostrar_menu()
    escolha = int(input("Escolha uma opção do menu: "))
 
    if escolha == 1:
        titulo = input("Digite o Titulo do Livro: \n")
        autor = input("Digite o nome do autor:\n")
        genero = input("Digite o genero do livro: \n")
        adicionar_livro(titulo, autor, genero)
    elif escolha == 2:
        titulo = input("Digite o Titulo do Livro que deseja remover: \n")
        remover_livro(titulo)
    elif escolha == 3:
        titulo = input("Digite o Titulo do Livro que deseja encontrar: \n")
        buscar_livro(titulo)
    elif escolha == 4:
        titulo = input("Listar todos os livros: \n")
        listar_livros()
    elif escolha == 5:
        titulo = input("Digite o título do livro para verificar disponibilidade:\n ")
        verificar_disponibilidade(titulo)
    elif escolha == 6:
        titulo = input("Emprestimo de livro:\n ")
        #IMPLEMENTAR ESSA FUNÇÃO
        #emprestimo_livro(titulo,autor)
    else:
        print("Fechando o Sistema...")
        break