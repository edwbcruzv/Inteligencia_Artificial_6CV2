from MiBusqueda import *
from LaberintoTemplate import *
class Agente:
    ID_int=0
     # celula y la orientacion
        #      0   1   2
        #    +---+---+---+
        #  0 |   | U |   |
        #    +---+---+---+
        #  1 | L |   | R |
        #    +---+---+---+
        #  2 |   | D |   |
        #    +---+---+---+
    
    def __init__(self,origen:tuple,destino:tuple,color):
        self.Laberinto = Laberinto("Laberinto2.txt", ['U', 'D', 'L', 'R'])
        try:
            self.Problema = Problema(estado_inicial=self.Laberinto.getEstado(origen[0],origen[1]),
                                estados_objetivos=[self.Laberinto.getEstado(destino[0],destino[1])],
                                 espacio_estados=self.Laberinto.EspacioEstados)
        except:
            print("No se definio el problema correctamente")
            return None
        
        self.Arbol_Solucion=None
        self.Trayectoria=None
        self.Lista_Camino=None
        
        self.__F, self.__C = self.__labelToCord(origen[0], origen[1])
        self.__Color=color
        
    
    def __labelToCord(self,num:int,letra:str):
        return num-1,ord(letra)-65
    
    def calcula(self):
        self.Arbol_Solucion,self.Trayectoria = BFS(problema=self.Problema)
        self.Lista_Camino = self.Arbol_Solucion.soluciones(problema=self.Problema)[0]
    """
    #------------------------------------
    @property
    def Atributo(self):
        # Documentacion de Atributo 
        return self.__Atributo
    
    @Atributo.setter
    def Atributo(self,new_Atributo):
        self.__Atributo=new_Atributo
    
    @Atributo.deleter
    def Atributo(self):
        del self.__Atributo
    #------------------------------------
    """
    #------------------------------------
    @property
    def Color(self):
        # Documentacion de Color 
        return self.__Color
    #------------------------------------
    
    #------------------------------------
    @property
    def F(self):
        # Documentacion de F 
        return self.__F
    
    @F.setter
    def F(self,new_F):
        self.__F=new_F
    
    @F.deleter
    def F(self):
        del self.__F
    #------------------------------------
    
    #------------------------------------
    @property
    def C(self):
        # Documentacion de C 
        return self.__C
    
    @C.setter
    def C(self,new_C):
        self.__C=new_C
    
    @C.deleter
    def C(self):
        del self.__C
    #------------------------------------
    
    #------------------------------------
    @property
    def Orientation(self):
        # Documentacion de ID 
        return self.__Orientation
    @Orientation.setter
    def Orientation(self,new_Orientation):
        self.__Orientation=new_Orientation
    
    @Orientation.deleter
    def Orientation(self):
        del self.__Orientation
    #------------------------------------
    
    
    
    def nextState(self):
        pass
    
    def backState(self):
        pass