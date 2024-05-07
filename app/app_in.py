
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from aluno import Aluno
from escola import Escola

class App:
    def __init__(self):
        modo = 'dev'
        if modo == 'dev':
            self.db = Escola()
        else:
            self.db = Escola()

        self.janela = Tk()
        self.janela.title('SysInfinity')

        self.label_matricula = Label(self.janela, text='Matricula', font='Tahoma 14 bold',
                                     fg='red')
        self.label_matricula.grid(row=0, column=0)

        self.txt_matricula = Entry(self.janela, width=27, font='Tahoma 14', state='readonly')
        self.txt_matricula.grid(row=0, column=1)

        self.label_nome = Label(self.janela, text='Nome', font='Tahoma 14 bold',
                                     fg='red')
        self.label_nome.grid(row=1, column=0)

        self.txt_nome = Entry(self.janela, width=27, font='Tahoma 14')
        self.txt_nome.grid(row=1, column=1)


        self.label_idade = Label(self.janela, text='Idade', font='Tahoma 14 bold',
                                     fg='red')
        self.label_idade.grid(row=2, column=0)

        self.txt_idade = Entry(self.janela, width=27, font='Tahoma 14')
        self.txt_idade.grid(row=2, column=1)


        self.label_curso = Label(self.janela, text='Curso', font='Tahoma 14 bold',
                                     fg='red')
        self.label_curso.grid(row=3, column=0)

        self.cursos = ['Python', 'Java', 'Javascript', 'Flask', 'Node']
        self.cb_cursos = ttk.Combobox(self.janela, width=28, font='Tahoma 12',
                                       values=self.cursos, state='readonly')
        self.cb_cursos.grid(row=3, column=1)


        self.label_nota = Label(self.janela, text='Nota', font='Tahoma 14 bold',
                                     fg='red')
        self.label_nota.grid(row=4, column=0)

        self.txt_nota = Entry(self.janela, width=27, font='Tahoma 14')
        self.txt_nota.grid(row=4, column=1)

        self.btn_adicionar = Button(self.janela, font='Tahoma 12 bold', width=7,
                                    text='Adicionar', fg='red', command=self.cadastrarAluno)
        self.btn_adicionar.grid(row=5, column=0)

        self.btn_editar = Button(self.janela, font='Tahoma 12 bold', width=7,
                                    text='Editar', fg='red', command=self.updateAluno)
        self.btn_editar.grid(row=5, column=1)

        self.btn_excluir = Button(self.janela, font='Tahoma 12 bold', width=7,
                                    text='Excluir', fg='red', command=self.removerAluno)
        self.btn_excluir.grid(row=5, column=2)

        self.frame = Frame(self.janela)
        self.frame.grid(row=6, column=0, columnspan=3)
        self.colunas = ['Matricula', 'Nome', 'Idade', 'Curso', 'Nota']
        self.tabela = ttk.Treeview(self.frame, columns=self.colunas, show='headings')
        for coluna in self.colunas:
            self.tabela.heading(coluna, text=coluna)
            self.tabela.column(coluna, width=110)
        self.tabela.bind('<ButtonRelease-1>', self.selecionarAluno)
        self.tabela.pack()

        self.escola = Escola()
        self.janela.mainloop()
    
    def selecionarAluno(self, event):
        self.limparCampos()
        linha_selecionada = self.tabela.selection()
        item = self.tabela.item(linha_selecionada)['values']
        self.txt_matricula.config(state=NORMAL)
        self.txt_matricula.insert(0, item[0])
        self.txt_matricula.config(state=DISABLED)
        self.txt_nome.insert(0, item[1])
        self.txt_idade.insert(0, item[2])
        self.cb_cursos.set(item[3])
        self.txt_nota.insert(0, item[4])

    def removerAluno(self):
        matricula = int(self.txt_matricula.get())
        self.db.deletarAluno(matricula)
        messagebox.showerror('Sucesso!', 'Dados removidos com sucesso!')
        self.atualizarTabela()
        self.limparCampos()


    def limparCampos(self):
        self.txt_nome.delete(0, END)
        self.txt_idade.delete(0, END)
        self.txt_nota.delete(0, END)
        self.txt_matricula.config(state=NORMAL)
        self.txt_matricula.delete(0, END)
        self.txt_matricula.config(state=DISABLED)
        self.cb_cursos.set('')

    def cadastrarAluno(self):
        nome = self.txt_nome.get()
        idade = int(self.txt_idade.get())
        curso = self.cb_cursos.get()
        nota = float(self.txt_nota.get())
        aluno = Aluno(nome, idade, curso, nota)
        self.db.adicionarAluno(aluno)
        messagebox.showinfo('Sucesso!', 'Aluno cadastrado com sucesso!')
        self.atualizarTabela()
        self.limparCampos()

    def updateAluno(self):
        matricula = int(self.txt_matricula.get())
        nome = self.txt_nome.get()
        idade = int(self.txt_idade.get())
        nota = float(self.txt_nota.get())
        curso = self.cb_cursos.get()
        aluno = Aluno(nome, idade, curso, nota)
        aluno.matricula = matricula
        self.db.editarAluno(aluno)
        messagebox.showinfo('Sucesso!', 'Dados alterados com sucesso!')
        self.atualizarTabela()
        self.limparCampos()


    def atualizarTabela(self):
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)
        
        for aluno in self.db.alunos:
            self.tabela.insert('', END, values=(aluno.matricula,
                                                aluno.nome,
                                                aluno.idade,
                                                aluno.curso,
                                                aluno.nota))

