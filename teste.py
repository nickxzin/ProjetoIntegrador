import sys

from termcolor import colored, cprint


print(" ___________________________________________________________________"
      "\n|   | 3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 | 33 | 36 | 2to1 |"
      "\n| 0 | 2 | 5 | 8 | 11 | 14 | 17 | 20 | 23 | 26 | 29 | 32 | 35 | 2to1 |"
      "\n|   | 1 | 4 | 7 | 10 | 13 | 16 | 19 | 22 | 25 | 28 | 31 | 34 | 2to1 |"
      "\n -------------------------------------------------------------------"
      "\n    |     1st 12     |       2nd 12      |      3rd 12       |"
      "\n     -------------------------------------------------------- "
      "\n    | 1 - 18 |  PAR  |   RED   |  BLACK  |  IMPAR  | 19 - 36 |"
      "\n     ---------------------------------------------------------")


text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
print(text)
cprint("Hello, World!", "green", "on_red")

print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")
print_red_on_cyan("Hello, World!")
print_red_on_cyan("Hello, Universe!")

for i in range(10):
    cprint(i, "magenta", end=" ")

cprint("Attention!", "red", attrs=["bold"], file=sys.stderr)

for c in range(0, quantidade):
      while true:
            print("\nDigite a casa(s) que deseja de 0-36")
            casa = int(input("Casa nº: "))
            if tentativa == 0:
                  self.apostar.append(casa)
                  tamanho = len(self.apostar)
                  tentativa += 1
                  # break
            elif tentativa == 1:
                  for indice in range(0, tamanho):
                        if self.apostar[indice] == casa:
                              print(f"Valor Já existe, favor digitar novamente um valor valido")
                              print(c)
                        else:
                              self.apostar.append(casa)
                              # tentativa += 1