from biblioteca.trat_erros import *
from biblioteca.arquivos import *   #importa todos as funções do módulo arquivos, do pacote biblioteca
import os
import platform

diretorioDados = "banco de dados"


def cabeçalho(txt):
    """
    Essa função imprime na tela um cabeçalho

    :param txt: String que para ser impressa como cabeçalho
    """
    print("-=" * 20)
    print(txt.center(40))
    print("-=" * 20)

def incluir(op):
    """
    Essa função inclui novos valores no banco da dados

    :param op: String relacionada à opção que será inclusa no banco de dados
    """
    dados = {}
    dadosExistente = False
    if op == "estudantes":
        dados["código"] = leiaInt("Digite o código do estudante: ")
        alunos = abrirJson("estudantes", diretorioDados)
        #verifica se o código já existe
        if len(alunos) > 0:
            for i, aluno in enumerate(alunos):  # percorre cada dicionário na lista
                if aluno.get('código') == dados["código"]:
                    dadosExistente = True
                    break 
        if dadosExistente:
            print(f"Código {dados["código"]} já existe!")
        else:
            dados["nome"] = leiaString("Digite o nome do estudante: ")
            dados["cpf"] = str(leiaInt("Digite o CPF do estudante: "))
            limpar_prompt()
            alunos.append(dados.copy()) 
            criarJson(alunos, "estudantes", diretorioDados)
            #limpar_prompt()

    elif op == "professores":
        dados["código"] = leiaInt("Digite o código do professor: ")
        docentes = abrirJson("professores", diretorioDados)
        #verifica se o código já existe
        if len(docentes) > 0:
            for i, profs in enumerate(docentes):  # percorre cada dicionário na lista
                if profs.get('código') == dados["código"]:
                    dadosExistente = True
                    break 
        if dadosExistente:
            print(f"Código {dados["código"]} já existe!")
        else:
            dados["nome"] = leiaString("Digite o nome do professor: ")
            dados["cpf"] = str(leiaInt("Digite o CPF do professor: "))
            limpar_prompt()
            docentes.append(dados.copy()) 
            criarJson(docentes, "professores", diretorioDados)
            #limpar_prompt()
        
    # elif op == "disciplinas":
        
    # elif op == "turmas":
    
    # else op == "matrículas":
       
    return None

def listar(op):
    """
    Essa função lista os valores do banco da dados

    :param op: String relacionada à opção que será listada
    """
    if op == "estudantes":
        alunos = abrirJson("estudantes", diretorioDados)
        if len(alunos) == 0: # o banco de dados estaja sem cadastros
            print("Não há estudantes cadastrados!")
        else:
            print("Estudantes cadastrados:".center(50))
            print("-"*58)
            # print(f"|CÓDIGO{'':^12}", end='|')
            print("|"+"CÓDIGO".center(12), end='|')
            print("NOME".center(30), end='|')
            print("CPF".center(12)+"|")
            # print(f"CPF{'':^12}|")
            
            print("-"*58)
            # for e in alunos: # percorre cada índice da lista
            #     for k, v in e.items():  # percorre cada índice do dicionário
            #         print(f"{k:<7}: {v:->30}", end=' | ')
            #     print("") 
            
            for i, aluno in enumerate(alunos):  # percorre cada dicionário na lista
                print(f"|{aluno.get('código'):^12}", end='|') 
                print(f" {aluno.get('nome'):-<29}", end='|')
                print(f" {aluno.get('cpf'):<11}|")

    elif op == "professores":
        docentes = abrirJson("professores", diretorioDados)
        if len(docentes) == 0: # o banco de dados estaja sem cadastros
            print("Não há professores cadastrados!")
        else:
            print("Professores cadastrados:".center(50))
            print("-"*58)
            # print(f"|CÓDIGO{'':^12}", end='|')
            print("|"+"CÓDIGO".center(12), end='|')
            print("NOME".center(30), end='|')
            print("CPF".center(12)+"|")
            # print(f"CPF{'':^12}|")
            
            print("-"*58)
            # for e in alunos: # percorre cada índice da lista
            #     for k, v in e.items():  # percorre cada índice do dicionário
            #         print(f"{k:<7}: {v:->30}", end=' | ')
            #     print("") 
            
            for i, prof in enumerate(docentes):  # percorre cada dicionário na lista
                print(f"|{prof.get('código'):^12}", end='|') 
                print(f" {prof.get('nome'):-<29}", end='|')
                print(f" {prof.get('cpf'):<11}|")

    return None          

