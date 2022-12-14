import sqlite3
import random
import sys
import CLASS

from colorama import Fore, Back, Style
from time import sleep
import time

normal = Fore.RESET
emailparaacessar = ''

#Implementar o Banco De Dados
#con = sqlite3.connect ('CASSINO (1).db')
#con.execute('PRAGMA foreign_keys = 1')
#cursor = con.cursor()

class Roleta():
    valor = 0
    apostar = []
    def __init__(self, jogador:str, carteira:int, email:str, nomeconexao, variavelConexao, variavelCursor):
        self.jogador = jogador
        self.carteira = carteira
        self.email = email
        self.nomeconexao = nomeconexao
        self.variavelConexao = variavelConexao
        self.variavelCursor = variavelCursor
    def criar(self):
        self.variavelConexao = sqlite3.connect(self.nomeconexao)
        self.variavelConexao.execute("PRAGMA foreign_keys = 1")
        self.variavelCursor = self.variavelConexao.cursor()
        self.variavelCursor.execute('SELECT DINAR FROM CARTEIRA WHERE email=?', (CLASS.emailparamim,))
        for linha in self.variavelCursor.fetchall():
            self.carteira = linha
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
        global cor
        print(f"Ol?? Jogador {self.jogador} e bem-vindo ao Jogo da Roleta"
              f"\nPara come??ar a jogar, primeiro escolha a sua cor:")
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
                if escolha == "1" or escolha == "verde":
                    cor = Fore.GREEN
                    print("Cor escolhida")
                    break
                elif escolha == "2" or escolha == "vermelho":
                    cor = Fore.RED
                    print("Cor escolhida")
                    break
                elif escolha == "3" or escolha == "azul":
                    cor = Fore.BLUE
                    print("Cor escolhida")
                    break
                elif escolha == "4" or escolha == "amarelo":
                    cor = Fore.YELLOW
                    print("Cor escolhida")
                    break
                elif escolha == "5" or escolha == "cinza":
                    cor = Fore.CYAN
                    print("Cor escolhida")
                    break
                elif escolha == "6" or escolha == "Preto":
                    cor = Fore.BLACK
                    print("Cor escolhida")
                    break
                else:
                    print(Fore.RED+"Nenhuma cor foi escolhida, Digite um valor valido"+normal)
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
                Fore.LIGHTMAGENTA_EX + f"\nH?? um numero amplificado em {self.valor_amplificador1}x na casa {self.lugar_aplificador1}" + normal)
        elif qtda_amplificador == 2:
            self.valor_amplificador1 = random.choice(multiplicadores)
            self.lugar_aplificador1 = random.randint(0, 36)
            self.valor_amplificador2 = random.choice(multiplicadores)
            self.lugar_aplificador2 = random.randint(0, 36)
            print(
                Fore.LIGHTMAGENTA_EX + f"H?? um numero amplificado em {self.valor_amplificador1}x na casa {self.lugar_aplificador1}" + normal)
            print(
                Fore.GREEN + f"H?? um numero amplificado em {self.valor_amplificador2}x na casa {self.lugar_aplificador2}" + normal)
        elif qtda_amplificador == 3:
            self.valor_amplificador1 = random.choice(multiplicadores)
            self.lugar_aplificador1 = random.randint(0, 36)
            self.valor_amplificador2 = random.choice(multiplicadores)
            self.lugar_aplificador2 = random.randint(0, 36)
            self.valor_amplificador3 = random.choice(multiplicadores)
            self.lugar_aplificador3 = random.randint(0, 36)
            print(
                Fore.LIGHTMAGENTA_EX + f"H?? um numero amplificado em {self.valor_amplificador1}x na casa {self.lugar_aplificador1}" + normal)
            print(
                Fore.GREEN + f"H?? um numero amplificado em {self.valor_amplificador2}x na casa {self.lugar_aplificador2}" + normal)
            print(
                Fore.LIGHTYELLOW_EX + f"H?? um numero amplificado em {self.valor_amplificador3}x na casa {self.lugar_aplificador3}" + normal)
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
                Fore.LIGHTMAGENTA_EX + f"H?? um numero amplificado em {self.valor_amplificador1}x na casa {self.lugar_aplificador1}" + normal)
            print(
                Fore.GREEN + f"H?? um numero amplificado em {self.valor_amplificador2}x na casa {self.lugar_aplificador2}" + normal)
            print(
                Fore.LIGHTYELLOW_EX + f"H?? um numero amplificado em {self.valor_amplificador3}x na casa {self.lugar_aplificador3}" + normal)
            print(
                Fore.CYAN + f"H?? um numero amplificado em {self.valor_amplificador4}x na casa {self.lugar_aplificador4}" + normal)
        else:
            print("\nN??o h?? nenhum numero Amplificado")

    def jogo(self, valorFicha):
        tentativa = 0
        tamanho = 0
        true = True
        self.criar()
        while true:
            print("\nDeseja fazer que tipo(s) de aposta"
                  "\n[1]-Interna"
                  "\n[2]-Externa"
                  "\n[3]-Encerrar Apostas"
                  "\n[4]-Encerrar Programa")
            jogada = str(input("\nDigite uma op????o: "))
            try:
                jogada = int(jogada)
            except:
                print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
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
                    print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
            while c < quantidade:
                print("\nDigite a casa(s) que deseja de 0-36")
                casa = str(input("Casa n??: "))
                try:
                    casa = int(casa)
                except:
                    print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
                    continue
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
                            print(f"Valor J?? existe, favor digitar novamente um valor valido")
                            aq += 1
                            break
                    if aq == 0:
                        self.apostar.append(casa)
                        c += 1
                    elif aq >= 1:
                        continue
            randomizador = random.randint(0, 36)
            perdeu = 0
            print(self.carteira)
            print(f"O numero sorteado foi o {randomizador}")
            for i in range(0, len(self.apostar)):
                if self.lugar_aplificador1 == self.apostar[i] and self.apostar[i] == randomizador:
                    self.carteira += valorFicha * self.valor_amplificador1
                    print(f"\nPARABENS VOC?? GANHOU R${valorFicha * self.valor_amplificador1} com um amplificador de {self.valor_amplificador1}x")
                    self.variavelCursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email=?', (self.carteira, emailparaacessar))
                    self.variavelConexao.commit()
                    perdeu += 1
                elif self.lugar_aplificador2 == self.apostar[i] and self.apostar[i] == randomizador:
                    self.carteira += valorFicha * self.valor_amplificador2
                    print(f"\nPARABENS VOC?? GANHOU R${valorFicha * self.valor_amplificador2} com um amplificador de {self.valor_amplificador2}x")
                    perdeu += 1
                elif self.lugar_aplificador3 == self.apostar[i] and self.apostar[i] == randomizador:
                    self.carteira += valorFicha * self.valor_amplificador3
                    print(f"\nPARABENS VOC?? GANHOU R${valorFicha * self.valor_amplificador3} com um amplificador de {self.valor_amplificador3}x")
                    perdeu += 1
                elif self.lugar_aplificador4 == self.apostar[i] and self.apostar[i] == randomizador:
                    self.carteira += valorFicha * self.valor_amplificador4
                    print(f"\nPARABENS VOC?? GANHOU R${valorFicha * self.valor_amplificador4} com um amplificador de {self.valor_amplificador4}x")
                    perdeu += 1
                elif self.apostar[i] == randomizador:
                    self.carteira += (valorFicha * (36 / quantidade))
                    print(f"\nPARABENS VOC?? GANHOU R${valorFicha * (36 / quantidade)}")
                    perdeu += 1
            if perdeu == 0:
                print("\nVoc?? Perdeu")


        elif jogada == 2:
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
                    print("Digite um valor v??lido")
                else:
                    break
            if responda == '1' or responda == "Colunas":
                colunas = [[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36], [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
                           [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]]
                verdade = True
                self.mesa()
                while verdade:
                    print(f"\nQual Coluna Voc?? deseja?"
                          f"\nDigite "
                          f"\n[1]-Para a Primeira Coluna (3,6...)"
                          f"\n[2]-Para a Segunda Coluna (2,5...)"
                          f"\n[3]-Para a Terceira Coluna (1,4...)")
                    try:
                        digite = int(input("\nEscolha a sua coluna: "))
                        if digite > 3 or digite <= 0:
                            continue
                    except:
                        print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
                        continue
                    else:
                        verdade = False
                    digite -= 1
                randomizador = random.randint(0, 36)
                perdeu = 0
                print(f"O numero sorteado foi o {randomizador}")
                for l in range(0, 12):
                    if colunas[digite][l] == randomizador:
                        self.carteira += valorFicha * 3
                        print(f"\nPARABENS VOC?? GANHOU R${valorFicha * 3}")
                        perdeu += 1
                        break
                if perdeu == 0:
                    print(f"Voc?? Perdeu, o dinheiro que voc?? perdeu nessa aposta foi de R${valorFicha}")

            elif responda == '2' or responda == 'Duzias':
                duzia = [[1,2,3,4,5,6,7,8,9,10,11,12], [13,14,15,16,17,18,19,20,21,22,23,24], [25,26,27,28,29,30,31,32,33,34,35,36]]
                verdade = True
                self.mesa()
                while verdade:
                    print(f"\nQual Duzia Voc?? deseja?"
                          f"\nDigite "
                          f"\n[1]-Para a Primeira Duzia"
                          f"\n[2]-Para a Segunda Duzia"
                          f"\n[3]-Para a Terceira Duzia")
                    try:
                        digite = int(input("\nEscolha a sua duzia: "))
                        if digite > 3 or digite <= 0:
                            continue
                    except:
                        print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
                        continue
                    else:
                        verdade = False
                    digite -= 1
                randomizador = random.randint(0, 36)
                perdeu = 0
                print(f"O numero sorteado foi o {randomizador}")
                for l in range(0, 12):
                    if duzia[digite][l] == randomizador:
                        self.carteira += valorFicha * 3
                        print(f"\nPARABENS VOC?? GANHOU R${valorFicha * 3}")
                        perdeu += 1
                        break
                if perdeu == 0:
                    print(f"Voc?? Perdeu, o dinheiro que voc?? perdeu nessa aposta foi de R${valorFicha}")

            elif responda == 3:
                cor = [[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35], [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]]
                verdade = True
                self.mesa()
                while verdade:
                    print(f"\nQual Cor Voc?? deseja?"
                          f"\nDigite "
                          f"\n[1]-Para a Cor Preta"
                          f"\n[2]-Para a Cor Vermelha")
                    try:
                        digite = int(input("\nEscolha a sua cor: "))
                        if digite > 2 or digite <= 0:
                            continue
                    except:
                        print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
                        continue
                    else:
                        verdade = False
                    digite -= 1
                randomizador = random.randint(0, 36)
                perdeu = 0
                print(f"O numero sorteado foi o {randomizador}")
                for l in range(0, 18):
                    if cor[digite][l] == randomizador:
                        self.carteira += valorFicha * 2
                        print(f"\nPARABENS VOC?? GANHOU R${valorFicha * 2}")
                        self.variavelCursor.execute('UPDATE CARTEIRA SET DINAR = ? WHERE email=?',(self.carteira, CLASS.emailparamim))
                        self.variavelConexao.commit()
                        perdeu += 1
                        break
                if perdeu == 0:
                    print(f"Voc?? Perdeu, o dinheiro que voc?? perdeu nessa aposta foi de R${valorFicha}")

            elif responda == "4" or responda == "Par/Impar":
                conjuntos = [[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36],
                       [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]]
                verdade = True
                self.mesa()
                while verdade:
                    print(f"\nQual Escolha Voc?? deseja?"
                          f"\nDigite "
                          f"\n[1]-Para a Par"
                          f"\n[2]-Para a Impar")
                    try:
                        digite = int(input("\nEscolha Par ou Impar: "))
                        if digite > 2 or digite <= 0:
                            continue
                    except:
                        print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
                        continue
                    else:
                        verdade = False
                    digite -= 1
                randomizador = random.randint(0, 36)
                perdeu = 0
                print(f"O numero sorteado foi o {randomizador}")
                for l in range(0, 18):
                    if conjuntos[digite][l] == randomizador:
                        self.carteira += valorFicha * 2
                        print(f"\nPARABENS VOC?? GANHOU R${valorFicha * 2}")
                        perdeu += 1
                        break
                if perdeu == 0:
                    print(f"Voc?? Perdeu, o dinheiro que voc?? perdeu nessa aposta foi de R${valorFicha}")

            elif responda == "5" or "1-18/19-36":
                altos = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
                             [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]]
                verdade = True
                self.mesa()
                while verdade:
                    print(f"\nQual Escolha Voc?? deseja?"
                          f"\nDigite "
                          f"\n[1]-Para a Numeros Baixos (1-18)"
                          f"\n[2]-Para a Numeros Altos (19-36)")
                    try:
                        digite = int(input("\nEscolha Alto ou Baixo: "))
                        if digite > 2 or digite <= 0:
                            continue
                    except:
                        print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
                        continue
                    else:
                        verdade = False
                    digite -= 1
                randomizador = random.randint(0, 36)
                perdeu = 0
                print(f"O numero sorteado foi o {randomizador}")
                for l in range(0, 18):
                    if altos[digite][l] == randomizador:
                        self.carteira += valorFicha * 2
                        print(f"\nPARABENS VOC?? GANHOU R${valorFicha * 2}")
                        perdeu += 1
                        break
                if perdeu == 0:
                    print(f"Voc?? Perdeu, o dinheiro que voc?? perdeu nessa aposta foi de R${valorFicha}")

        elif jogada == 3:
            #Voltar para a pagina principal
            quit()
        elif jogada == 4 or "Sair do Cassino":
            print("Obrigado por jogar o nosso jogo")
            print("Tenha um otimo dia")
            quit()





    def fichasEOpcoes(self):
        true = True
        while true:
            print("\n"+ "-=" * 100)
            print(f"Agora est?? na hora de apostar, e por isso lhe daremos duas op????es a partir daqui:"
                  f"\n1-Livro de Regras"
                  f"\n2-Jogar"
                  f"\n3-Encerrar Aposta"
                  f"\n4-Encerrar Programa")
            n = str(input("Qual voc?? escolhe: ")).lower()
            try:
                n = str(n)
            except:
                print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
                continue
            #Regras de Apostas
            if n == "1" or n == "livro de regras":
                print("\nA roleta que ?? jogada aqui ?? a roleta europeia, que conta com 37 numeros na roleta."
                      "\n"
                      "\nA roleta na Roleta European cont??m 37 posi????es, numeradas de zero a 36. Isso significa que os jogadores s??o ofertados com melhores \nprobabilidades do que em outras mesas de roleta, como a Americana, que tem mais posi????es."
                      "\nAs duas principais se????es da mesa nas quais as apostas s??o colocadas s??o a 'se????o interna' e a 'se????o externa'. Cada uma com diversas \nformas diferentes para apostar."
                      "\nA se????o interna oferece apostas em n??meros individuais que est??o pr??ximos um do outro no layout da mesa, ou grupos de at?? seis n??meros."
                      "\nA se????o externa cont??m pares de apostas para vermelho ou preto, alto ou baixo e par ou ??mpar (cada uma cobrindo 18 n??meros). Voc?? tamb??m \npode fazer seis diferentes apostas de 12 n??meros (tr??s de cada, conhecidas como apostas de 'Coluna' e 'D??zia')."
                      "\nAl??m disso, existem grupos de apostas que abrangem de sete a 17 n??meros, localizadas em diferentes segmentos da roleta. Estas apostas \npodem ser colocadas com um simples clique na 'racetrack', a parte do layout da mesa de roleta que representa a roleta verdadeira \ne a ordem na qual os n??meros s??o mostrados, em vez da ordem num??rica do layout de apostas principal."
                      "\n"
                      "\nO Jogo e as Regras do Jogo"
                      "\nUma vez que entrar na mesa, cada jogador ?? solicitado a selecionar uma cor de ficha para utilizar durante a sess??o. Voc?? pode ent??o \nselecionar facilmente o valor das fichas ao colocar as apostas, e variar o n??mero colocado de uma vez em uma determinada ??rea de aposta."
                      "\nAcompanhamos automaticamente os valores apostados, e n??o permitir?? que apostas abaixo do limite m??nimo da mesa sejam colocadas. Se o \nvalor nominal escolhido for menor do que o m??nimo permitido, o seu primeiro clique na ??rea de apostas ir?? colocar a aposta m??nima da mesa."
                      "\nUtilizando apostas internas ou externas, voc?? pode apostar em qualquer n??mero, ou combina????o de n??meros. Lembre-se que cada aposta \nexterna deve ser de pelo menos o valor do m??nimo da mesa; a mesma regra se aplica ao total apostado nas apostas internas. \nLembre-se tamb??m que cada uma ?? independente da outra em rela????o ao m??nimo da mesa."
                      "\nPara as apostas ganhadoras, a aposta original ?? retornada para a sua conta, mais o pagamento que voc?? recebe baseado no valor investido \ne as informa????es das probabilidades (relacionada abaixo). As apostas perdedoras ser??o perdidas."
                      "\nO software reconhece automaticamente que as apostas internas s??o acumulativas, assim as apostas podem ser colocadas na se????o interna \nda mesa at?? que o m??nimo seja atingido. Caso ele n??o seja atingido, as apostas abaixo do m??nimo ser??o removidas quando a roleta for girada (depois que o cron??metro de apostas encerrar)."
                      "\nAo jogar em uma mesa de Jogadores M??ltiplos, todas as apostas ser??o eleg??veis a ganhar ou perder uma vez que o cron??metro de apostas \nencerrar. Nas mesas de Jogador ??nico, as apostas n??o ser??o consideradas ativas at?? que a a????o seja confirmada e o bot??o Girar tenha sido clicado."
                      "\n"
                      "\n                 Pagamento das Apostas Internas - Roleta"
                      "\nNome Da Aposta         N??meros Cobertos           Probabilidade de Pagamento"
                      "\n Pleno                        1                             35 para 1"
                      "\n Dividir                      2                             17 para 1"
                      "\n Linha                        3                             11 para 1"
                      "\n Quadrado                     4                             8 para 1"
                      "\n Linha Dupla                  6                             5 para 1"
                      "\n"
                      "\n                 Pagamento Das Apostas Externas - Roleta"
                      "\nNome Da Aposta         N??meros Cobertos           Probabilidade de Pagamento"
                      "\n Vermelho                     18                            1 para 1"
                      "\n Preto                        18                            1 para 1"
                      "\n ??mpar                        18                            1 para 1"
                      "\n Par                          18                            1 para 1"
                      "\n Baixo(1-18)                  18                            1 para 1"
                      "\n Alto(19-36                   18                            1 para 1"
                      "\n 1??, 2?? ou 3?? duzia           12                            2 para 1"
                      "\n 1??, 2?? ou 3?? coluna          12                            2 para 1"
                      "\n"
                      "\nApostas Divididas e Racetrack"
                      "\nAl??m das se????es Interna e Externa, as apostas tamb??m podem ser colocadas na ??rea 'racetrack' da mesa. Esta se????o do layout da mesa de \nroleta representa a ordem real que os n??meros aparecem na pr??pria roleta. Clique em um dos n??meros para colocar fichas nele, \nmais os dois n??meros adjacentes (conhecidos como 'vizinhos') dos dois lados deste n??mero."
                      "\nA 'racetrack' pode ser utilizada para colocar outras quatro apostas especiais, cada qual coloca automaticamente v??rias fichas no layout,\n como mostrado na tabela a seguir."
                      "\n"
                      "\nNome Da Aposta         Custo Da Ficha          N??meros Cobertos                              Distribui????o"
                      "\n Vizinhos do Zero       Nove Fichas                   17                              0/2/3 (duas fichas), 4/7, 12/15, 18/21, 19/22, 25/26/28/29 (duas fichas), 32/35"
                      "\n Ter??o da Roleta        Seis Fichas                   12                              5/8, 10/11, 13/16, 23/24, 27/30, 33/36"
                      "\n Orphelins en Plein     Oito Fichas                   8                               1, 6, 9, 14, 17, 20, 31, 34"
                      "\n Zero                   Quatro Fichas                 7                               0/3, 12/15, 26, 32/35"
                      "\n"
                      "\nApostas em dois n??meros adjacentes (divididos) da mesma cor no layout principal (ex. vermelho ou preto) podem ser apostadas em uma a????o\n utilizando os controles para apostas divididas encontrados perto da ??rea 'racetrack' da mesa."
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
                      "\nSeguindo uma conven????o semelhante ?? maioria dos cassinos modernos em todo o mundo, os limites de apostas nas mesas de roleta variam, \ndependendo se elas cobrem as apostas internas ou externas."
                      "\nA aposta externa m??xima exibida em cada mesa indica o maior valor que pode ser colocado em cada (ou todas) as posi????es de apostas externas. N??o existe um m??ximo acumulativo."
                      "\nA aposta interna m??xima de uma mesa se refere ao valor permitido para ser colocado em cada aposta de n??mero individual (ou direta)."
                      "\nTodos os outros tipos de apostas internas (por exemplo a dividida, linha dupla, linha, etc.) t??m o seu pr??prio valor m??ximo de aposta, \nrelativo ao m??ximo do direto da mesa. A regra geral ?? que quanto mais n??meros forem cobertos por uma aposta, maiores ser??o os limites. \nPor exemplo, uma aposta Pleno cobre um n??mero e a aposta m??xima pode ser de 25 fichas. Uma aposta Dividida cobre dois n??meros e assim o dobro do m??ximo ?? permitido (50 fichas). \nUma aposta de Linha cobre tr??s n??meros e neste exemplo a aposta m??xima seria de 75 fichas, e assim por diante."
                      "\nEm uma mesa com um limite de aposta m??xima no pleno de 25 fichas, ?? poss??vel colocar at?? 40 apostas de 25 fichas em torno de um n??mero \nposicionado na coluna do meio do layout, como o 17 (apostas em um pleno (1), quatro divididos (8), uma linha (3), quatro quadrados (16), e duas linhas duplas (12), para um total de 1.000 fichas."
                      "\n"
                      "\nVantagem Da Casa"
                      "\nOs jogos de Roleta t??m uma vantagem da casa (calculada como a diferen??a entre as probabilidades reais e as probabilidades de pagamento) de 2,70%."
                      "\nOs jogos de American Roulette t??m uma vantagem da casa de 5,26%. A aposta Five Line na American Roulette tem uma vantagem da casa de 7,89%."
                      "\n"
                      "\nApostas Salvas"
                      "\nEm mesas de Jogador ??nico, ?? poss??vel salvar suas apostas favoritas, ent??o voc?? pode fazer apostas de combina????o espec??fica de forma r??pida e conveniente. \nSelecione ???Salvar Aposta Atual??? para adicion??-la aos seus favoritos. Voc?? pode gerenciar apostas salvas no menu ???Minhas Apostas???."
                      "\n"
                      "\nMesas De Jogadores M??ltiplos"
                      "\nAs Mesas de Jogadores M??ltiplos oferecem a voc?? e seus amigos a oportunidade de jogarem juntos e aproveitar a emo????o de um jogo social. Exatamente como nos cassinos da vida real, \nas mesas de Jogadores M??ltiplos transformam o jogo online em uma experi??ncia interativa divertida.")
            elif n == "2" or n == "jogar":
                jogo.mesa()
                sleep(1.5)
                while true:
                    print(cor+f"\nEscolha a sua ficha"
                          f"\n[1]-R$0.5"
                          f"\n[2]-R$2.5"
                          f"\n[3]-R$5"
                          f"\n[4]-R$25"
                          f"\n[5]-R$100"
                          f"\n[6]-R$500"
                          f"\n[7]-R$2K"
                          f"\n[8]-R$5K"
                          f"\n[9]-Encerrar Aposta"
                          f"\n[0]-Encerrar Programa"+normal)
                    fichas = str(input("\nDigite: "))
                    try:
                        fichas = int(fichas)
                    except:
                        print(Fore.RED+"Valor Invalido, favor digitar novamente"+normal)
                        continue
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
                    elif fichas == 9:
                        print("VOLTA PRA TELA INICIAL")
                    elif fichas == 0:
                        print("\nObrigado por jogar o nosso jogo")
                        print("Tenha um otimo dia")
                        quit()
            elif n == '3':
                print("\nVOLTA PRA TELA INICIAL")
            elif n == '4':
                print("\nObrigado por jogar o nosso jogo")
                print("Tenha um otimo dia")
                quit()
            else:
                print(f"Digite um valor v??lido")

jogo = Roleta("", 0,"hugo", 'CASSINO (1).db', 'con', 'cursor')
jogo.inicio()
jogo.fichasEOpcoes()
