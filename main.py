import sqlite3


class Contas():
    def __init__(self, nomeBanco, variavelConexão, variavelCursor):
        self.variavelConexão = sqlite3.connect(f'{nomeBanco}')
        self.variavelConexão.execute("PRAGMA foreign_keys = 1")
        self.variavelCursor = self.variavelConexão.cursor()
    def menu(self):
        print("Menu:"
              "1-Criar Conta"
              "2-Entrar Na Conta"
              )
        resposta = int(input("Digite Aqui: "))
        return resposta
    def criarConta(self):
        nome = str(input("Digite seu nome: "))
        senha = str(input("Digite sua senha: "))
        email = str(input("Digite seu email: "))
        self.variavelCursor.execute(f"INSERT INTO contas(nome, senha, email) VALUES ('{nome}','{senha}', '{email}' )")
        self.variavelCursor.execute("SELECT * FROM contas")
        for linhas in self.variavelCursor.fetchall():
            print(linhas)


conta1 = Contas("Casino.db", "conexao", "cursor")
conta1.criarConta()