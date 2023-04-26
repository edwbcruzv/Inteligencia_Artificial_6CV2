from typing import Iterator
from MiBusqueda import *
import numpy as np

class Laberinto(MutableMapping):
    
    def __init__(self,laberinto_txt:str,orden_acciones:list) -> None:
        super().__init__()
        self.Orden_Acciones=orden_acciones
        
        if not self.Orden_Acciones.__len__()==4:
            return
        # Definiendo las acciones validas en el laberinto
        self.L = Accion("L")
        self.R = Accion("R")
        self.D = Accion("D")
        self.U = Accion("U")
        
        # Matriz donde se almacenaran los estados
        try:
            self.Matriz = np.loadtxt(laberinto_txt, dtype=int)
            self.Filas =self.Matriz.shape[0]
            self.Columnas = self.Matriz.shape[1]
        except:
            print("Error al carcar el laberinto.txt")
            return None
        
        # diccionario que tendran las acciones las acciones
        self.EspacioEstados={}
        
        # se definen los estados
        self.MatrizEstado = np.ndarray((self.Filas, self.Columnas),dtype=Estado)
        for f in range(0,self.Filas):
            for c in range(self.Columnas):
                # cuando es 1 se crea el estado
                if self.Matriz[f][c]==1:
                    # list aux regresa las acciones validas en cada estado del laberinto
                    lista_aux, dicc_aux = self.__acciones(f, c)
                    self.MatrizEstado[f][c]=Estado(str(f+1)+str(chr(c+65)),lista_aux)
                    # se cada estado se deja las acciones vacias para despues llenar los destinos mas adelante
                    self.EspacioEstados[self.MatrizEstado[f][c]] = {}
                else:
                    self.MatrizEstado[f][c] = '0'
        
        for f in range(0,self.Filas):
            for c in range(self.Columnas):
                if self.Matriz[f][c]==1:
                    lista_aux,dicc_aux = self.__acciones(f, c)
                    
                    self.EspacioEstados[self.MatrizEstado[f][c]] = dicc_aux
                else:
                    self.MatrizEstado[f][c] = '0'
        
        # Validar que hay suficientes estados
        if self.EspacioEstados.__len__()<2:
            self.EspacioEstados=None
        # Muestra la matriz
        # for line in self.MatrizEstado:
        #     print('  '.join(map(str,line)))
        
        # Mostrar el contenido del diccionario
        
        # for estado in self.EspacioEstados.keys():
        #     print(estado, end=":")
        #     try:
        #         print([("{"+key.__str__()+":"+value.__str__()+"}") for key,value in self.EspacioEstados[estado].items()])
        #     except:
        #         print("Algo paso    ")
                
    # Dependiendo del orden de los if sera la prioridad de las acciones
    def __acciones(self,f,c):
        dicc_aux={}
        
        # DOWN (abajo)
        if f+1 < self.Filas and self.Matriz[f+1][c] == 1:
            dicc_aux[self.D]= self.MatrizEstado[f+1][c]
            
        # LEFT (Izquierda)
        if c-1 >= 0 and self.Matriz[f][c-1] == 1:
            dicc_aux[self.L] = self.MatrizEstado[f][c-1]
            
        # RIGHT (Derecha)
        if c+1 < self.Columnas and self.Matriz[f][c+1] == 1:
            dicc_aux[self.R] = self.MatrizEstado[f][c+1]
            
        # UP (ARRIBA)
        if  f-1 >= 0        and self.Matriz[f-1][c] == 1:
            dicc_aux[self.U]= self.MatrizEstado[f-1][c]
        
        lista_keys=list(dicc_aux.keys())
        lista_keys.sort(key= lambda elem: self.Orden_Acciones.index(elem.__str__()))
        dicc_order={key:dicc_aux[key] for key in lista_keys}
        
        return lista_keys,dicc_order
    
    def __str__(self) -> str:
        return str(self.Matriz.shape)+"\n"+self.Matriz.__str__()+"\n"
    
    def __delitem__(self, __key: str) -> None:
        return None
    
    def __getitem__(self, __key: Estado)-> Estado:
        return self.EspacioEstados[__key]
    
    def __iter__(self) -> Iterator:
        return self.EspacioEstados.__iter__()
    
    def __len__(self) -> int:
        return self.EspacioEstados.__len__()
    
    def __setitem__(self, __key, __value) -> None:
        return None
    
    def keys(self):
        return self.EspacioEstados.keys()

    def getEstado(self, num, letra):
        return self.MatrizEstado[num-1][ord(letra)-65]