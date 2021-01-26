import MySQLdb


def conectar():
    """
    Função para conectar ao servidor
    """
    try:
        conn = MySQLdb.connect(
            db='pmysql',
            host='127.0.0.1',
            user='thayse',
            passwd='Thamar.0103'
        )

        return conn
    except MySQLdb.Error as e:
        print(f'Erro na conexao ao MySQL Server1: {e}')

def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    if conn:
      conn.close()


def listar():
    """
    Função para listar os produtos
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()

    if len(livros) > 0:
        print('Listando os livros...')
        for livro in livros:
            print(f'ID: {livro[0]}')
            print(f'Livro: {livro[1]}')
            print(f'Autor: {livro[2]}')
            print(f'Editora: {livro[3]}')
            print(f'Ano: {livro[4]}')
            print(f'Preço: {livro[5]}')
    else:
        print("Não existem produtos cadastrados.")
    desconectar(conn)


def inserir():
    """
    Função para inserir um produto
    """  
    conn = conectar()
    cursor = conn.cursor()

    livro = input('Digite o nome do livro: ')
    autor = input('Digite o nome do autor: ')
    editora = input('Digite o nome da editora: ')
    ano = int(input('Digite o ano de publicação: '))
    preco = float(input('Digite o preço: '))

    cursor.execute(f"INSERT INTO livros (livro, autor, editora, ano, preco) VALUES ('{livro}', '{autor}', '{editora}', {ano}, {preco})")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto {livro} foi inserido com sucesso.')
    else:
        print('Não foi possivel inserir.')
    desconectar(conn)


def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o código do livro: '))
    livro = input('Informe o novo nome do livro: ')
    autor = input('Informe o novo nome do autor: ')
    editora = input('Informe o novo nome da editora: ')
    ano = int(input('Informe o novo ano de publicação: '))
    preco = float(input('Informe o novo preço: '))

    cursor.execute(f"UPDATE livros SET livro='{livro}', autor='{autor}', editora='{editora}', ano={ano}, preco={preco} "
                   f"WHERE id={codigo}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O livro {livro} foi atualizado com sucesso.')
    else:
        print('Não foi possivel atualizar')
    desconectar(conn)


def deletar():
    """
    Função para deletar um produto
    """  
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o código do livro: '))

    cursor.execute(f'DELETE FROM livros WHERE id={codigo}')
    conn.commit()

    if cursor.rowcount == 1:
        print('Excluido')
    else:
        print(f'Não foi possivel excluir o livro do código {codigo}.')
    desconectar(conn)

def menu():
    """
    Função para gerar o menu inicial
    """
    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')
