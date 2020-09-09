from No import No

class Lista: 

    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def adicionar(self, valor):
        if self.primeiro: 
            aux = self.primeiro
            ant = None
            while(aux.proximo):
                ant = aux
                aux = aux.proximo
            aux.proximo = No(valor)
            aux.proximo.anterior = aux
            aux.anterior = ant
            if self.ultimo:
                self.ultimo = aux.proximo
        else:
            self.primeiro = No(valor)
            self.ultimo = No(valor)
    
    def Vazio(self):
        return self.primeiro is None

    def ImpListaOrd(self):
        if self.primeiro== None:
            print("A lista está vazia")

        aux = self.primeiro
        print("Lista em ordem de cadastro" )
        while(aux):
            
            print(aux.dado)
            aux = aux.proximo
        
       
    
    def ImpListaRev(self):
        aux = self.ultimo
        print("Lista em ordem reversa " )
        while(aux):
            print(aux.dado)
            aux = aux.anterior
        
     
           

    