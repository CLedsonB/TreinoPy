class Aluno: 
    def __init__(self, nome, senha):
         self.nome = nome
         self.senha = senha
    def mudar_senha(self, senha_antiga, senha_nova): 
        if self.senha == senha_antiga:
            self.senha = senha_nova 
            return True 
        else:
            return False 
            
class Interface: 
    alunos = [] 
    def cadastrar_aluno(self): 
        nome = input('\tQual é o nome do aluno?\n')
        senha = input('\tQual é a senha desejada?\n')
        self.alunos.append(Aluno(nome, senha))
        print('\tAluno adicionado!')
        
    def listar_alunos(self):
         for i, aluno in enumerate(self.alunos):
                print(i, aluno.nome)
    def mudar_senha(self):
         numero_aluno = int(input('\tQual é o número de listagem do aluno?'))
         senha_antiga = input('\tQual é a senha atual?\n')
         senha_nova = input('\tQual é a senha nova desejada?\n')
         sucesso = self.alunos[numero_aluno].mudar_senha(senha_antiga, senha_nova)
         if sucesso: 
             print('\tAlteração realizada!')
         else: 
             print('\tErro ao tentar alterar senha!')
    def loop(self):
        while True:
            cmd = input('\n\t1 - Listar alunos\n\t2 - Cadastrar aluno\n\t3 - Mudar senha\n')
            if cmd == '1':
                self.listar_alunos()
            elif cmd == '2':
                self.cadastrar_aluno()
            elif cmd == '3':
                self.mudar_senha()
            else:
                print('\tNão entendi!')
                continue
if __name__ == '__main__':
    interface = Interface()
    interface.loop()