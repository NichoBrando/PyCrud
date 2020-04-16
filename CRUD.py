import mysql.connector as mysql
from validate_email import validate_email
from tkinter import *

def limitaDigito(entrada, i):
    if len(entrada)>int(i):
        return False
    return True

class JanelaCRUD(Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.conexao = conexao = mysql.connect(
            host="localhost",
            user="root",
            passwd="",
            charset="utf8"
        )
        self.cursorBD = self.conexao.cursor()
        self.resizable(False, False)
        self.cursorBD.execute("create database if not exists PyCrud")
        self.cursorBD.execute("use PyCrud")
        self.cursorBD.execute("create table if not exists cadastro(email varchar(40) not null, nome varchar(40) not null, telefone varchar(11), primary key (email))")
        self.conexao.commit()
        self.limitadorG = self.register(func=limitaDigito)
        self.builderlayout()
        self.title("PyCrud")

    def jaCadastrado(self):
        email = str(self.cadastroEmail.get())
        email = email.strip(' ')
        comando = """select count(email) from cadastro where email = %s"""
        x = self.conexaoDB.execute(comando, (email, ))
        if(x>0):
            return False
        return True

    def cadastrar(self):
        erro = ""
        nome = str(self.cadastroNome.get())
        nome = nome.strip(' ')
        if len(nome) == 0:
            erro += "Nome não preenchido\n"
        email = str(self.cadastroEmail.get())
        email = email.strip(' ')
        if len(email) == 0:
               erro += "E-mail não preenchido"
        is_valid = validate_email(email.strip(' '))
        telefone = str(self.cadastroTelefone.get())
        telefone = telefone.strip(' ')
        self.cadastroMsg.place(x=15, y= 170)
        if(not self.jaCadastrado):
            is_valid = False
        if telefone.isdigit() and len(telefone) >= 10  or telefone == "":
            if is_valid and len(nome) > 0:
                try:
                    comando = "INSERT INTO cadastro(email, nome, telefone) VALUES(%s, %s, %s)"
                    valores = (email, nome, telefone)
                    self.cursorBD.execute(comando, valores)
                    self.conexao.commit()
                    self.cadastroMsg["fg"] = 'green'
                    self.cadastroMsg["text"] = "Cadastro realizado com sucesso! :-)"
                except:
                    pass
            else:
                self.cadastroMsg["fg"] = 'red'
                self.cadastroMsg["text"] = "erro, já cadastrado ou e-mail inválido"
        else:
            self.cadastroMsg["fg"]= 'red'
            self.cadastroMsg["text"] = "Telefone inválido! :-("

    def busca(self):
        emailBusca = str(self.lerEmail.get())
        emailBusca = emailBusca.strip(' ')
        nome = ""
        telefone = ""
        comando = """select nome, telefone from cadastro where email = %s"""
        self.cursorBD.execute(comando, (emailBusca,))
        itens = self.cursorBD.fetchall()
        self.lerMsg.place(x=320, y=121)
        for row in itens:
            nome = row[0]
            telefone = row[1]
        if len(nome) == 0 and len(telefone) == 0:
            self.lerMsg["text"] = "E-mail não cadastrado :/"
            self.lerMsg["fg"] = "red"
        else:
            self.lerMsg["text"] = "Nome: {}\nTelefone: {}".format(nome,telefone if len(str(telefone))>=10 else "Não possui!")
            self.lerMsg["fg"] = "green"
        
    def altera(self):
        comando = ""
        email = str(self.alteraEmail.get())
        email = email.strip(' ')
        nome = str(self.alteraNome.get())
        telefone = str(self.alteraTelefone.get())
        nome = nome.strip(' ')
        telefone = telefone.strip(' ')
        self.alteraMsg.place(x=15, y= 435)
        if len(telefone)>=10 and len(nome)>1:
            comando = """ UPDATE cadastro SET nome = %s, telefone = %s WHERE email = %s"""
            valores = (nome, telefone, email)
            muda = "nome e telefone"
            valor = True
        else:
            if len(telefone)>=10:
                comando = """ UPDATE cadastro SET telefone = %s WHERE email = %s"""
                valores = (telefone, email)
                muda = "telefone"
                valor = False
            elif len(nome)>1:
                comando = """ UPDATE cadastro SET nome = %s WHERE email = %s """
                valores = (nome, email)
                muda = "nome"
                valor = False
        if len(comando)>1:
            self.cursorBD.execute(comando, valores)
            self.conexao.commit()
            self.alteraMsg["fg"] = 'green'
            self.alteraMsg["text"] = "Cadastro alterado com sucesso!\n{} agora {}".format(muda, "possuem outros valores! :-)" if valor else "possui outro valor! :-)")
        else:
            self.alteraMsg["fg"] = 'red'
            self.alteraMsg["text"] = "Cadastro não alterado! :-("
            
    def deleta(self):
        self.deletarMsg.place(x=320, y= 370)
        email = str(self.deletarEmail.get())
        email = email.strip(' ')
        email = (email, )
        comando = """ DELETE FROM cadastro WHERE email = %s"""
        self.cursorBD.execute(comando,email)
        self.conexao.commit()
        if self.cursorBD.rowcount > 0:
            self.deletarMsg["fg"] = 'red'
            self.deletarMsg["text"] = "!!{} cadastro deletado com sucesso!! :-O".format(self.cursorBD.rowcount)
        else:
            self.deletarMsg["fg"] = 'grey'
            self.deletarMsg["text"] = "!!Nenhum cadastro deletado!!"
            
    def builderlayout(self):
        imagem = PhotoImage(file="fundo.png")
        fundo = Label(self, image=imagem)
        fundo.imagem = imagem
        fundo.pack()
        #campo de cadastro
        self.cadastroNome = Entry(width=36,validate='key', validatecommand=(self.limitadorG, '%P', '40'))
        self.cadastroNome.place(x=69, y=57)
        self.cadastroTelefone = Entry(width=11, validate='key', validatecommand=(self.limitadorG, '%P', '11'))
        self.cadastroTelefone.place(x=86, y=81)
        self.cadastroEmail = Entry(width=35, validate='key', validatecommand=(self.limitadorG, '%P', '40'))
        self.cadastroEmail.place(x=75, y=107)
        self.cadastroBotao = Button(text="Cadastrar", bg="green", command=self.cadastrar)
        self.cadastroBotao.place(x=125, y=135)
        self.cadastroMsg = Label(text="", borderwidth=2, relief="solid")
        #campo de alteração
        self.alteraNome = Entry(width=36,validate='key', validatecommand=(self.limitadorG, '%P', '40'))
        self.alteraNome.place(x=51, y=347)
        self.alteraTelefone = Entry(width=11, validate='key', validatecommand=(self.limitadorG, '%P', '11'))
        self.alteraTelefone.place(x=70, y=372)
        self.alteraEmail = Entry(width=35, validate='key', validatecommand=(self.limitadorG, '%P', '40'))
        self.alteraEmail.place(x=56, y=307)
        self.alteraBotao = Button(text="Alterar", bg="blue", command=self.altera)
        self.alteraBotao.place(x=125, y=400)
        self.alteraMsg = Label(text="", borderwidth=2, relief="solid")
        #campo ler
        self.lerEmail = Entry(width=35, validate='key', validatecommand=(self.limitadorG, '%P', '40'))
        self.lerEmail.place(x=361, y=58)
        self.lerBotao = Button(text="Buscar", bg="grey", command=self.busca)
        self.lerBotao.place(x=437, y=86)
        self.lerMsg = Label(text="", borderwidth=2, relief="solid")
        #campo deletar
        self.deletarEmail = Entry(width=35, validate='key', validatecommand=(self.limitadorG, '%P', '40'))
        self.deletarEmail.place(x=359, y=308)
        self.deletarBotao = Button(text="Deletar", bg="red", command=self.deleta)
        self.deletarBotao.place(x=437, y=335)
        self.deletarMsg = Label(text="", borderwidth=2, relief="solid")

if __name__ == '__main__':
    janela = JanelaCRUD()
