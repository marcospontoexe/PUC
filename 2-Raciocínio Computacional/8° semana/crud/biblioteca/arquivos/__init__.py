import json # para manipular arquivos .json
import os

def criarJson(arquivo, nomeArquivo, nomeDiretorio):
    """
    Essa função cria um arquivo json
    
    :param arquivo: Lista contendo os dados a serem gravados no arquivo json
    :param nomeArquivo: String contendo o nome do arquivo json a ser criado
    :param nomeDiretorio: String contendo o diretório do arquivo json
    """
    # Caminho do subdiretório e arquivo
    subdiretorio = os.path.join(nomeDiretorio)  # Usa o separador correto para o SO
    arquivo_json = os.path.join(subdiretorio, nomeArquivo + '.json')

    # Verifica se o subdiretório existe, se não, cria-o
    if not os.path.exists(subdiretorio):
        os.makedirs(subdiretorio)

    try:
        with open(arquivo_json, 'w', encoding="utf-8") as dadosJson: # abre um arquivo json no modo escrita, com possibilidade de uso de caracteres especiais (UTF-8)
            json.dump(arquivo, dadosJson, indent=4, ensure_ascii=False)   # escreve no modo apend, o conteudo de "arquivo" no json arbeto (dadosJson), e permite a codificação correta de caracteres não-ASCII
            dadosJson.close()   # fecha o arquivo "dadosJson"
    except (IOError, FileNotFoundError): # erro durante a leitura ou gravação de um arquivo.
        print(f"Erro ao tentar salvar o arquivo {nomeArquivo}.json!")
    finally:
        print(f"{nomeArquivo}.json salvo com sucesso!")
         

def abrirJson(nomeArquivo, nomeDiretorio):
    """
    Essa função aber um arquivo json
    
    :param nomeArquivo: String contendo o nome do arquivo json a ser aberto
    :param nomeDiretorio: String contendo o diretório do arquivo json
    :return: Dicionário com os dados do arquivo json aberto
    """
    # Caminho do subdiretório e arquivo
    subdiretorio = os.path.join(nomeDiretorio)  # Usa o separador correto para o SO
    arquivo_json = os.path.join(subdiretorio, nomeArquivo + '.json')

    dados = []  
    try:    # tenta usar  "with open"
        with open(arquivo_json, 'r', encoding='utf-8') as dadosJson: # abre um arquivo json em modo de leitura. encoding="utf-8" para usar caracteres especiais
            dados = json.load(dadosJson)    # "dados" recebe o conteúdo do arquivo JSON
            dadosJson.close()   # fecha o arquivo "dadosJson" 
            return dados
    except (IOError, FileNotFoundError):
        print(f"{nomeArquivo}.json não encontrado!")
        return dados
    else:
        print(f"{nomeArquivo}.json aberto com sucesso!")