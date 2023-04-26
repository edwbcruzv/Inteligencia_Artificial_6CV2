from .Estructuras import *


"""
Funciones auxiliares
"""
def __nodoRaiz(problema: Problema) -> Nodo:  # Listo
    estado_raiz = problema.Estado_Inicial
    acciones_raiz = {}

    if estado_raiz in problema.Espacio_Estados.keys():
        acciones_raiz = problema.Espacio_Estados[estado_raiz]
    raiz = NodoH(estado=estado_raiz, acciones=acciones_raiz)
    raiz.Costo = 0
    raiz.Heuristica = estado_raiz.Heuristica
    raiz.FNValor = raiz.Costo+raiz.Heuristica
    return raiz


def __nodoHijo(problema: Problema, padre: Nodo, accion: Accion) -> Nodo:  # Listo
    nuevo_estado = problema.sucesorFN(padre.Estado, accion)
    acciones_nuevo = {}

    if nuevo_estado in problema.Espacio_Estados.keys():
        acciones_nuevo = problema.Espacio_Estados[nuevo_estado]

    hijo = NodoH(nuevo_estado, accion, acciones_nuevo, padre)
    costo = padre.Costo
    costo += problema.costoAccion(padre.Estado, accion)
    hijo.Costo = costo
    hijo.Heuristica=nuevo_estado.Heuristica
    hijo.FNValor = hijo.Costo+hijo.Heuristica
    padre.addNodo(hijo)
    return hijo

# Busqueda Voras (F(n)= H(n)) sin el costo de camino recorrido,
# Busqueda con Costo Uniforme
def UCS_V(problema: Problema, info: bool = False):  # Listo
    raiz = __nodoRaiz(problema)
    # la frontera almacena nodos
    frontera = [raiz, ]

    # explorados almacena estados
    explorados = set()  # un set tiene elementos unicos sin repetirse
    ruta = []
    if info:
        print("=======================UCS===========================")
    while True:
        if info:
            # print("Explorados:", [estado.__str__() for estado in explorados])
            print("Frontera(PRIORY-LIFO):<=IN==", [(nodo.__str__(),nodo.Heuristica)
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
            return nodo, ruta
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
                          if nodo.Estado == hijo.Estado]

                if buscar:
                    print(hijo.Heuristica,buscar[0].Heuristica)
                    if hijo.Heuristica < buscar[0].Heuristica:
                        indice = frontera.index(buscar[0])
                        frontera[indice] = hijo
            frontera.sort(key=lambda nodo: nodo.Heuristica)


# Busqueda A* (F(n)= H(n) +  G(n))
# Busqueda con Costo Uniforme
def UCS_A(problema: Problema, info: bool = False):  # Listo
    raiz = __nodoRaiz(problema)
    # la frontera almacena nodos
    frontera = [raiz, ]

    # explorados almacena estados
    explorados = set()  # un set tiene elementos unicos sin repetirse
    ruta = []
    if info:
        print("=======================UCS===========================")
    while True:
        if info:
            # print("Explorados:", [estado.__str__() for estado in explorados])
            print("Frontera(PRIORY-LIFO):<=IN==", [(nodo.__str__(), nodo.FNValor, nodo.Costo, nodo.Heuristica)
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
            return nodo, ruta
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
                          if nodo.Estado == hijo.Estado]

                if buscar:
                    if hijo.FNValor < buscar[0].FNValor:
                        indice = frontera.index(buscar[0])
                        frontera[indice] = hijo
            frontera.sort(key=lambda nodo: nodo.FNValor)