def atualizar(op):
    """
    Essa função atualiza os valores do banco da dados

    :param op: String relacionada à opção que será atualizada
    """
    dados = {}
    if op == "estudantes":
        alunos = abrirJson("estudantes", diretorioDados)
        if len(alunos) == 0: # o banco de dados estaja sem cadastros
            print("Não há estudantes para atualizar!")
        else:
            atualiza = leiaInt("Digite o código do estudante a ser atualizado: ")
            for i, aluno in enumerate(alunos):  # percorre cada dicionário na lista
                if aluno.get('código') == atualiza:
                    alunos.pop(i)  #apaga o item da posição iterada 
                    #limpar_prompt()
                    dados["código"] = leiaInt("Digite o novo código do estudante: ")
                    dados["nome"] = leiaString("Digite o novo nome do estudante: ")
                    dados["cpf"] = str(leiaInt("Digite o novo CPF do estudante: "))
                    alunos.insert(i, dados) # insere o novo dicionária à lista
                    criarJson(alunos, "estudantes", diretorioDados)
                    print(f"Estudante com o código {atualiza} foi atualizado.")
                    return None  # encerra a função
            else:
                print(f"Estudante com o código {atualiza} não foi encontrado.")
    elif op == "professores":
        docentes = abrirJson("professores", diretorioDados)
        if len(docentes) == 0: # o banco de dados estaja sem cadastros
            print("Não há professores para atualizar!")
        else:
            atualiza = leiaInt("Digite o código do professor a ser atualizado: ")
            for i, prof in enumerate(docentes):  # percorre cada dicionário na lista
                if prof.get('código') == atualiza:
                    docentes.pop(i)  #apaga o item da posição iterada 
                    dados["código"] = leiaInt("Digite o novo código do professor: ")
                    dados["nome"] = leiaString("Digite o novo nome do professor: ")
                    dados["cpf"] = str(leiaInt("Digite o novo CPF do professor: "))
                    docentes.insert(i, dados) # insere o novo dicionária à lista
                    criarJson(docentes, "professores", diretorioDados)
                    print(f"Professor com o código {atualiza} foi atualizado.")
                    return None  # encerra a função
            else:
                print(f"Professor com o código {atualiza} não foi encontrado.")
    return None
    
def excluir(op):
    """
    Essa função exclui os valores do banco da dados

    :param op: String relacionada à opção que será excluida
    """
    if op == "estudantes":
        alunos = abrirJson("estudantes", diretorioDados)
        if len(alunos) == 0: # o banco de dados estaja sem cadastros
            print("Não há estudantes para excluir!")
        else:
            apagar = leiaInt("Digite o código do estudante a ser excluido: ")
            for i, aluno in enumerate(alunos):  # percorre cada dicionário na lista
                if aluno.get('código') == apagar: 
                    alunos.pop(i)  #apaga o item da posição iterada
                    criarJson(alunos, "estudantes", diretorioDados)
                    print(f"Estudante com o código {apagar} foi excluído.")
                    return None   # encerra a função
            else:
                print(f"Estudante com o código {apagar} não foi encontrado.")
    elif op == "professores":
        docentes = abrirJson("professores", diretorioDados)
        if len(docentes) == 0: # o banco de dados estaja sem cadastros
            print("Não há professores para excluir!")
        else:
            apagar = leiaInt("Digite o código do professor a ser excluido: ")
            for i, prof in enumerate(docentes):  # percorre cada dicionário na lista
                if prof.get('código') == apagar: 
                    docentes.pop(i)  #apaga o item da posição iterada
                    criarJson(docentes, "professores", diretorioDados)
                    print(f"Professor com o código {apagar} foi excluído.")
                    return None   # encerra a função
            else:
                print(f"Professor com o código {apagar} não foi encontrado.")
    return None

def menuPrincipal(lista):
    """
    Essa função cria um menu de opções baseado na lista de entrada

    :param lista: Lista contendo os valores a serem impressos como um menu de opções
    :return: Retorna um int relacionado a opção escolhida a partir da lista de entrada
    """
    cabeçalho("MENU PRINCIPAL")
    for p, v in enumerate(lista):
        print(f"{p+1:0>2} - {v}")
    print("--" * 20)
    while True:
        op = leiaInt("Informe a opção desejada: ")
        if op > 0 and op <= len(lista):
            break
        else:
            print("\033[35mOpção inválida!!!\033[m")
    return op

def menuOp(n, lista_opt):
    """
    Essa função cria um menu de opções baseado em uma string e uma lista de entrada

    :param n: String usada como opção de seleção para o menu de operações
    :param lista_opt: Lista contendo os valores a serem impressos como um menu de opções
    """
    strAux = f"[{n}] menu de operações".upper()
    while True:
        cabeçalho(strAux)
        for p, v in enumerate(lista_opt):
            print(f"{p+1:0>2} - {v}")
        print("--" * 20)
        op = leiaInt("Informe a opção desejada: ")
        #limpar_prompt()
        if op > 0 and op <= len(lista_opt):
            if op == 1:
                incluir(n)
                #limpar_prompt()
            elif op == 2:
                #limpar_prompt()
                listar(n)
            elif op == 3:
                #limpar_prompt()
                atualizar(n)
            elif op == 4:
                #limpar_prompt()
                excluir(n)
            elif op == 5:
                #limpar_prompt()    
                break 
        else:
            print("\033[35mOpção inválida!!!\033[m")

    return None  

def limpar_prompt():
    """
    Essa função limpa a tela
    """
    try:
        sistema_operacional = platform.system()
        if sistema_operacional == "Windows":
            os.system('cls')
        elif sistema_operacional in ["Linux", "Darwin"]:  
            os.system('clear')
        else:
            raise NotImplementedError(f"Sistema operacional '{sistema_operacional}' não suportado.")
    except Exception as e:
        print(f"Erro ao tentar limpar o prompt: {e}")