from biblioteca.trat_erros import *
import os
import platform

estudante = []

def cabeçalho(txt):
    print("-=" * 20)
    print(txt.center(40))
    print("-=" * 20)

def incluir(op):
    if op.upper().strip() == "ESTUDANTES":
        estudante.append(input("Digite o nome: "))
    else:
        print("Em desenvolvimento!")
        

def listar(op):
    if len(estudante) == 0:
        print("Não há estudantes cadastrados!")
    else:
        for nome in estudante:
            print(f"Estudante: {nome}")
    


def menuPrincipal(lista):
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
    '''
    op = leiaInt("Informe a opção desejada: ")
    if op > 0 and op <= len(lista):
        return op
    else:
        while True:
            print("\033[35mOpção inválida!!!\033[m")
            op = leiaInt("Informe a opção desejada: ")
            if op > 0 and op <= len(lista):
                return op
    '''
  
    
    

def menuOp(n, lista_opt):
    strAux = f"[{n}] menu de operações".upper()
    cabeçalho(strAux)
    '''
    if n == 1:       
        cabeçalho("[ESTUDANTES] MENU DE OPERAÇÕES")
    elif n == 2:
        cabeçalho("[PROFESSORES] MENU DE OPERAÇÕES")
    elif n == 3:
        cabeçalho("[DISCIPLINAS] MENU DE OPERAÇÕES")
    elif n == 4:
        cabeçalho("[TURMAS] MENU DE OPERAÇÕES")
    elif n == 5:
        cabeçalho("[MATRÍCULAS] MENU DE OPERAÇÕES")
    '''
        
    for p, v in enumerate(lista_opt):
        print(f"{p+1:0>2} - {v}")
    print("--" * 20)
    while True:
        op = leiaInt("Informe a opção desejada: ")
        if op > 0 and op <= len(lista_opt):
            if op == 1:
                incluir(n)
            elif op == 2:
                listar(n)
            elif op == 3:
                print("Em desenvolvimento!")
            elif op == 4:
                print("Em desenvolvimento!")
            elif op == 5:    
                break
        else:
            print("\033[35mOpção inválida!!!\033[m")
    #limpar_prompt()
    '''
    op = leiaInt("Informe a opção desejada: ")
    limpar_prompt()
    if op > 0 and op <= len(lista):
        if op == 1:
            incluir(n)
        elif op == 2:
            listar(n)
        elif op == 3:
            atualizar(n)
        elif op == 4:
            excluir(n)
        elif op == 6:
            return
    else:
        while True:
            print("\033[35mOpção inválida!!!\033[m")
            op = leiaInt("Informe a opção desejada: ")
            if op > 0 and op <= len(lista):
                if op == 1:
                    incluir(n)
                elif op == 2:
                    listar(n)
                elif op == 3:
                    atualizar(n)
                elif op == 4:
                    excluir(n)
                elif op == 6:
                    return
    '''

def limpar_prompt():
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