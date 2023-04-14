from time import sleep
from tkinter import Frame
import numpy as np
from LaberintoFrame import *
from LaberintoTemplate import *
from Constantes import *
from Agente import *
from Controls import *
import re

class Window(Frame):
    
    
    def __init__(s,master,width:int,height:int):
        # Constructor de Frame()
        super().__init__(master,width=width,height=height,background="gray")
        # empaquetando elementos dentro de su ventana contenedora
        s.Laberinto = Laberinto("Laberinto2.txt", ['U', 'D', 'L', 'R'])
        s.Centinela_Auto=False
        
        s.createWidgets()
        s.changeWidgets()
        s.pack()
    
    def createAgent(s):
        # al se creado el agente esta listo para moverlo
        s.agente = Agente(s.Laberinto, origen=(int(s.f_o), s.c_o),
                          destino=(int(s.f_d), s.c_d), color=COLOR_3)
        s.agente.calcular(s.Controls.AlgoritmoNoInfo.get())
        # se resetea el laberinto
        s.Lab_cv.clear()
        # Se coloca al agente en el estado inicial
        s.Lab_cv.drawAgent(s.agente.F,s.agente.C,None)
        
    # Aqui se crean todos los widgets del frame
    def createWidgets(s):
        # se define el tamaño estatico del canvas en pixeles y la posicion
        s.Lab_cv=LaberintoFrame(master=s,matrix_laberinto=s.Laberinto.Matriz,cells_side=15,size_px=700)
        s.Lab_cv.place(relx=0.5,rely=0.01)
        s.Controls=Controls(master=s)
        s.Controls.place(relx=0.01, rely=0.1)
        
    def changeWidgets(s):
        s.Controls.Btn_Cargar.config(command=s.__Cargar)
        s.Controls.Btn_Iniciar.config(command=s.__Iniciar)
        s.Controls.Btn_Pausar.config(command=s.__Pausar)
        s.Controls.Btn_Cancelar.config(command=s.__Cancelar)
        s.Controls.Btn_L.config(command=s.__L)
        s.Controls.Btn_R.config(command=s.__R)
        s.Controls.Btn_U.config(command=s.__U)
        s.Controls.Btn_D.config(command=s.__D)
        s.Controls.Btn_Back.config(command=s.__Back)
        s.Controls.Btn_Next.config(command=s.__Next)
    
    def __Cargar(s):
        reg_f=re.compile('\A[1-15]$')
        reg_c=re.compile('\A[A-O]$')
        
        s.f_o=s.Controls.Fila_Origen.get()
        s.c_o=s.Controls.Columna_Origen.get()
        s.f_d=s.Controls.Fila_Destino.get()
        s.c_d=s.Controls.Columna_Destino.get()
        
        # s.f_o='10'
        # s.c_o='A'
        # s.f_d='2'
        # s.c_d='O'
        
        print(s.f_o, s.c_o, s.f_d, s.c_d)
        s.createAgent()
        s.Controls.cargar()
        s.Centinela_Auto=True
        
    def __Iniciar(s):
        while s.Centinela_Auto and s.__Next():
            s.Lab_cv.update()
            sleep(s.Controls.Scale_Velocidad.get())
        print("hecho")
    def __Pausar(s):
        pass
    def __Cancelar(s):
        s.Centinela_Auto = False
        #2inicia los controles
        s.Controls.reiniciar()
        # se resetea el laberinto
        s.Lab_cv.clear()
    def __L(s):
        pass
    def __R(s):
        pass
    def __U(s):
        pass
    def __D(s):
        pass

    def __Back(s):
        if s.Controls.OpcionRecorrido.get()==0:
            return s.__Camino_Back()
        elif s.Controls.OpcionRecorrido.get()==1:
            return s.__Nodo_Back()
        elif s.Controls.OpcionRecorrido.get()==2:
            return s.__Estado_Back()
        return None
    
    def __Next(s):
        if s.Controls.OpcionRecorrido.get()==0:
            return s.__Camino_Next()
        elif s.Controls.OpcionRecorrido.get()==1:
            return s.__Nodo_Next()
        elif s.Controls.OpcionRecorrido.get()==2:
            return s.__Estado_Next()
        return None
    
    def __Camino_Back(s):
        elem = s.agente.backCamino()
        s.Lab_cv.drawAgent(s.agente.F, s.agente.C, None)
        return elem

    def __Camino_Next(s):
        elem = s.agente.nextCamino()
        s.Lab_cv.drawAgent(s.agente.F, s.agente.C, None)
        return elem
        
    def __Nodo_Back(s):
        elem = s.agente.backNode()
        s.Lab_cv.drawAgent(s.agente.F, s.agente.C, None)
        return elem
    def __Nodo_Next(s):
        elem = s.agente.nextNode()
        s.Lab_cv.drawAgent(s.agente.F, s.agente.C, None)
        return elem
    def __Estado_Back(s):
        elem=s.agente.backState()
        if isinstance(elem, Estado):
            s.Lab_cv.drawAgent(s.agente.F, s.agente.C,None)
        elif isinstance(elem, Accion):
            s.Lab_cv.drawAgent(s.agente.F, s.agente.C, s.agente.Orientation)
        return elem
    def __Estado_Next(s):
        elem=s.agente.nextState()
        print(elem)
        if isinstance(elem, Estado):
            s.Lab_cv.drawAgent(s.agente.F, s.agente.C, None)
        elif isinstance(elem, Accion):
            s.Lab_cv.drawAgent(s.agente.F, s.agente.C, s.agente.Orientation)
        return elem
            
if __name__ == '__main__':
    root = Tk()
    root.title("Ventana Principal")
    app = Window(root, 1500, 750)
    app.mainloop()
