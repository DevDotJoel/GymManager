from posix import fpathconf


class Member:
    def __init__(self, idt, name, enter=0, sub=False):
        self.__idt = idt
        self.__name = name
        self.enter = enter
        self.sub = sub

    @property
    def idt(self):
        return self.__idt

    @property
    def name(self):
        return self.__name

    def buy_enter(self, buy):
        self.enter += buy

    def active_or_unactive(self, process):
        self.sub = process

    def __str__(self):
        if self.sub:
            return str(self.idt) + ": " + self.name + "(" + str(self.enter) + " entradas disponíveis, subscrição ativa)"
        else:
            return str(self.idt) + ": " + self.name + "(" + str(self.enter) + " entradas disponíveis, subscrição inativa)"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return self.idt == other.idt
    def print_menu(self):
        print("1.Consultar estado")
        print("2.Registar entrada")
        print("3.Registar saída")
        print("4.Marcar aula")
        print("5.Comprar entradas")
        print("6.Ativar subscrição")
        print("7.Cancelar subscrição")
        print("0.Voltar")

    def menu_membro(self,g):
        while True:
            self.print_menu()
            sel = int(input('Opção: '))
            if sel == 0:
                print("Voltar")
                return
            elif sel == 1:
                estado=str(self)
                if self in g.treinar:
                    estado=str(self)
                    estado+=" - a treinar"
                for aulas in g.aulas:
                    if self in aulas.alunos:
                        estado += f" - em aula: {aulas.name}"
                print(estado)
            elif sel == 2:
                g.entry(self)
            elif sel == 3:
                if self in g.treinar:
                    g.out(self)
                    print("Espero que tenhas tido um bom treino:)")
                else:
                    print ("O membro não está a treinar")
            elif sel == 4:
                print("---Aulas disponíveis---")
                for aulas in g.aulas:
                    print(f"- {aulas.name}: {aulas.instrutor} ({len(aulas.alunos)} / {aulas.lotacao})")
                    aula_escolhida = input("Que aula queres participar: ")
                    if self not in g.treinar:
                        print(" O membro não está a treinar! Tem que registar a sua entrada no ginásio primeiro.")
                    else:
                        for aula in g.aulas:
                            if aula.name == aula_escolhida:
                                aula.entrada(self)
                                print(f" Membro {self.name} registado com sucesso na aula de {aula_escolhida}!")
                                break
                        else:
                            print(f"Essa aula ('{aula_escolhida}') não existe.")
            elif sel == 5:
                compra=int(input('Número de entradas: '))
                if compra <0:
                    print ("Quantidade inválida")
                else:
                    self.buy_enter(compra)
                    print(f"Agora tens {self.enter} entradas")
            elif sel == 6:
                self.active_or_unactive(True)
                print(self)
            elif sel == 7:
                self.active_or_unactive(False)
                print(self)

# Exemplos de objetos Member
m1 = Member(1, "João Silva")
m2 = Member(2, "Maria Costa", 3)
m3 = Member(3, "Pedro Santos", 5, True)
m4 = Member(4, "Ana Ramos")
m5 = Member(5, "Carlos Pinto", 8)
m6 = Member(6, "Rita Gomes", 0, True)
m7 = Member(7, "Luís Pereira", 2)
m8 = Member(8, "Sofia Martins", 10, True)
m9 = Member(9, "Hugo Fernandes", 1)
m10 = Member(10, "Beatriz Lopes", 4, True)


# T2 CLASSE AULA (CLASS):
class Class:
    def __init__(self, name, instrutor, lotacao):
        self.__name = name
        self.__inst = instrutor
        self.__lot = lotacao
        self.alunos = []

    @property
    def name(self):
        return self.__name

    @property
    def instrutor(self):
        return self.__inst

    @property
    def lotacao(self):
        return self.__lot

    def entrada(self, membro):
        if membro in self.alunos:
            print("Este aluno já está registado!")
        elif len(self.alunos) == self.__lot:
            print("Aula cheia!")
        else:
            self.alunos.append(membro)
            print(f"{membro.name} entrou na aula {self.name}.")

    def saída(self, membro):
        if membro in self.alunos:
            self.alunos.remove(membro)
        else:
            print("Nunca esteve cá...")

    def are_you_here(self,membro):
        if membro in self.alunos:
            print(f"{membro.name} ,estás aqui!")
        else:
            print ("Não estás aqui")

    def estado(self):
        ocupadas = len(self.alunos)
        disponíveis = self.__lot - ocupadas
        print(f"{ocupadas} vagas ocupadas e {disponíveis} disponíveis, ainda vais a tempo!")

    def __str__(self):
        return self.name + ": " + self.__inst + " ( " + str(len(self.alunos)) + "/" + str(self.__lot) + ")"

    def list_students(self):
        print("---Participantes de Aula----")
        for c in self.alunos:
            print(c)


