#PROJETO INDIVIDUAL DE PROGRAMAÇÃO (LCD) 2025/2026
#ALINE FONTOURA N.º 139552

#T1 CLASSE MEMBRO (MEMBER):
class Member:
    def __init__(self,idt,name,enter=0,sub=False):
        self.__idt=idt
        self.__name=name
        self.enter=enter
        self.sub=sub
        
    @property
    def idt(self):
        return self.__idt
    @property
    def name(self):
        return self.__name
    
    def buy_enter(self, buy):
        self.enter+=buy
    
    def active_or_unactive(self, process):
        if process==False:
            self.sub = False
        else:
            self.sub = True        
        
    def __str__(self):
        if self.sub ==False:
            return str(self.idt)+": "+ self.name + "(" + str(self.enter)+ " entradas disponíveis, subscrição inativa)"
        else:
            return str(self.idt)+": "+ self.name + "(" + str(self.enter)+" entradas disponíveis, subscrição ativa)"
    
    def __eq__(self,other):
        if not isinstance (other, self.__class__):
            return False
        else:
            return self.idt==other.idt
        
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

#T2 CLASSE AULA (CLASS):
class Class:
    def __init__(self,name1,instrutor,lotacao):
        self.__name1= name1
        self.__inst=instrutor
        self.__lot=lotacao
        self.alunos=[]
        
    @property
    def name1(self):
        return self.__name1
    @property
    def instrutor(self):
        return self.__inst
    @property
    def lotacao(self):
        return self.__lot
    
    def entrada (self, membro):
        if not isinstance (membro, Member):
            print ("Erro de registo!")
        elif membro in self.alunos:
            print ("Este aluno já está registado!")
        elif len(self.alunos) == self.__lot:
            print ("Aula cheia!")
        else:
            self.alunos.append(membro)
            print(f"{membro.name} entrou na aula {self.name1}.")
    
    def saída (self,membro):
        if not isinstance (membro, Member):
            print ("Erro de registo!")
        elif membro in self.alunos:
            self.alunos.remove(membro)
        else:
            print ("Nunca esteve cá...")
    
    def are_you_here(self,identificador):
        for membro in self.alunos:
            if membro.idt == identificador:
                print ("Estás aqui!")
            else:
                print ("Não estás aqui :(")       
    
    def estado (self):
        ocupadas= len(self.alunos)
        disponíveis= self.__lot - ocupadas
        print(f"{ocupadas} vagas ocupadas e {disponíveis} disponíveis, ainda vais a tempo!")
    
    def __str__(self):
        return self.name1+ ": "+ self.__inst+ " ( " + str(len(self.alunos))+ "/"+ str(self.__lot) + ")"
        
    def list_students(self):
        print ("---Participantes de Aula----")
        for c in self.alunos:
            print (c)
    
 # Exemplos de objetos Class            
c1  = Class("Yoga Matinal", "Ana Silva", 15)
c2  = Class("Pilates", "João Mendes", 12)
c3  = Class("CrossFit", "Rita Costa", 20)
c4  = Class("Zumba", "Clara Sousa", 18)
c5  = Class("Karaté", "Hugo Almeida", 10)
c6  = Class("Musculação", "Pedro Ramos", 25)
c7  = Class("Spinning", "Marta Ferreira", 16)
c8  = Class("Boxe", "Tiago Nunes", 14)
c9  = Class("Dança Contemporânea", "Inês Rocha", 12)
c10 = Class("Meditação Guiada", "Sofia Martins", 8)            
             
class Gym:
    def __init__(self,nome, localizacao,lotacao):
        self.__nome= nome
        self.__loc=localizacao
        self.__lotacao=lotacao
        self.alunos=[]
        self.membros=[]
        self.aulas=[]
        
    @property
    def nome(self):
        return self.__nome
    @property
    def localizacao(self):
        return self.__loc
    @property
    def lotacao(self):
        return self.__lotacao
        
    def new_member(self,membro):
        if not isinstance (membro, Member):
            print ("Erro de registo!")
        elif membro in self.membros:
            print ("Este aluno já está registado!")
        elif len(self.membros) >= self.lotacao:
            print ("Ginásio cheio!")
        else:
            self.membros.append(membro)
            print (f"{membro.name} registado com sucesso!")
            
    def entry (self,membro):
        if membro not in self.membros:
            print (f"{membro.nome} não está registado!")
        elif membro.enter>0:
            membro.enter-=1
            self.alunos.append(membro)
            print (f"Bem vindo {membro.nome} !")
        else:
            print ("Tens de comprar entradas!")
            
            
    def out (self,membro):
        if membro in self.alunos:
            self.alunos.remove(membro)
            print ("Até a próxima ;)")
        else:
            print ("Este membro nunca esteve presente...")
    
    def is_it (self,identificador):
        for membro in self.alunos:
            if membro.idt == identificador:
                print ("Estás aqui!")
                return True 
            else:
                print ("Não estás aqui :(")
                return False 
   
    def gimi_members(self):
        print ("---Membros do Ginásio----")
        for c in self.membros:
            print (c)
            
    def in_gimi (self):
        print ("---No Ginásio----")
        for c in self.alunos:
            print (c)
            
    def create_class (self, classes):
        if not isinstance (classes, Class):
            print ("Erro de registo!")
        elif classes in self.aulas:
            print ("Esta é aula já existe")
        else:
            name1= input("Qual é o nome da tua aula: ")
            instrutor= input ("Como se chama o teu instrutor: ")
            lotacao= int(input("Qual é a lotação máxima: "))
            classes= Class (name1, instrutor, lotacao)
            self.aulas.append(classes)
            print (f"Aula {name1} criada com sucesso!")
            
    def cancel_class (self, classes):
        if not isinstance (classes, Class):
            print ("Erro de registo!")
        elif classes in self.aulas:
            self.aulas.remove(classes)
            print (f"{classes.name1} foi cancelada com sucesso!")
        else:
            print ("Esta aula nunca existiu...")
            
    def aula_in_gimi(self):
        print ("---Aulas a decorrer---")
        for c in self.aulas:
            print (c)
            
    def estado (self):
        ocupadas=len(self.alunos)
        disponivel= self.lotacao - ocupadas
        print(f"{ocupadas} vagas ocupadas e {disponivel} vagas disponíveis")
    
    def __str__(self):
        return f"{self.nome} @ {self.localizacao} ({len(self.alunos)}/{self.lotacao})"

    #T4: exportação e carregamento a partir de ficheiros???
    def export_the_gimi(self, filename):
        f = open (filename, "w")
        f.write(f"{self.nome}, {self.__loc}, {self.lotacao}\n")
        for c in self.membros:
            f.write(f"{c.idt},{c.name},{c.enter},{c.sub}\n")
        for x in self.aulas:
            f.write(f"{x.name1},{x.inst},{x.lot}\n")
        f.close()
            
    
    def carregas (self, filename):
        f=open(filename, 'r')
        primeira= f.readline().strip()
        if primeira:
            nome, localizacao, lotacao = primeira.strip().split(',')
            self= Gym ( nome,localizacao,int(lotacao))
        for line in f:
            if len(line)==4:
                idt, name, enter, sub= line.strip().split(',')
                membro= Member (int(idt), name, int(enter), sub)
                self.membros.append(membro)
            elif len(line)==3:
                name1, inst, lot = line.strip(). split(',')
                aula= Class (name1, inst, int(lot))
                self.aulas.append(aula)
            return self
            
        
        

 # Exemplos de objetos Gym
g1 = Gym("LCD Fit", "Lisboa", 150)
g1.new_member(m1)
g1.create_class(c1)