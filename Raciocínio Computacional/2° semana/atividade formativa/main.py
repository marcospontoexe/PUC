#pacote (biblioteca) é a junção de vários módulos

from biblioteca.interface import *   #importa todos as funções do módulo interface, do pacote biblioteca
from biblioteca.trat_erros import *
from biblioteca.arquivo import *
import os   #usado para limpar o prompt de comando


arq = "dados.txt"
if not arquivoExiste(arq):  #função do módulo arquivo
    criarArquivo(arq)       #função do módulo arquivo


while True:

    opção = menuPrincipal(["Gerenciar estudantes", "Gerenciar professores", "Gerenciar disciplinas", "Gerenciar turmas", "Gerenciar matrículas", "Sair"])
    limpar_prompt()
    
    if opção == 6:
        cabeçalho("Saindo... Até logo!")
        break

    menuOp(opção)
    #limpar_prompt()