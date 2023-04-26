from collections import deque
from .Estructuras import Accion,Estado,Nodo,Problema


"""
Funciones auxiliares
"""
def __nodoRaiz(problema:Problema)->Nodo: # Listo
    estado_raiz=problema.Estado_Inicial
    acciones_raiz={}
    
    if estado_raiz in problema.Espacio_Estados.keys():
        acciones_raiz= problema.Espacio_Estados[estado_raiz]
    raiz=Nodo(estado=estado_raiz,acciones=acciones_raiz)
    raiz.Costo=0
    return raiz


def __nodoHijo(problema: Problema, padre: Nodo, accion: Accion) -> Nodo:  # Listo
    nuevo_estado=problema.sucesorFN(padre.Estado,accion)
    acciones_nuevo={}
    
    if nuevo_estado in problema.Espacio_Estados.keys():
        acciones_nuevo = problema.Espacio_Estados[nuevo_estado]

    hijo=Nodo(nuevo_estado,accion,acciones_nuevo,padre)
    costo=padre.Costo
    costo+=problema.costoAccion(padre.Estado,accion)
    hijo.Costo=costo
    padre.addNodo(hijo)
    return hijo

# Busqueda primero por anchura
def BFS(problema: Problema,info:bool=False):  # Listo
    raiz=__nodoRaiz(problema)
    
    if problema.testObjetivo(raiz.Estado):
        return raiz
    # la frontera almacena nodos
    frontera=deque([])
    frontera.appendleft(raiz)  # se inserta por la izquierda
    ruta=[]
    # explorados almacena estados
    explorados=set() # un set tiene elementos unicos sin repetirse
    if info:
        print("======================BFS============================")
    while True:
        if info:
            # print("Explorados:", [estado.__str__() for estado in explorados])
            print("Frontera(DEQUE-LIFO):=IN=>", [nodo.__str__() for nodo in frontera],"=OUT=>")
        
        # hasta que se quede vacia la frontera, si eso pasa no hay solucion.
        if len(frontera)==0:
           return None
        nodo = frontera.pop() # se quita y se devuelve el elemento de la derecha
        explorados.add(nodo.Estado)
        ruta.append(nodo)
        if info:
            print("Pop:", nodo, end="-->")
        if not nodo.Acciones:
            if info:
                print("no hay acciones")
            continue
        
        # validacionde acciones que podemos realizar
        for accion in nodo.Acciones.keys():
            hijo = __nodoHijo(problema,nodo,accion)
            estados_frontera = [nodo.Estado for nodo in frontera]
            if hijo.Estado not in explorados and hijo.Estado not in estados_frontera:
                if info:
                    print(hijo,end="|")
                if problema.testObjetivo(hijo.Estado):
                    ruta.append(hijo)
                    if info:
                        print("\n=====================================================",end='')
                        print("\nSe encontro el objetivo:", hijo)
                    return hijo,ruta
                
                frontera.appendleft(hijo) # se inserta por la izquierda
        if info:
            print("\n=====================================================")
                
# Busqueda con Costo Uniforme
def UCS(problema: Problema, info: bool = False):  # Listo
    raiz = __nodoRaiz(problema)
    # la frontera almacena nodos
    frontera = [raiz,]

    # explorados almacena estados
    explorados = set()  # un set tiene elementos unicos sin repetirse
    ruta=[]
    if info:
        print("=======================UCS===========================")
    while True:
        if info:
            # print("Explorados:", [estado.__str__() for estado in explorados])
            print("Frontera(PRIORY-LIFO):<=IN==", [(nodo.__str__(),nodo.Costo)
              for nodo in frontera], "<====")

        # hasta que se quede vacia la frontera, si eso pasa no hay solucion.
        if len(frontera) == 0:
            if info:
                print("Frontera vacia, no se encontro el objetivo")
                print("=====================================================")
            return None
        nodo = frontera.pop(0)
        ruta.append(nodo)
        if problema.testObjetivo(nodo.Estado):
            if info:
                print("Se encontro el objetivo:", nodo)
                print("=====================================================")
            return nodo,ruta
        explorados.add(nodo.Estado)
        if info:
            print("Pop:", nodo)
            print("=====================================================")
        if not nodo.Acciones:
            if info:
                print("no hay acciones")
            continue

        # validacion de acciones que podemos realizar
        for accion in nodo.Acciones.keys():
            hijo = __nodoHijo(problema, nodo, accion)

            estados_frontera = [nodo.Estado for nodo in frontera]
            if hijo.Estado not in explorados and hijo.Estado not in estados_frontera:
                frontera.append(hijo) 
            else:
                buscar = [nodo for nodo in frontera 
                          if nodo.Estado== hijo.Estado]
                
                if buscar:
                    if hijo.Costo < buscar[0].Costo:
                        indice=frontera.index(buscar[0])
                        frontera[indice]=hijo
            frontera.sort(key=lambda nodo: nodo.Costo)

