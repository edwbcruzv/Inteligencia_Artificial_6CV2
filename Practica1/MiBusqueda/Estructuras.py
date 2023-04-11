from _collections_abc import MutableMapping


class Accion:
    """
    La accion que se aplicara al padre para generar el nodo.
    """
    def __init__(self, nombre:str) -> None:
        self.__Nombre = nombre
    
    @property
    def Nombre(self)->str:
        return self.__Nombre

    def __str__(self) -> str:
        return self.Nombre

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value,Accion):
            return self.Nombre == __value.Nombre
        else:
            # print("Clase Accion: Incompatibilidad de clases")
            return False

    def __hash__(self) -> int:
        return hash(self.Nombre*len(self.Nombre))


class Estado:
    """
    El estado que le corresponde a un nodo.
    En cada estaso se podra ejecutar una serio de acciones.
    Las acciones definiral los hijos del estado
    """

    def __init__(self, nombre:str, acciones: list) -> None:
        self.__Nombre = nombre
        self.__Acciones = acciones

    @property
    def Nombre(self)->str:
        return self.__Nombre
    
    @property
    def Acciones(self)->list:
        return self.__Acciones
    
    def __str__(self) -> str:
        # ocultar las acciones para solo ver el estado
        # msg = "{0}-->{1}"
        # return msg.format(self.Nombre, [accion.__str__() for accion in self.Acciones])
        return self.Nombre

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Estado):
            return self.Nombre == __value.Nombre
        else:
            # print("Clase Estado: Incompatibilidad de clases")
            return False
    
    def __hash__(self) -> int:
        return hash(self.Nombre*len(self.Nombre))


class Problema:
    """
    Modelo abstracto del problema segun la definicion y que es interpretada
    por cualquier algorito que necesite de ella.
    """
    def __init__(self, estado_inicial: Estado, estados_objetivos: list, espacio_estados: dict|MutableMapping,costos:dict|MutableMapping=None) -> None:
        self.Estado_Inicial = estado_inicial
        self.Estados_Objetivos = estados_objetivos
        self.Espacio_Estados = espacio_estados
        self.__num_Objetivos=len(self.Estados_Objetivos)
        self.Costos=costos
        self.CostoInfinito=99999999999999999999
        
        # se crea un objeto vacio para evitar problemas por no agregar los costos
        # y a cada accion se le da un costo de 1
        if not self.Costos:
            self.Costos={}
            for estado in self.Espacio_Estados.keys():
                self.Costos[estado]={}
                for accion in self.Espacio_Estados[estado].keys():
                    self.Costos[estado][accion]=1
            

    def testObjetivo(self, estado: Estado) -> tuple:
        if isinstance(estado, Estado):
            self.__num_Objetivos = self.__num_Objetivos-1
            return estado in self.Estados_Objetivos
        else:
            return None

    # describe las posibles acciones disponibles para el agente
    def sucesorFN(self, estado: Estado, accion: Accion) -> Accion:

        # disponibilidad del estado (nodo)
        if estado not in self.Espacio_Estados.keys():
            # si no es valido no hay nada que regresar
            return None
        
        # si es valido el estado, se buscan las acciones (nodos hijos)
        acciones_estado = self.Espacio_Estados[estado]
            
        # se busca el par ordenado <Accion : Estado_Sucesor>
        if accion not in acciones_estado.keys():
            # existe la accion, pero no el estado sucesor
            return None
        else:
            # se regresa el estado sucesor de la accion
            return acciones_estado[accion]
        
    def costoAccion(self,estado:Estado,accion:Accion)->float|int:
        # Checamos si ele stado es valido
        if estado not in self.Costos.keys():
            # Al no existir el estado su costo es infinito
            return self.CostoInfinito
        
        # recodar que e sun dicionario
        costos_estado=self.Costos[estado]
        
        # Checamos que la accion sea valida
        if accion not in costos_estado.keys():
            # al no existir la accion su costo es infinito
            return self.CostoInfinito
        else:
            return costos_estado[accion]
        
    def costoCamino(self, nodo) -> float | int:
        total=0
        while nodo.Padre:
            total +=self.costoAccion(nodo.Padre.Estado,nodo.Accion_Padre)
            nodo=nodo.Padre
        return total

    def __str__(self) -> str:
        msg = "Estado Inicial:{0}\nObjetivos:{1}\nEspacio de estados:{2}"
        return msg.format(self.Estado_Inicial,
                        [estados.Nombre for estados in self.Estados_Objetivos],
                        [accion.__str__() for accion in self.Espacio_Estados])


