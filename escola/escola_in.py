

class EscolaDb:
    def __init__(self):
        self.conexao = pymysql.connect(
            host='localhost', 
            user='root', 
            password='',
            database='escola',
            cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conexao.cursor()

    def listarAlunos(self):
        sql = "SELECT * FROM alunos"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def deletarAluno(self, matricula):
        sql = "DELETE FROM alunos WHERE matricula = %s"
        self.cursor.execute(sql, matricula)
        self.conexao.commit()

    def adicionarAluno(self, aluno: Aluno):
        sql = "INSERT INTO alunos (nome, idade, curso, nota) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (aluno.nome, aluno.idade, aluno.curso, aluno.nota))
        self.conexao.commit()

    def editarAluno(self, aluno: Aluno):
        sql = "UPDATE alunos SET nome = %s, idade = %s, curso = %s, "\
        "nota = %s WHERE matricula = %s"
        self.cursor.execute(sql, (aluno.nome, aluno.idade, aluno.curso,
                                  aluno.nota, aluno.matricula))
        self.conexao.commit()
        self, matricula
        sql = "DELETE FROM alunos WHERE matricula = %s"
        self.cursor.execute(sql, matricula)
        self.conexao.commit()

