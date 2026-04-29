import mysql.connector, os ## import da biblioteca para conectar bancos MySQL num código Python + os para limpar o terminal com o "os.system("cls")"

"""
Sistema CRUD com Python e MySQL
- Operações: Create, Read, Update, Delete
- Conexão com banco de dados
- Menu interativo no terminal
"""

## Funções 
def UpdateTabela(cursor,connect):
    LeituraTabela(cursor) ## Printa todos os valores da tabela com SELECT * FROM aluno
    values = []
    id = int(input("Qual id deseja modificar ?"))
    os.system("cls")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    coluna = int(input("Qual coluna deseja modificar ?(1-nome, 2-email, 3-telefone, 4-data de nascimento)"))
    match(coluna): ## o match funciona do mesmo jeito que um switch case, é o switch case do python
        case 1:
            coluna = "nome"
        case 2:
            coluna = "email"
        case 3:
            coluna = "telefone"
        case 4:
            coluna = "data_nascimento"
        case _:
            print("Valor Inválido.")

    os.system("cls")
    valor = str(input("Digite o valor que deseja adicionar na linha: "))
    ## na linha abaixo salvamos numa lista as variáveis que são necessárias para o comando SQL de UPDATE rodar corretamente, para mandarmos junto do comando sql na função cursor.execute 
    values.append(valor)
    values.append(id)
    sql = f"UPDATE aluno SET {coluna} = %s WHERE id = %s"
    try:
        cursor.execute(sql,values) ## manda o comando SQL para o MySQL + a lista com os valores que vão preencher as mascaras do comando SQL(a lista está com os valores em ordem)
        connect.commit() ## O comando é executado e as alterações no banco são feitas
        print("Dado atualizado na tabela do banco de dados com sucesso!!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    except Exception as erro:
        print(f"Não foi possível atualizar a linha de 'alunos'. Error: {erro}")

def InsertTabela(cursor,connect):
    while(True):
        values = [] ## Lista que vai guardar os valores que serão enviados no comando INSERT atráves do cursor
        sql = "INSERT INTO aluno(nome,email,telefone,data_nascimento) VALUES(%s,%s,%s,%s)" ## Usamos as mascaras caso não tenhamos os valores definidos para sobrescreve-los no comando sql, podendo ser colado um valor futuramente em cima da mascara %s
        os.system("cls")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Digite o nome do aluno,email,telefone e data de nascimento(no formato YYYY-MM-DD):")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for cont in range(4):
            if cont == 0:
                valor = str(input("Digite o nome do aluno: "))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            elif cont == 1:
                valor = str(input("Digite o email do aluno(nome@email.com): "))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            elif cont == 2:
                valor = str(input("Digite o telefone do aluno(83 99999-9999): "))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            elif cont == 3:
                valor = str(input("Digite a data de nascimento do aluno(no formato YYYY-MM-DD): "))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            values.append(valor)
        try:
            cursor.execute(sql,values) ## manda o comando SQL para o MySQL + a lista com os valores que vão preencher as mascaras do comando SQL(a lista está com os valores em ordem)
            connect.commit() ## O comando é executado e as alterações no banco são feitas
            print("Dados inseridos na tabela do banco de dados com sucesso!!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        except Exception as erro:
            print(f"Algo deu errado, erro: {erro}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        continuar = str(input("Deseja adicionar mais um aluno ?(S/N) "))
        if continuar != "S":
            break

def LeituraTabela(cursor):
    cursor.execute("SELECT * FROM aluno") ## Manda o comando SQL para o MySQL
    resultado = cursor.fetchall() ## Retorna o resultado do comando SQL descrito no último cursor.execute()

    for linha in resultado:
        print(linha)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def DeleteTabela(cursor,connect):
    LeituraTabela(cursor)
    id = int(input("Digite o ID da linha que deseja remover: "))
    os.system("cls")
    try:
        cursor.execute(f"DELETE FROM aluno WHERE id = {id}") ## manda o comando SQL para o MySQL
        connect.commit() ## O comando é executado e as alterações no banco são feitas
        print("Linha da tabela removida com sucesso!")
    except Exception as error:
        print(f"Não foi possível remover a linha. ERRO: {error}")


## CÓDIGO PRINCIPAL

## PREENCHA COM SEUS DADOS DO MYSQL
connect = mysql.connector.connect( ## Conexão com o banco de dados MySQL
    host = "seu hoostname",
    user="seuusername",
    database = "atividade_pratica_gabrielferreira"
)

cursor = connect.cursor()
while(True):
    os.system("cls")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    operacao = int(input("Escolha uma operação SQL para o banco de dados: 1-Update 2-Read 3-Insert 4-Delete 5-Sair"))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    match(operacao):
        case 1:
            UpdateTabela(cursor,connect) ## Executa a função para atualizar valores na linha de um determinado aluno (buscado pelo id)
            input("Aperte enter para continuar com o programa...")
        case 2:
            LeituraTabela(cursor) ## Executa a função para exibir todas as linhas da tabela
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            input("Aperte enter para continuar com o programa...")
        case 3:
            InsertTabela(cursor,connect) ## Executa a função para Inserir valores na tabela aluno
            input("Aperte enter para continuar com o programa...")
        case 4:
            DeleteTabela(cursor,connect) ## Executa a função para deletar uma linha de dados da tabela (buscada pelo id)
            input("Aperte enter para continuar com o programa...")
        case 5:
            print("Saindo...")
            break
        case _:
            print("Digite um valor básico preente no menu,valores como 1,2,3,4 ou 5")




        
            