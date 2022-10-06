import sqlite3
import random
from colorama import Fore, Back, Style
from time import sleep
import time

normal = Fore.RESET


class Roleta():
    valor = 0
    apostar = []
    def __init__(self, jogador:str, carteira:int):
        self.jogador = jogador
        self.cartera = carteira
    def mesa(self):
        a = Back.RED
        b = Back.BLACK
        no = Back.RESET
        letraPreta = Fore.RESET
        verde = Back.LIGHTGREEN_EX
        preto = Fore.BLACK
        print(" ___________________________________________________________________________________________"
              "\n|"+verde+"   "+no+"|"
              ,a,"3",no,
                 "|"
              ,b,"6",no,
                 "|"
              ,a,"9",no,
                 "|"
               ,a,"12",no,
                 "|"
              ,b,"15",no,
                 "|"
              ,a,"18",no,
                 "|"
              ,a,"21",no,
                 "|"
              ,b,"24",no,
                 "|"
              ,a,"27",no,
                 "|"
              ,a,"30",no,
                 "|"
              ,b,"33",no,
                 "|"
              ,a,"36",no,
                 "|"+verde+preto+" 2to1 "+no+letraPreta+"|"
              "\n|"+verde+preto+" 0 "+no+letraPreta+"|"
              ,b,"2",no,
                 "|"
              ,a,"5",no,
                 "|"
              ,b,"8",no,
                 "|"
              ,b,"11",no,
                 "|"
              ,a,"14",no,
                 "|"
              ,b,"17",no,
                 "|"
              ,b,"20",no,
                 "|"
              ,a,"23",no,
                 "|"
              ,b,"26",no,
                 "|"
              ,b,"29",no,
                 "|"
              ,a,"32",no,
                 "|"
              ,b,"35",no,
                 "|"+verde+preto+" 2to1 "+no+letraPreta+"|"
              "\n|"+verde+"   "+no+"|"
              ,a,"1",no,
                 "|"
              ,b,"4",no,
                 "|"
              ,a,"7",no,
                 "|"
              ,b,"10",no,
                 "|"
              ,b,"13",no,
                 "|"
              ,a,"16",no,
                 "|"
              ,a,"19",no,
                 "|"
              ,b,"22",no,
                 "|"
              ,a,"25",no,
                 "|"
              ,b,"28",no,
                 "|"
              ,b,"31",no,
                 "|"
              ,a,"34",no,
                "|"+verde+preto+" 2to1 "+no+letraPreta+"|"
              "\n -------------------------------------------------------------------------------------------"
              "\n    |"+verde+preto+"         1st 12         "+no+letraPreta+"|"+verde+preto+"           2nd 12          "+no+letraPreta+"|"+verde+preto+"          3rd 12           "+no+letraPreta+"|"
              "\n     ------------------------------------------------------------------------------- ",no,letraPreta,
              "\n    |"+verde+preto+"   1 - 18  "+no+letraPreta+"|"+verde+preto+"    EVEN    "+no+letraPreta+"|"+verde+preto+"     RED     "+no+letraPreta+"|"+verde+preto+"    BLACK    "+no+letraPreta+"|"+verde+preto+"     Odd     "+no+letraPreta+"|"+verde+preto+"   19 - 36   "+no+letraPreta+"|"
              "\n     --------------------------------------------------------------------------------")

    def inicio(self, primeiro:int=1):
        print(f"Olá Jogador {self.jogador} e bem-vindo ao Jogo da Roleta"
              f"\nPara começar a jogar, primeiro escolha a sua cor:")
        sleep(0.5)
        print("[1]-Verde"
              "\n[2]-Vermelho"
              "\n[3]-Azul"
              "\n[4]-Amarelo"
              "\n[5]-Cinza"
              "\n[6]-Preto")
        while True:
            #Ver Depois
            escolha = str(input("Digite a cor da sua escolha aqui: "))
            try:
                global cor
                x = print("Cor escolhida")
                if escolha == "1" or escolha == "verde":
                    cor = Fore.GREEN
                    x
                    break
                elif escolha == "2" or escolha == "vermelho":
                    cor = Fore.RED
                    x
                    break
                elif escolha == "3" or escolha == "azul":
                    cor = Fore.BLUE
                    x
                    break
                elif escolha == "4" or escolha == "amarelo":
                    cor = Fore.YELLOW
                    x
                    break
                elif escolha == "5" or escolha == "cinza":
                    cor = Fore.CYAN
                    x
                    break
                elif escolha == "6" or escolha == "Preto":
                    cor = Fore.BLACK
                    x
                    break
                else:
                    print("Nenhuma cor foi escolhida, Digite um valor valido")
            except Exception is SyntaxError:
                print()
    def multiplicadores(self):
        multiplicadores = [50, 100, 500]
        self.valor_amplificador1 = 1
        self.valor_amplificador2 = 1
        self.valor_amplificador3 = 1
        self.valor_amplificador4 = 1
        self.lugar_aplificador1 = 0
        self.lugar_aplificador2 = 0
        self.lugar_aplificador3 = 0
        self.lugar_aplificador4 = 0
        qtda_amplificador = random.randint(1, 4)
        if qtda_amplificador == 1:
            self.valor_amplificador1 = random.choice(multiplicadores)
            self.lugar_aplificador1 = random.randint(0, 36)
            print(
                Fore.LIGHTMAGENTA_EX + f"\nHá um numero amplificado em {self.valor_amplificador1}x na casa {self.lugar_aplificador1}" + normal)
        elif qtda_amplificador == 2:
            self.valor_amplificador1 = random.choice(multiplicadores)
            self.lugar_aplificador1 = random.randint(0, 36)
            self.valor_amplificador2 = random.choice(multiplicadores)
            self.lugar_aplificador2 = random.randint(0, 36)
            print(
                Fore.LIGHTMAGENTA_EX + f"Há um numero amplificado em {self.valor_amplificador1}x na casa {self.lugar_aplificador1}" + normal)
            print(
                Fore.GREEN + f"Há um numero amplificado em {self.valor_amplificador2}x na casa {self.lugar_aplificador2}" + normal)
        elif qtda_amplificador == 3:
            self.valor_amplificador1 = random.choice(multiplicadores)
            self.lugar_aplificador1 = random.randint(0, 36)
            self.valor_amplificador2 = random.choice(multiplicadores)
            self.lugar_aplificador2 = random.randint(0, 36)
            self.valor_amplificador3 = random.choice(multiplicadores)
            self.lugar_aplificador3 = random.randint(0, 36)
            print(
                Fore.LIGHTMAGENTA_EX + f"Há um numero amplificado em {self.valor_amplificador1}x na casa {self.lugar_aplificador1}" + normal)
            print(
                Fore.GREEN + f"Há um numero amplificado em {self.valor_amplificador2}x na casa {self.lugar_aplificador2}" + normal)
            print(
                Fore.LIGHTYELLOW_EX + f"Há um numero amplificado em {self.valor_amplificador3}x na casa {self.lugar_aplificador3}" + normal)
        elif qtda_amplificador == 4:
            self.valor_amplificador1 = random.choice(multiplicadores)
            self.lugar_aplificador1 = random.randint(0, 36)
            self.valor_amplificador2 = random.choice(multiplicadores)
            self.lugar_aplificador2 = random.randint(0, 36)
            self.valor_amplificador3 = random.choice(multiplicadores)
            self.lugar_aplificador3 = random.randint(0, 36)
            self.valor_amplificador4 = random.choice(multiplicadores)
            self.lugar_aplificador4 = random.randint(0, 36)
            print(
                Fore.LIGHTMAGENTA_EX + f"Há um numero amplificado em {self.valor_amplificador1}x na casa {self.lugar_aplificador1}" + normal)
            print(
                Fore.GREEN + f"Há um numero amplificado em {self.valor_amplificador2}x na casa {self.lugar_aplificador2}" + normal)
            print(
                Fore.LIGHTYELLOW_EX + f"Há um numero amplificado em {self.valor_amplificador3}x na casa {self.lugar_aplificador3}" + normal)
            print(
                Fore.CYAN + f"Há um numero amplificado em {self.valor_amplificador4}x na casa {self.lugar_aplificador4}" + normal)
        else:
            print("\nNão há nenhum numero Amplificado")

    def jogo(self, valorFicha):
        tentativa = 0
        tamanho = 0
        true = True
        while true:
            print("\nDeseja fazer que tipo(s) de aposta"
                  "\n[1]-Interna"
                  "\n[2]-Externa"
                  "\n[3]-Encerrar Apostas"
                  "\n[4]-Sair do Cassino")
            jogada = str(input("\nDigite uma opção: "))
            try:
                jogada = int(jogada)
            except:
                print("Valor Invalido favor digitar novamente")
            else:
                true = False
        #Aposta Interna
        if jogada == 1:
            self.multiplicadores()
            tentativa = 0
            quantidade = 0
            aq = 0
            c = 0
            while True:
                print(f"\nDigite em quantas casas deseja apostar")
                try:
                    quantidade = int(input("Digite aqui um valor maior ou igual a zero e menor que 36: "))
                    if 0 > quantidade or quantidade > 36:
                        print("Valor Muito Alto/Baixo, Favor Digitar Novamente")
                    else:
                        break
                except:
                    print("Houve um erro, favor digitar novamente")
            while c < quantidade:
                print("\nDigite a casa(s) que deseja de 0-36")
                casa = int(input("Casa nº: "))
                if tentativa == 0:
                    if casa > 36 or casa < 0:
                        print(Fore.RED+"\nValor muito alto ou muito baixo, favor digitar o valor Corretamente"+normal)
                        continue
                    self.apostar.append(casa)
                    tentativa += 1
                    c += 1
                elif tentativa == 1:
                    if casa > 36 or casa < 0:
                        print(Fore.RED+"Valor muito alto ou muito baixo, favor digitar o valor Corretamente"+normal)
                        continue
                    aq = 0
                    for indice in range(0, len(self.apostar)):
                        if self.apostar[indice] == casa:
                            print(f"Valor Já existe, favor digitar novamente um valor valido")
                            aq += 1
                            break
                    if aq == 0:
                        self.apostar.append(casa)
                        c += 1
                    elif aq >= 1:
                        continue
            randomizador = random.randint(0, 36)
            perdeu = 0
            for i in range(0, len(self.apostar)):
                if self.lugar_aplificador1 == self.apostar[i] and self.apostar[i] == randomizador:
                    print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * self.valor_amplificador1} com um amplificador de {self.valor_amplificador1}x")
                    perdeu += 1
                elif self.lugar_aplificador2 == self.apostar[i] and self.apostar[i] == randomizador:
                    print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * self.valor_amplificador2} com um amplificador de {self.valor_amplificador2}x")
                    perdeu += 1
                elif self.lugar_aplificador3 == self.apostar[i] and self.apostar[i] == randomizador:
                    print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * self.valor_amplificador3} com um amplificador de {self.valor_amplificador3}x")
                    perdeu += 1
                elif self.lugar_aplificador4 == self.apostar[i] and self.apostar[i] == randomizador:
                    print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * self.valor_amplificador4} com um amplificador de {self.valor_amplificador4}x")
                    perdeu += 1
                elif self.apostar[i] == randomizador:
                    print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * (36 / quantidade)}")
                    perdeu += 1
            if perdeu == 0:
                print("\nVocê Perdeu")


        elif jogada == 2:
            qtd_colunas = 0
            achado = 0
            c = 0
            print("\nQual a jogada externa deseja fazer"
                  "\n[1]-Colunas"
                  "\n[2]-Duzias"
                  "\n[3]-Cor"
                  "\n[4]-Par/Impar"
                  "\n[5]-1-18/19-36")
            while True:
                responda = str(input("\nDigite aqui: "))
                try:
                    responda = int(responda)
                except:
                    print("Digite um valor válido")
                else:
                    break
            #AQUI EU ACHO QUE SÓ PODE UMA COLUNA
            if responda == '1' or responda == "Colunas":
                colunas = [[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36], [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
                           [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]]
                verdade = True
                self.mesa()
                while verdade:
                    print(f"\nQual Coluna Você deseja?"
                          f"\nDigite "
                          f"\n[1]-Para a Primeira Coluna (3,6...)"
                          f"\n[2]-Para a Segunda Coluna (2,5...)"
                          f"\n[3]-Para a Terceira Coluna (1,4...)")
                    try:
                        digite = int(input("\nEscolha a sua coluna: "))
                        if digite > 3 or digite <= 0:
                            continue
                    except:
                        print("\nErro, Digite o valor novamente")
                        continue
                    else:
                        verdade = False
                    digite -= 1
                randomizador = random.randint(0, 36)
                perdeu = 0
                print(f"O numero sorteado foi o {randomizador}")
                for l in range(0, 12):
                    if colunas[digite][l] == randomizador:
                        print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * 2}")
                        perdeu += 1
                        break
                if perdeu == 0:
                    print(f"Você Perdeu, o dinheiro que você perdeu nessa aposta foi de R${valorFicha}")


            elif responda == '2' or responda == 'Duzias':
                duzia_digitada = 0
                duzia = [[1,2,3,4,5,6,7,8,9,10,11,12], [13,14,15,16,17,18,19,20,21,22,23,24], [25,26,27,28,29,30,31,32,33,34,35,36]]
                verdade = True
                self.mesa()
                while verdade:
                    print(f"\nQual Duzia Você deseja?"
                          f"\nDigite "
                          f"\n[1]-Para a Primeira Duzia"
                          f"\n[2]-Para a Segunda Duzia"
                          f"\n[3]-Para a Terceira Duzia")
                    try:
                        digite = int(input("\nEscolha a sua duzia: "))
                        if digite > 3 or digite <= 0:
                            continue
                    except:
                        print("\nErro, Digite o valor novamente")
                        continue
                    else:
                        verdade = False
                    digite -= 1
                randomizador = random.randint(0, 36)
                perdeu = 0
                print(f"O numero sorteado foi o {randomizador}")
                for l in range(0, 12):
                    if duzia[digite][l] == randomizador:
                        print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * 2}")
                        perdeu += 1
                        break
                if perdeu == 0:
                    print(f"Você Perdeu, o dinheiro que você perdeu nessa aposta foi de R${valorFicha}")

            elif responda == "3" or responda == "Cor":
                cor = [[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35], [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]]
                verdade = True
                self.mesa()
                while verdade:
                    print(f"\nQual Cor Você deseja?"
                          f"\nDigite "
                          f"\n[1]-Para a Cor Preta"
                          f"\n[2]-Para a Cor Vermelha")
                    try:
                        digite = int(input("\nEscolha a sua cor: "))
                        if digite > 2 or digite <= 0:
                            continue
                    except:
                        print("\nErro, Digite o valor novamente")
                        continue
                    else:
                        verdade = False
                    digite -= 1
                randomizador = random.randint(0, 36)
                perdeu = 0
                print(f"O numero sorteado foi o {randomizador}")
                for l in range(0, 18):
                    if cor[digite][l] == randomizador:
                        print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * 2}")
                        perdeu += 1
                        break
                if perdeu == 0:
                    print(f"Você Perdeu, o dinheiro que você perdeu nessa aposta foi de R${valorFicha}")


            elif responda == "4" or responda == "Par/Impar":
                conjuntos = [[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36],
                       [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]]
                verdade = True
                self.mesa()
                while verdade:
                    print(f"\nQual Escolha Você deseja?"
                          f"\nDigite "
                          f"\n[1]-Para a Par"
                          f"\n[2]-Para a Impar")
                    try:
                        digite = int(input("\nEscolha Par ou Impar: "))
                        if digite > 2 or digite <= 0:
                            continue
                    except:
                        print("\nErro, Digite o valor novamente")
                        continue
                    else:
                        verdade = False
                    digite -= 1
                randomizador = random.randint(0, 36)
                perdeu = 0
                print(f"O numero sorteado foi o {randomizador}")
                for l in range(0, 18):
                    if conjuntos[digite][l] == randomizador:
                        print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * 2}")
                        perdeu += 1
                        break
                if perdeu == 0:
                    print(f"Você Perdeu, o dinheiro que você perdeu nessa aposta foi de R${valorFicha}")


            elif responda == "5" or "1-18/19-36":
                altos = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
                             [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]]
                verdade = True
                self.mesa()
                while verdade:
                    print(f"\nQual Escolha Você deseja?"
                          f"\nDigite "
                          f"\n[1]-Para a Numeros Baixos (1-18)"
                          f"\n[2]-Para a Numeros Altos (19-36)")
                    try:
                        digite = int(input("\nEscolha Alto ou Baixo: "))
                        if digite > 2 or digite <= 0:
                            continue
                    except:
                        print("\nErro, Digite o valor novamente")
                        continue
                    else:
                        verdade = False
                    digite -= 1
                randomizador = random.randint(0, 36)
                perdeu = 0
                print(f"O numero sorteado foi o {randomizador}")
                for l in range(0, 18):
                    if altos[digite][l] == randomizador:
                        print(f"\nPARABENS VOCÊ GANHOU R${valorFicha * 2}")
                        perdeu += 1
                        break
                if perdeu == 0:
                    print(f"Você Perdeu, o dinheiro que você perdeu nessa aposta foi de R${valorFicha}")

        elif jogada == "3":
            print("Obrigado por jogar o nosso jogo")
            print("Tenha um otimo dia")
            quit()





    def fichasEOpcoes(self):
        true = True
        print("\n"+ "-=" * 100)
        print(f"Agora está na hora de apostar, e por isso lhe daremos duas opções a partir daqui:"
              f"\n1-Livro de Regras"
              f"\n2-Jogar")
        while true:
            n = str(input("Qual você escolhe: ")).lower()
            try:
                n = str(n)
            except:
                print("Algo deu errado, favor digitar um numero valido")
            #Regras de Apostas
            if n == "1" or n == "livro de regras":
                print("\nA roleta que é jogada aqui é a roleta europeia, que conta com 37 numeros na roleta."
                      "\n"
                      "\nA roleta na Roleta European contém 37 posições, numeradas de zero a 36. Isso significa que os jogadores são ofertados com melhores \nprobabilidades do que em outras mesas de roleta, como a Americana, que tem mais posições."
                      "\nAs duas principais seções da mesa nas quais as apostas são colocadas são a 'seção interna' e a 'seção externa'. Cada uma com diversas \nformas diferentes para apostar."
                      "\nA seção interna oferece apostas em números individuais que estão próximos um do outro no layout da mesa, ou grupos de até seis números."
                      "\nA seção externa contém pares de apostas para vermelho ou preto, alto ou baixo e par ou ímpar (cada uma cobrindo 18 números). Você também \npode fazer seis diferentes apostas de 12 números (três de cada, conhecidas como apostas de 'Coluna' e 'Dúzia')."
                      "\nAlém disso, existem grupos de apostas que abrangem de sete a 17 números, localizadas em diferentes segmentos da roleta. Estas apostas \npodem ser colocadas com um simples clique na 'racetrack', a parte do layout da mesa de roleta que representa a roleta verdadeira \ne a ordem na qual os números são mostrados, em vez da ordem numérica do layout de apostas principal."
                      "\n"
                      "\nO Jogo e as Regras do Jogo"
                      "\nUma vez que entrar na mesa, cada jogador é solicitado a selecionar uma cor de ficha para utilizar durante a sessão. Você pode então \nselecionar facilmente o valor das fichas ao colocar as apostas, e variar o número colocado de uma vez em uma determinada área de aposta."
                      "\nAcompanhamos automaticamente os valores apostados, e não permitirá que apostas abaixo do limite mínimo da mesa sejam colocadas. Se o \nvalor nominal escolhido for menor do que o mínimo permitido, o seu primeiro clique na área de apostas irá colocar a aposta mínima da mesa."
                      "\nUtilizando apostas internas ou externas, você pode apostar em qualquer número, ou combinação de números. Lembre-se que cada aposta \nexterna deve ser de pelo menos o valor do mínimo da mesa; a mesma regra se aplica ao total apostado nas apostas internas. \nLembre-se também que cada uma é independente da outra em relação ao mínimo da mesa."
                      "\nPara as apostas ganhadoras, a aposta original é retornada para a sua conta, mais o pagamento que você recebe baseado no valor investido \ne as informações das probabilidades (relacionada abaixo). As apostas perdedoras serão perdidas."
                      "\nO software reconhece automaticamente que as apostas internas são acumulativas, assim as apostas podem ser colocadas na seção interna \nda mesa até que o mínimo seja atingido. Caso ele não seja atingido, as apostas abaixo do mínimo serão removidas quando a roleta for girada (depois que o cronômetro de apostas encerrar)."
                      "\nAo jogar em uma mesa de Jogadores Múltiplos, todas as apostas serão elegíveis a ganhar ou perder uma vez que o cronômetro de apostas \nencerrar. Nas mesas de Jogador Único, as apostas não serão consideradas ativas até que a ação seja confirmada e o botão Girar tenha sido clicado."
                      "\n"
                      "\n                 Pagamento das Apostas Internas - Roleta"
                      "\nNome Da Aposta         Números Cobertos           Probabilidade de Pagamento"
                      "\n Pleno                        1                             35 para 1"
                      "\n Dividir                      2                             17 para 1"
                      "\n Linha                        3                             11 para 1"
                      "\n Quadrado                     4                             8 para 1"
                      "\n Linha Dupla                  6                             5 para 1"
                      "\n"
                      "\n                 Pagamento Das Apostas Externas - Roleta"
                      "\nNome Da Aposta         Números Cobertos           Probabilidade de Pagamento"
                      "\n Vermelho                     18                            1 para 1"
                      "\n Preto                        18                            1 para 1"
                      "\n Ímpar                        18                            1 para 1"
                      "\n Par                          18                            1 para 1"
                      "\n Baixo(1-18)                  18                            1 para 1"
                      "\n Alto(19-36                   18                            1 para 1"
                      "\n 1ª, 2ª ou 3ª duzia           12                            2 para 1"
                      "\n 1ª, 2ª ou 3ª coluna          12                            2 para 1"
                      "\n"
                      "\nApostas Divididas e Racetrack"
                      "\nAlém das seções Interna e Externa, as apostas também podem ser colocadas na área 'racetrack' da mesa. Esta seção do layout da mesa de \nroleta representa a ordem real que os números aparecem na própria roleta. Clique em um dos números para colocar fichas nele, \nmais os dois números adjacentes (conhecidos como 'vizinhos') dos dois lados deste número."
                      "\nA 'racetrack' pode ser utilizada para colocar outras quatro apostas especiais, cada qual coloca automaticamente várias fichas no layout,\n como mostrado na tabela a seguir."
                      "\n"
                      "\nNome Da Aposta         Custo Da Ficha          Números Cobertos                              Distribuição"
                      "\n Vizinhos do Zero       Nove Fichas                   17                              0/2/3 (duas fichas), 4/7, 12/15, 18/21, 19/22, 25/26/28/29 (duas fichas), 32/35"
                      "\n Terço da Roleta        Seis Fichas                   12                              5/8, 10/11, 13/16, 23/24, 27/30, 33/36"
                      "\n Orphelins en Plein     Oito Fichas                   8                               1, 6, 9, 14, 17, 20, 31, 34"
                      "\n Zero                   Quatro Fichas                 7                               0/3, 12/15, 26, 32/35"
                      "\n"
                      "\nApostas em dois números adjacentes (divididos) da mesma cor no layout principal (ex. vermelho ou preto) podem ser apostadas em uma ação\n utilizando os controles para apostas divididas encontrados perto da área 'racetrack' da mesa."
                      "\n"
                      "\nDivididos Vermelhos(Quatro Apostas)                   Divididos Pretos(Sete Apostas)"
                      "\n 9/12                                                          8/11"
                      "\n 16/19                                                         10/11"
                      "\n 18/21                                                         10/13"
                      "\n 27/30                                                         17/20"
                      "\n                                                               26/29"
                      "\n                                                               28/29"
                      "\n                                                               28/31"
                      "\n"
                      "\nLimites De Apostas"
                      "\nSeguindo uma convenção semelhante à maioria dos cassinos modernos em todo o mundo, os limites de apostas nas mesas de roleta variam, \ndependendo se elas cobrem as apostas internas ou externas."
                      "\nA aposta externa máxima exibida em cada mesa indica o maior valor que pode ser colocado em cada (ou todas) as posições de apostas externas. Não existe um máximo acumulativo."
                      "\nA aposta interna máxima de uma mesa se refere ao valor permitido para ser colocado em cada aposta de número individual (ou direta)."
                      "\nTodos os outros tipos de apostas internas (por exemplo a dividida, linha dupla, linha, etc.) têm o seu próprio valor máximo de aposta, \nrelativo ao máximo do direto da mesa. A regra geral é que quanto mais números forem cobertos por uma aposta, maiores serão os limites. \nPor exemplo, uma aposta Pleno cobre um número e a aposta máxima pode ser de 25 fichas. Uma aposta Dividida cobre dois números e assim o dobro do máximo é permitido (50 fichas). \nUma aposta de Linha cobre três números e neste exemplo a aposta máxima seria de 75 fichas, e assim por diante."
                      "\nEm uma mesa com um limite de aposta máxima no pleno de 25 fichas, é possível colocar até 40 apostas de 25 fichas em torno de um número \nposicionado na coluna do meio do layout, como o 17 (apostas em um pleno (1), quatro divididos (8), uma linha (3), quatro quadrados (16), e duas linhas duplas (12), para um total de 1.000 fichas."
                      "\n"
                      "\nVantagem Da Casa"
                      "\nOs jogos de Roleta têm uma vantagem da casa (calculada como a diferença entre as probabilidades reais e as probabilidades de pagamento) de 2,70%."
                      "\nOs jogos de American Roulette têm uma vantagem da casa de 5,26%. A aposta Five Line na American Roulette tem uma vantagem da casa de 7,89%."
                      "\n"
                      "\nApostas Salvas"
                      "\nEm mesas de Jogador Único, é possível salvar suas apostas favoritas, então você pode fazer apostas de combinação específica de forma rápida e conveniente. \nSelecione ‘Salvar Aposta Atual’ para adicioná-la aos seus favoritos. Você pode gerenciar apostas salvas no menu ‘Minhas Apostas’."
                      "\n"
                      "\nMesas De Jogadores Múltiplos"
                      "\nAs Mesas de Jogadores Múltiplos oferecem a você e seus amigos a oportunidade de jogarem juntos e aproveitar a emoção de um jogo social. Exatamente como nos cassinos da vida real, \nas mesas de Jogadores Múltiplos transformam o jogo online em uma experiência interativa divertida.")
            elif n == "2" or n == "jogar":
                jogo.mesa()
                sleep(1.5)
                while true:
                    print(f"\nEscolha a sua ficha"
                          f"\n[1]-R$0.5"
                          f"\n[2]-R$2.5"
                          f"\n[3]-R$5"
                          f"\n[4]-R$25"
                          f"\n[5]-R$100"
                          f"\n[6]-R$500"
                          f"\n[7]-R$2K"
                          f"\n[8]-R$5K")
                    fichas = int(input("\nDigite: "))
                    try:
                        n = int(n)
                    except:
                        print(f"Algo deu errado, Digite novamente")
                    if fichas == 1:
                        self.valor = 0.5
                        self.jogo(self.valor)
                    elif fichas == 2:
                        self.valor = 2.5
                        self.jogo(self.valor)
                    elif fichas == 3:
                        self.valor = 5
                        self.jogo(self.valor)
                    elif fichas == 4:
                        self.valor = 25
                        self.jogo(self.valor)
                    elif fichas == 5:
                        self.valor = 100
                        self.jogo(self.valor)
                    elif fichas == 6:
                        self.valor = 500
                        self.jogo(self.valor)
                    elif fichas == 7:
                        self.valor = 2000
                        self.jogo(self.valor)
                    elif fichas == 8:
                        self.valor = 5000
                        self.jogo(self.valor)
            else:
                print(f"Digite um valor válido")
global cor
jogo = Roleta("Nícolas", 2000)
#jogo.mesa()
#jogo.inicio()
jogo.fichasEOpcoes()
