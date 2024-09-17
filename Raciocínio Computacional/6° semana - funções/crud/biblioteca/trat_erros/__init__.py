

def leiaInt(i):
    """
    Essa função pede para o usuário digitar um número inteiro, saindo da função apenas quando a condição for fatisfeita.
    :param i: String usada para solicitar um valor ao usuário
    :param temp: Int
    """
    while True:
        try:
            while True:
                temp = int(input(i))
                if temp >=0:
                    break
                else:
                    print("Digite uma número maior doque zero!")

        except (TypeError, ValueError):
            print("\033[34mERRO. Apenas número inteiro!\033[m")
            continue
        except (KeyboardInterrupt):
            print("Programa interrompido pelo usuário.")
        else:
            return temp



def leiaString(n):
    """
    Essa função pede para o usuário digitar uma String, saindo da função apenas quando a condição for fatisfeita.
    :param n: String usada para solicitar um valor ao usuário
    :param temp: String
    """
    while True:
        temp = input(n).strip()
        if temp == "" or temp.isalpha() == False:
            print("\033[34mERRO! Escreva algum nome.\033[m")
        else:
            return temp
