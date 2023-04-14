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
    
    def __init__(self,laberinto:Laberinto,origen:tuple,destino:tuple,color):
        self.Index_Trayectoria = None
        self.Index_Nodo = None
        self.__Color=color
        self.Laberinto = laberinto
        try:
            self.Problema = Problema(estado_inicial=self.Laberinto.getEstado(origen[0],origen[1]),
                                estados_objetivos=[self.Laberinto.getEstado(destino[0],destino[1])],
                                espacio_estados=self.Laberinto.EspacioEstados)
        except:
            print("No se definio el problema correctamente")
            return None
    
    def __labelToCord(self,label:str):
        
        num=''
        for l in label:
            if l.isdigit():
                num=num + l
            else:
                letra=l
        
        return int(num)-1,ord(letra)-65
    
    def __cordToLabel(self,f:int,c:int):
        
        return str(f+1)+str(chr(c+65))
    
    def calcular(self,opcion:int=0):
        Arbol_Solucion=None
        if opcion==0:
            Arbol_Solucion,self.Trayectoria = BFS(problema=self.Problema)
        if opcion==1:
            Arbol_Solucion, self.Trayectoria = DFS(problema=self.Problema)
        
        self.Lista_Camino = Arbol_Solucion.soluciones(problema=self.Problema)[0]
        # print([nodo.__str__() for nodo in Trayectoria])
        
        self.Trayectoria_Completa=[]
        tam = self.Trayectoria.__len__()
        i=0
        while True:
            nodo = self.Trayectoria[i]
            nodo_sig = self.Trayectoria[i+1]
            self.Trayectoria_Completa.append(nodo.Estado)
            for accion in self.Problema.Espacio_Estados[nodo.Estado].keys():
                self.Trayectoria_Completa.append(accion)
                if self.Problema.Espacio_Estados[nodo.Estado][accion]==nodo_sig:
                    break
            
            i+=1
            if i ==tam-1:
                nodo = self.Trayectoria[i]
                self.Trayectoria_Completa.append(nodo.Estado)
                break
        # print(self.Lista_Camino)
        # print([elem.__str__() for elem in self.Trayectoria_Completa])
        self.Index_Trayectoria = 0
        self.Index_Nodo = 0
        self.__F, self.__C = self.__labelToCord(self.Trayectoria_Completa[0].__str__())

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
    
        
    
    
    def backState(self):
        self.Index_Trayectoria -= 1

        if not self.Index_Trayectoria == -1:

            elem = self.Trayectoria_Completa[self.Index_Trayectoria]
            if isinstance(elem, Estado):
                self.F, self.C = self.__labelToCord(elem.__str__())
                return elem
            elif isinstance(elem, Accion):
                self.Orientation = elem.__str__()
                return elem
        else:
            self.Index_Trayectoria += 1
            return None
    
    def nextState(self):
        self.Index_Trayectoria += 1
        
        if not self.Index_Trayectoria == self.Trayectoria_Completa.__len__():
            
            elem=self.Trayectoria_Completa[self.Index_Trayectoria]
            if isinstance(elem, Estado):
                self.F,self.C=self.__labelToCord(elem.__str__())
                return elem
            elif isinstance(elem, Accion):
                self.Orientation=elem.__str__()
                return elem
        else:
            self.Index_Trayectoria -= 1
            return None
        
        
    def backNode(self):
        self.Index_Nodo -= 1

        if not self.Index_Nodo == -1:
            elem = self.Trayectoria[self.Index_Nodo]
            self.F, self.C = self.__labelToCord(elem.__str__())
            return elem
        else:
            self.Index_Nodo += 1
            return None

    def nextNode(self):
        self.Index_Nodo+=1
        
        if not self.Index_Nodo == self.Trayectoria.__len__():
            elem=self.Trayectoria[self.Index_Nodo]
            self.F, self.C = self.__labelToCord(elem.__str__())
            return elem
        else:
            self.Index_Nodo -= 1
            return None
        
    def backCamino(self):
        self.Index_Nodo -= 1

        if not self.Index_Nodo == -1:
            elem = self.Lista_Camino[self.Index_Nodo]
            self.F, self.C = self.__labelToCord(elem.__str__())
            return elem
        else:
            self.Index_Nodo += 1
            return None

    def nextCamino(self):
        self.Index_Nodo += 1

        if not self.Index_Nodo == self.Lista_Camino.__len__():
            elem = self.Lista_Camino[self.Index_Nodo]
            self.F, self.C = self.__labelToCord(elem.__str__())
            return elem
        else:
            self.Index_Nodo -= 1
            return None