class Nodo:
    """
    Es el encargado de crear el grafo.
    El primer elemento sera el nodo raiz
    """
    def __init__(self, estado, accion_padre=None, acciones=None, padre=None) -> None:
        self.Estado = estado
        self.Accion_Padre = accion_padre
        self.Acciones = acciones
        self.Padre=padre
        self.Hijos = []
        self.Costo=0
    

    def expandir(self, problema:Problema)->list:
        # limpia de la variable
        self.Hijos = []
        # verificamos la existencia de acciones
        if not self.Acciones:
            # buscamos las acciones del estado actual
            if self.Estado not in problema.Espacio_Estados.keys():
                # estariamos en un nodo hoja
                return self.Hijos
            else:
                # traemos las acciones
                self.Acciones = problema.Espacio_Estados[self.Estado]

        # Recorremos las acciones que se pueden ejecutar en el estado
        # y los expandimos
        for accion_to_new_child in self.Acciones.keys():
            nuevo_estado = problema.sucesorFN(self.Estado, accion_to_new_child)
            acciones_nuevo = {}
            
            # checamos el el nuevo estado sea valido,
            # se encuentre dentro del espacio de estados y 
            # que nos regrese las acciones de ese estado
            if nuevo_estado in problema.Espacio_Estados.keys():
                acciones_nuevo = problema.Espacio_Estados[nuevo_estado]
            
            # Creamos unn nodo hijo para que se siga expandiendo el grafo
            hijo = Nodo(nuevo_estado, accion_to_new_child, acciones_nuevo, self)
            
            # Iremos guardando el costo del camino de cada nodo que ve vaya expandiendo.
            # Tomamos el costo del nodo padre, tomando en cuanta la existencia del nodo padre.
            costo=self.Padre.Costo if self.Padre else 0
            costo+=problema.costoAccion(self.Estado,accion_to_new_child)
            hijo.Costo=costo
            
            # Guardamos el nuevo hijo expandido
            self.Hijos.append(hijo)
        return self.Hijos

    def mejorHijo(self,problema:Problema):
        
        if not self.Hijos:
            return None
        
        mejor_hijo=self.Hijos[0]
        
        for hijo in self.Hijos:
            for objetivo in problema.Estados_Objetivos:
                costo_camino_hijo = problema.costoCamino(hijo)
                costo_camino_mejor_hijo = problema.costoCamino(mejor_hijo)
                if costo_camino_hijo < costo_camino_mejor_hijo:
                    mejor_hijo=hijo
                
        return mejor_hijo
    
    def __str__(self) -> str:
        return self.Estado.__str__()
    
    def addNodo(self,nuevo_nodo)->None:
        if isinstance(nuevo_nodo, Nodo) and not nuevo_nodo.Accion_Padre==None :
            nuevo_nodo.Padre=self
            self.Hijos.append(nuevo_nodo)

    def soluciones(self, problema: Problema, info: bool = False):  # Listo
        if info:
            print("=========================Camino del objetivo al nodo raiz con costos============================")
        if not problema:
            if info:
                print("Falta el problema para calcular el costo.")
                print("================================================================================================")
            return
        nodo = self
        if not problema:
            return []
        list_states = [] # [state,state,...,state]
        list_states_actions = [] # [state,action,state,action,...,....,state]
        list_states_actions_cost = [] #[(state,total_cost),(action,cost),......(state,total_cost)]
        nodo = self
        while nodo:
            if info:
                msg = "Estado "+nodo.Estado.__str__()+", Costo total:"+str(nodo.Costo)
                print(msg)
            
            list_states.append(nodo.Estado.__str__())
            
            list_states_actions.append(nodo.Estado.__str__())
            
            list_states_actions_cost.append((nodo.Estado.__str__(), nodo.Costo))
            
            if nodo.Accion_Padre:
                accion = nodo.Accion_Padre
                estado = nodo.Padre.Estado
                costo = problema.costoAccion(estado, accion)
                list_states_actions.append(nodo.Accion_Padre.__str__())
                list_states_actions_cost.append((nodo.Accion_Padre.__str__(), costo))
                if info:
                    msg = "<---"+nodo.Accion_Padre.__str__() + \
                        "[" + str(costo)+"]"+"--"
                    print(msg)
            nodo = nodo.Padre
        if info:
            print("================================================================================================")
        list_states.reverse()
        list_states_actions.reverse()
        list_states_actions_cost.reverse()
        
        return list_states,list_states_actions,list_states_actions_cost
