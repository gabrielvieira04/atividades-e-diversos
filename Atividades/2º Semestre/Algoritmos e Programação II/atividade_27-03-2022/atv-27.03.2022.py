#Atividade de persistencia em banco de dados
#Autor: José Gabriel V.

import sqlite3

#Criação da estrutura do banco
def inicializador_bd():
    con = sqlite3.connect("/home/gabrielv/Área de trabalho/Aulas-Py/Atv-banco_de_dados/banco-atv.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS cliente (id integer not null, nome VARCHAR(200), cpf VARCHAR(11), email VARCHAR(100), codigo_plano integer, PRIMARY KEY (id));")
    cursor.execute("CREATE TABLE IF NOT EXISTS plano (codigo integer, nome_do_plano VARCHAR(200), valor_mensal real);")
    con.commit()
    con.close()

def menu_1():
    print("eConnect - Sistema para provedores de Internet\n")
    print("Menu de opções: \n")
    print("1. Cadastro de Clientes.")
    print("2. Cadastro de Planos.")
    print("3. Sair.")

def menu_cliente():
    print("Cadastro de Clientes.\n")
    print("1. Novo cliente.")
    print("2. Listar clientes.")
    print("3. Editar cliente.")
    print("4. Remover cliente")
    print("5. Voltar ao menu principal")

def menu_planos():

    print("Cadastro de Panos.\n")
    print("1. Novo plano.")
    print("2. Listar planos.")
    print("3. Editar plano.")
    print("4. Remover plano")
    print("5. Voltar ao menu principal")

def opcao_invalida():
    print("Você digitou uma opção inválida")

def cadastro_cliente():
    con = sqlite3.connect("/home/gabrielv/Área de trabalho/Aulas-Py/Atv-banco_de_dados/banco-atv.db")
    cursor = con.cursor()
    print("Informe os dados do cliente a serem cadastrados:\n")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    email = input("E-mail: ")
    codigo_plano = int(input("Código Plano: "))
    consultaInsert = "INSERT INTO cliente (nome,cpf,email,codigo_plano) VALUES (?,?,?,?);"
    cursor.execute(consultaInsert,(nome,cpf,email,codigo_plano))
    con.commit()
    con.close()

def listar_cliente():
    con = sqlite3.connect("/home/gabrielv/Área de trabalho/Aulas-Py/Atv-banco_de_dados/banco-atv.db")
    cursor = con.cursor()
    consulta = "SELECT nome, cpf, email, codigo_plano FROM cliente;"
    cursor.execute(consulta)
    print("Clientes presentes no sistema: \n")
    for linha in cursor.fetchall():
        print("Nome", linha[0])
        print("CPF:", linha[1])
        print("E-mail:", linha[2])
        print("Código do plano:", linha[3])
        print(" -------------------")

    con.close()   

def atualizar_cliente():
    cpf = input("Qual o CPF do cliente a ser atualizado ?")
    novoNome = input("Nome: ")
    novoCPF = input("CPF: ")
    novoEmail = input("Email: ")
    novoCodigoPlano = input("Codigo Plano: ")
    con = sqlite3.connect("/home/gabrielv/Área de trabalho/Aulas-Py/Atv-banco_de_dados/banco-atv.db")
    cursor = con.cursor()
    consultaAtualizar = "UPDATE cliente SET nome=?, cpf=?, email=?, codigo_plano=? WHERE cpf=?"
    cursor.execute(consultaAtualizar,(novoNome,novoCPF,novoEmail,novoCodigoPlano,cpf))
    con.commit()
    con.close()

def remover_cliente():
    listar_cliente()
    cpf = int(input("Qual o cpf do cliente a ser removido ?: \n "))
    con = sqlite3.connect("/home/gabrielv/Área de trabalho/Aulas-Py/Atv-banco_de_dados/banco-atv.db")
    cursor = con.cursor()
    consultaDelete = "DELETE FROM cliente WHERE cpf ="
    cursor.execute(consultaDelete+str(cpf))
    con.commit()
    con.close()

def cadastro_plano():
    con = sqlite3.connect("/home/gabrielv/Área de trabalho/Aulas-Py/Atv-banco_de_dados/banco-atv.db")
    cursor = con.cursor()
    print("Cadastro de novo plano\n")
    codigo = int(input("Código: "))
    nome_do_plano = input("Nome do plano: ")
    valor_mensal = input("Valor mensal: ")
    consultaInsert = "INSERT INTO plano (codigo,nome_do_plano,valor_mensal) VALUES (?,?,?);"
    cursor.execute(consultaInsert,(codigo,nome_do_plano,valor_mensal))
    con.commit()
    con.close()

def listar_plano():
    con = sqlite3.connect("/home/gabrielv/Área de trabalho/Aulas-Py/Atv-banco_de_dados/banco-atv.db")
    cursor = con.cursor()
    consulta = "SELECT codigo, nome_do_plano, valor_mensal FROM plano;"
    cursor.execute(consulta)
    print("\n== PLANOS CADASTRADOS ==\n")
    for linha in cursor.fetchall():
        print("Código", linha[0])
        print("Nome do plano:", linha[1])
        print("Valor mensal:", linha[2])
        print(" -------------------")

    con.close()   

def atualizar_plano():
    codigo = input("Informe o código do plano a se atualizar\n")
    novoCodigo = input("Código: ")
    novoNome = input("Nome do plano: ")
    novoValorMensal = input("Valor mensal: ")
    con = sqlite3.connect("/home/gabrielv/Área de trabalho/Aulas-Py/Atv-banco_de_dados/banco-atv.db")
    cursor = con.cursor()
    consultaAtualizar = "UPDATE plano SET codigo=?, nome_do_plano=?, valor_mensal=? WHERE codigo=?"
    cursor.execute(consultaAtualizar,(novoCodigo,novoNome,novoValorMensal,codigo))
    con.commit()
    con.close()

def remover_plano():
    listar_plano()
    codigo = int(input("Informe o codigo do plano a ser removido\n"))
    con = sqlite3.connect("/home/gabrielv/Área de trabalho/Aulas-Py/Atv-banco_de_dados/banco-atv.db")
    cursor = con.cursor()
    consultaDelete = "DELETE FROM plano WHERE codigo ="
    cursor.execute(consultaDelete+str(codigo))
    con.commit()
    con.close()


#Sistema eConnect: 
inicializador_bd()
opcao_menu = 1
opcao_cliente = 0
opcao_plano = 0

while(opcao_menu!=3):
    menu_1()
    opcao_menu = int(input("Selecione a opção desejada: "))
    if (opcao_menu == 1):
        menu_cliente()
        opcao_cliente = int(input("Selecione a opção desejada: "))
        
        if (opcao_cliente==1):
            cadastro_cliente()
            print("")

        elif (opcao_cliente==2):
            listar_cliente()
            print("")

        elif(opcao_cliente==3):
            atualizar_cliente()
            print("")

        elif (opcao_cliente==4):
            remover_cliente()
            print("")

        elif (opcao_cliente==5):
            menu_1()
        else:
            opcao_invalida()
    
    elif (opcao_menu == 2):
        menu_planos()
        opcao_plano = int(input("Selecione a opção desejada: "))
        
        if (opcao_plano==1):
            cadastro_plano()
            print("")

        elif (opcao_plano==2):
            listar_plano()
            print("")

        elif(opcao_plano==3):
            atualizar_plano()
            print("")

        elif (opcao_plano==4):
            remover_plano()
            print("")

        elif (opcao_plano==5):
            menu_1()

        else:
            opcao_invalida()

    if (opcao_menu==3):
        exit()    
      

