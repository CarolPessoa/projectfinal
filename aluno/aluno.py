
class pessoa:
    matricula = 0
    def __init__(self, nome: str, idade: int):
        pessoa.matricula += 1
        self.matricula = pessoa.matricula
        self.nome = nome
        self.idade = idade

def __repr__(self):
    return f"({self.matricula}, {self.nome}, {self.idade})" # função criada com o objetivo de mostrar o resultado em vez do endereço de onde está resultado

 # Só vai mostrar quando vc estiver nessa pasta, e mostrar os objetos.

    p1 = pessoa('Jonas', 21)
    p2 = pessoa('Marta', 19)
    print(p1)
    print(p2)