# Busqueda Primero en Profundidad
def DFS(problema: Problema, info: bool = False):  # Listo
    raiz = __nodoRaiz(problema)

    if problema.testObjetivo(raiz.Estado):
        return raiz
    # la frontera almacena nodos
    frontera = []
    frontera.append(raiz)
    ruta=[]
    # explorados almacena estados
    explorados = set()  # un set tiene elementos unicos sin repetirse
    if info:
        print("========================DFS==========================")
    while True:
        if info:
            # print("Explorados:", [estado.__str__() for estado in explorados])
            print("Frontera(STACK-FIFO):", [nodo.__str__()
              for nodo in frontera], "<==OUTOUT==>")

        # hasta que se quede vacia la frontera, si eso pasa no hay solucion.
        if len(frontera) == 0:
           return None
        nodo = frontera.pop()
        explorados.add(nodo.Estado)
        ruta.append(nodo)
        if info:
            print("Pop:", nodo, end="-->")
        if not nodo.Acciones:
            if info:
                print("no hay acciones")
            continue

        # validacionde acciones que podemos realizar
        for accion in nodo.Acciones.keys():
            hijo = __nodoHijo(problema, nodo, accion)

            estados_frontera = [nodo.Estado for nodo in frontera]
            if hijo.Estado not in explorados and hijo.Estado not in estados_frontera:
                if info:
                    print(hijo, end="|")
                if problema.testObjetivo(hijo.Estado):
                    ruta.append(hijo)
                    if info:
                        print("\n=====================================================",end='')
                        print("\nSe encontro el objetivo:", hijo)
                    return hijo,ruta

                frontera.append(hijo)
        if info:
            print("\n=====================================================")


# Busqueda Primero en Profundidad (Recursiva)
def DFS_R(problema: Problema):  # Listo
    explorados = set()
    nodo_raiz = __nodoRaiz(problema)
    return __BPP_R(nodo_raiz, problema, explorados)
    

def __BPP_R(nodo: Nodo, problema: Problema, explorados: set):  # Listo
    if problema.testObjetivo(nodo.Estado):
        return nodo
    explorados.add(nodo.Estado)
    # print([estado.__str__() for estado in explorados])
    if not nodo.Acciones:
        return None
    for accion in problema.Espacio_Estados[nodo.Estado]:
        hijo = __nodoHijo(problema, nodo, accion)
        
        if hijo.Estado not in explorados:
            resultado = __BPP_R(hijo, problema, explorados)
            if resultado:
                return resultado
    return None

# Busqueda Primero en Profundidad Limitada Recursiva
# Seria el DFS_R pero limitada a niveles
def LDFS_R(problema, limite=99999):  # Listo
    explorados = set()
    nodo_raiz = __nodoRaiz(problema)
    return __BPL_R(nodo_raiz, problema, limite, explorados)

def __BPL_R(nodo, problema, limite, explorados):  # Listo
    
    if problema.testObjetivo(nodo.Estado):
       return nodo

    if limite == 0:
        return None # corte
    explorados.add(nodo.Estado)

    for accion in problema.Espacio_Estados[nodo.Estado]:
        hijo = __nodoHijo(problema,nodo,accion)
        if hijo.Estado not in explorados:
            resultado = __BPL_R(hijo,problema,limite-1,explorados.copy())

            if resultado:
               return resultado

    return None


# Busqueda Primero en Profundidad Limitada Iterativa
def LDFS_I(problema, limite)->Nodo: # Listo
    if limite is None:
        # Si el limite no fue definida por defecto sera
        # por busqueda primero a profundidad
       resultado = DFS_R(problema)

    for i in range(1, limite + 1):
        resultado = LDFS_R(problema, i)
        if resultado:
         return resultado
    return None


# Busqueda en Profundidad de Costo Iterativo
# Busqueda en Costo Iterativo
def ICS(problema: Problema, limite: int = 99999, intervalo: int = 1, info: bool = False):
    for i in range(1,limite+1,intervalo):
        nodo_raiz = __nodoRaiz(problema)
        explorados=set()
        soluciones=[]
        __Costo_Recursivo(nodo_raiz, problema,limite, explorados,soluciones)
        if soluciones:
            mejor=min(soluciones,key=lambda nodo: nodo.Costo)
            if info:
                print("==================ICS: Lista del conjunto de soluciones====================")
                print([(nodo.__str__(), nodo.Costo) for nodo in soluciones])
                print("El mejor es :",mejor)
                print("===========================================================================")
            return mejor
    return None

def __Costo_Recursivo(nodo: Nodo, problema: Problema,limite:int, explorados: set,soluciones:list):
    if limite <= 0:
        # print("Menor",limite)
        return None
    if problema.testObjetivo(nodo.Estado):
        soluciones.append(nodo)
        return nodo
    explorados.add(nodo.Estado)
    if not nodo.Acciones:
        return None
    for accion in nodo.Acciones.keys():
        hijo = __nodoHijo(problema, nodo, accion)
        if hijo.Estado not in explorados:
            costo=problema.costoAccion(nodo.Estado,accion)
            # print(limite) # tiene que ser mas grande que el costo, sino no regrega nada
            __Costo_Recursivo(hijo, problema,limite - costo, explorados.copy(),soluciones)
    return None


