import sqlite3
import random
from colorama import Fore, Back, Style

a = Back.RED
b = Back.BLACK
no = Back.RESET
letraPreta = Fore.RESET
verde = Back.LIGHTGREEN_EX
preto = Fore.BLACK


def roleta():
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

roleta()

alea = random.randint(0, 36)
print(alea)