from biblioteca.trat_erros import *
import os
import platform

def cabeçalho(txt):
    print("-=" * 20)
    print(txt.center(40))
    print("-=" * 20)

def incluir(op):
    lista = ["estudante", "professor", "disciplina", "turma", "matrícula"]    
    cabeçalho(f"INCLUIR {lista[op-1]}")

def listar(op):
    lista = ["estudante", "professor", "disciplina", "turma", "matrícula"]    
    cabeçalho(f"LISTAR {lista[op-1]}")

def atualizar(op):
    lista = ["estudante", "professor", "disciplina", "turma", "matrícula"]    
    cabeçalho(f"ATUALIZAR {lista[op-1]}")

def excluir(op):
    lista = ["estudante", "professor", "disciplina", "turma", "matrícula"]    
    cabeçalho(f"EXLUIR {lista[op-1]}")


def menuPrincipal(lista):
    cabeçalho("MENU PRINCIPAL")
    for p, v in enumerate(lista):
        print(f"{p+1:0>2} - {v}")
    print("--" * 20)
    op = leiaInt("Opção: ")
    if op > 0 and op <= len(lista):
        return op
    else:
        while True:
            print("\033[35mOpção inválida!!!\033[m")
            op = leiaInt("Opção: ")
            if op > 0 and op <= len(lista):
                return op

def menuOp(n):
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

    lista = ["Incluir", "Listar", "Atualizar", "Excluir", "Voltar ao menu principal"]
    
    for p, v in enumerate(lista):
        print(f"{p+1:0>2} - {v}")
    print("--" * 20)
    op = leiaInt("Opção: ")
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
            op = leiaInt("Opção: ")
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

def limpar_prompt():
    try:
        sistema_operacional = platform.system()
        if sistema_operacional == "Windows":
            os.system('cls')
        elif sistema_operacional in ["Linux", "Darwin"]:  # Darwin é o nome do sistema para macOS
            os.system('clear')
        else:
            raise NotImplementedError(f"Sistema operacional '{sistema_operacional}' não suportado.")
    except Exception as e:
        print(f"Erro ao tentar limpar o prompt: {e}")