# Busqueda Bidireccional 
def __nodoBS(problema: Problema,estado:Estado) -> Nodo:  # Listo
    acciones = {}
    
    if estado in problema.Espacio_Estados.keys():
        acciones = problema.Espacio_Estados[estado]
        
    raiz = Nodo(estado=estado, acciones=acciones)
    raiz.Costo = 0
    return raiz

def __ampliaFrontera(problema:Problema,nodo:Nodo,objetivo:Estado,frontera:list,explorados:list):
    for accion in nodo.Acciones.keys():
        hijo=__nodoHijo(problema,nodo,accion)
        estados_frontera = [nodo.Estado for nodo in frontera]
        estados_explorados = [nodo.Estado for nodo in explorados]
        
        if hijo.Estado not in estados_explorados and hijo.Estado not in estados_frontera:
            if hijo.Estado == objetivo:
                return hijo
            
            frontera.append(hijo)
    
    return None


def BS(problema: Problema, info: bool = False):
    
    if info:
        print("=======================================BS===========================================")
    nodo_i=__nodoBS(problema,problema.Estado_Inicial)
    nodo_f=__nodoBS(problema,problema.Estados_Objetivos[0])
    
    if problema.testObjetivo(nodo_f):
        return (nodo_i,nodo_f)
    
    if problema.Estado_Inicial==nodo_f.Estado:
        return (nodo_i, nodo_f)
    
    frontera_i = [nodo_i, ]
    frontera_f = [nodo_f, ]
    
    explorados_i=[]
    explorados_f=[]
    
    while True:
        if not frontera_i or not frontera_f:
            return (None,None)
        
        nodo_i = frontera_i.pop(0)
        nodo_f = frontera_f.pop()
        
        explorados_i.append(nodo_i)
        explorados_f.append(nodo_f)
        
        resultado_i = __ampliaFrontera(
            problema, nodo_i, problema.Estados_Objetivos[0], frontera_i, explorados_i)
        resultado_f = __ampliaFrontera(
            problema, nodo_f, problema.Estado_Inicial, frontera_f, explorados_f)
        
        if resultado_i:
            return (resultado,None)
        
        if resultado_f:
            return (None, resultado)
        
        nodos_arbol_i=[]
        nodos_arbol_f=[]
        nodos_arbol_i.extend(frontera_i)
        nodos_arbol_f.extend(frontera_f)
        nodos_arbol_i.extend(explorados_i)
        nodos_arbol_f.extend(explorados_f)
        if info:
            print("nodos_i:",[nodo.__str__() for nodo in nodos_arbol_i])
            print("nodos_f:",[nodo.__str__() for nodo in nodos_arbol_f])
            print()
        estados_i = set(nodo.Estado for nodo in frontera_i)
        estados_f = set(nodo.Estado for nodo in frontera_f)
        
        estados_i = estados_i.union(set(nodo.Estado for nodo in explorados_i))
        estados_f = estados_f.union(set(nodo.Estado for nodo in explorados_f))
        
        comunes = estados_i.intersection(estados_f)
        if comunes:
            
            
            comun= comunes.pop()
            comun_i = [
                nodo for nodo in nodos_arbol_i if nodo.Estado == comun][0]
            comun_f = [
                nodo for nodo in nodos_arbol_f if nodo.Estado == comun][0]

            return muestraSolucionBS((comun_i, comun_f) ,False)
        

def muestraSolucionBS(solucion:tuple=(None|Nodo,None|Nodo), info: bool = False):
    if info:
        print("==================Camino Bidireccional del objetivo al nodo raiz=====================")
    nodo_i=solucion[0]
    nodo_f=solucion[1]
    
    costo_i=nodo_i.Costo if nodo_i else 0
    costo_f=nodo_f.Costo if nodo_f else 0
    camino=[]
    list_aux=[]
    # Se recorren los nodos en su respectivo sentido
    if nodo_i:
        while nodo_i :
            list_aux.insert(0, nodo_i.__str__())
            if nodo_i.Accion_Padre:
                list_aux.insert(0, nodo_i.Accion_Padre.__str__())
            camino.insert(0,nodo_i)
            nodo_i=nodo_i.Padre
    if nodo_f:
        nodo_f=nodo_f.Padre # es el nodod comun, lo saltamos para no repetirlo
        while nodo_f:
            list_aux.append(nodo_f.Accion_Padre.__str__())
            list_aux.append(nodo_f.__str__())
            camino.append(nodo_f)
            nodo_f=nodo_f.Padre
    
    
    if not camino:
        if info:
            print("No hay solucion")
            print("====================================================================================")
        return
    
    if info:
        for nodo in camino:
            msg = "Estado "+nodo.Estado.__str__()
            print(msg)
    
    if info:
        print("====================================================================================")
        print("Costo total:",costo_i+costo_f)
        print("====================================================================================")
    return [nodo.__str__() for nodo in camino]