# Exemplos de objetos Class
c1 = Class("Yoga Matinal", "Ana Silva", 15)
c2 = Class("Pilates", "João Mendes", 12)
c3 = Class("CrossFit", "Rita Costa", 20)
c4 = Class("Zumba", "Clara Sousa", 18)
c5 = Class("Karaté", "Hugo Almeida", 10)
c6 = Class("Musculação", "Pedro Ramos", 25)
c7 = Class("Spinning", "Marta Ferreira", 16)
c8 = Class("Boxe", "Tiago Nunes", 14)
c9 = Class("Dança Contemporânea", "Inês Rocha", 12)
c10 = Class("Meditação Guiada", "Sofia Martins", 8)


class Gym:
    def __init__(self, nome, localizacao, lotacao):
        self.__nome = nome
        self.__loc = localizacao
        self.__lotacao = lotacao
        self.treinar= []
        self.membros = []
        self.aulas = []

    # adicionar um atributo no membro se está a treinar ou não/comprar entradas no ginásio
    @property
    def nome(self):
        return self.__nome

    @property
    def localizacao(self):
        return self.__loc

    @property
    def lotacao(self):
        return self.__lotacao

    def new_member(self, membro):
        if not isinstance(membro, Member):
            print("Erro de registo!")
        elif membro in self.membros:
            print("Este aluno já está registado!")
        elif len(self.membros) >= self.lotacao:
            print("Ginásio cheio!")
        else:
            self.membros.append(membro)
            print(f"{membro.name} registado com sucesso!")

    def entry(self, membro):
        if membro not in self.membros:
            print(f"{membro.name} não está registado!")
        elif membro.enter > 0:
            membro.enter -= 1
            self.treinar.append(membro)
            print(f"Bem vindo {membro.name} !")
        elif membro.sub==False:
            print(f"{membro.name} tem que ativar a subscrição!")
        else:
            print("Tens de comprar entradas!")

    def out(self, membro):
        if membro in self.treinar:
            self.treinar.remove(membro)
            print("Até a próxima ;)")
        else:
            print("Este membro não estava a treinar")

    def is_it(self, identificador):
        for membro in self.treinar:
            if membro.idt == identificador:
                print("Estás aqui!")
                return True
        print("Não estás aqui :(")
        return False

    def gimi_members(self):
        print("---Membros do Ginásio----")
        for c in self.membros:
            print(c)

    def in_gimi(self):
        print("---No Ginásio----")
        for c in self.treinar:
            print(c)

    def create_class(self):
        i=0
        name = input("Qual é o nome da tua aula: ")
        instrutor = input("Como se chama o teu instrutor: ")
        lotacao = int(input("Qual é a lotação máxima: "))
        classes = Class(name, instrutor, lotacao)
        for a in self.aulas:
            if a.instrutor == instrutor:
                print("Este instrutor já tem aula!")
                i=1
        if lotacao>self.lotacao:
            print("A aula não pode ter lotação maior do que a do ginásio")
            i=1
        elif lotacao<0:
            print("Lotação inválida!")
            i=1
        if i==0:
            self.aulas.append(classes)
            print(f"Aula {name} criada com sucesso!")

    def cancel_class(self):
        x = "Esta aula nunca existiu..."
        cancela=input("Nome do instrutor: ")
        for a in self.aulas:
            if a.instrutor == cancela:
                self.aulas.remove(a)
                x = "A aula foi cancelada com sucesso!"
        print(x)

    def aula_in_gimi(self):
        print("---Aulas a decorrer---")
        for c in self.aulas:
            print(c)

    def estado(self):
        ocupadas = len(self.treinar)
        disponivel = self.lotacao - ocupadas
        print(f"{ocupadas} vagas ocupadas e {disponivel} vagas disponíveis")

    def __str__(self):
        return f"{self.nome} @ {self.localizacao} ({len(self.treinar)}/{self.lotacao})"

    def find(self,id):
        for m in self.membros:
            if m.idt == id:
                return m
        return None


    # T4: exportação e carregamento a partir de ficheiros???
    def export_the_gimi(self, filename):
        f = open(filename, "w")
        f.write(f"{self.nome}, {self.__loc}, {self.lotacao}\n")
        for c in self.membros:
            f.write(f"{c.idt},{c.name},{c.enter},{c.sub}\n")
        for x in self.aulas:
            f.write(f"{x.name},{x.instrutor},{x.lotacao}\n")
        f.close()

    def importar(self, filename):#alterar para self
        f = open(filename, 'r')
        nome, localizacao, lotacao = f.readline().strip().split(',')
        self.name = nome
        self.loc = localizacao
        self.__lotacao = int(lotacao)
        for line in f:
            s=line.strip().split(',')
            if len(s) == 4:
                m=Member(int(s[0]), s[1], int(s[2]), s[3]==True)
                self.membros.append(m)
            elif len(s) == 3:
                aula=Class(s[0], s[1], int(s[2]))
                self.aulas.append(aula)
        f.close()

    def print_menu_gimi(self):
        print("1. Registrar Membro")
        print("2. Listar membros")
        print("3. Listar membros a treinar")
        print("4. Criar aula")
        print("5. Cancelar aula")
        print("6. Listar aulas")
        print("7. Ver aula")
        print("8. Visão global")
        print("0. Voltar")

    def menu_gestão(self):
        while True:
            self.print_menu_gimi()
            sel = int(input("Opção: "))

            if sel == 0:
                print("Voltar")
                return

            elif sel == 1:
                nome_membro = input("Nome do novo membro: ")
                novo_id = self.membros[-1].idt + 1 if self.membros else 1
                novo_membro = Member(novo_id, nome_membro)
                self.new_member(novo_membro)

            elif sel == 2:
                filtro = input("Filtro: ")
                for c in self.membros:
                    if filtro.lower() in c.name.lower():
                        print(c)

            elif sel == 3:
                self.in_gimi()

            elif sel == 4:
                self.create_class()

            elif sel == 5:
                self.cancel_class()

            elif sel == 6:
                self.aula_in_gimi()

            elif sel == 7:
                nome = input("Nome do instrutor: ")
                for c in self.aulas:
                    if nome.lower() == c.instrutor.lower():
                        print(c)
                else:
                    print("Esta aula não existe")

            elif sel == 8:
                print("1. Número de membros")
                print("2. Percentagem de membros com entradas disponíveis ou subscrição ativa")
                print("3. Número de aulas")
                print("4. Ocupação média das aulas")
                print("5. Percentagem dos membros que estão no ginásio que não estão na aula")
                op=int(input("Opção: "))
                if op == 1:
                    if len(self.membros) ==0:
                        print("Não existem membros registados")
                    else:
                        print (f"Número de registados: {len(self.membros)}")
                elif op == 2:
                    quant=0
                    for c in self.membros:
                        if c.sub==True or c.enter>0:
                            quant += 1
                    return (quant*100)/len(self.membros)
                elif op == 3:
                    if len(self.aulas)==0:
                        print ("Não existem aulas disponíveis")
                    else:
                        print(f"Número de aulas: {len(self.aulas)}")
                elif op == 4:
                    media=0
                    for c in self.aulas:
                        media+=len(c.alunos)
                    return media/len(self.aulas)
                elif op == 5:
                    a=self.aulas
                    n_aulas=0
                    for c in self.treinar:
                        if c in a.alunos:
                            n_aulas+=1
                    return (n_aulas*100)/len(self.treinar)










def print_menu():
    print("1. Menu de membro")
    print("2. Menu de gestão")
    print("3. Carregar ginásio")
    print("4. Exportar ginásio")
    print("0. Sair")


def menu_principal():
    g=Gym(None, None, None)
    g.importar('gym.txt')
    while True:
        print_menu()
        sel = int(input('Opção: '))
        if sel == 0:
            print("Saindo do menu")
            return
        elif sel == 1:
            id_membro = int(input('ID do membro: '))
            m=g.find(id_membro)
            if m == None:
                print ("Este membro não existe...")
            else:
                m.menu_membro(g)
        elif sel == 2:
            return g.menu_gestão()
        elif sel == 3:
            if len(g.treinar)==0:
                try:
                    h=input("Nome do ficheiro: ")
                    g.importar(h)
                    print("Ficheiro carregado com sucesso!")
                except:
                    print("Ficheiro inválido!")
            else:
                print("O ginásio tem que estar vazio!")
        elif sel == 4:
            ficheiro=input('Ficheiro: ')
            g.export_the_gimi(ficheiro)
            print("Ficheiro exportado com sucesso!")
        else:
            sel = int(input('Opção: '))

menu_principal()

