from time import sleep
from tkinter import Frame
import numpy as np
from TableroFrame import *
from LaberintoTemplate import *
from Constantes import *
from Agente import *
from Controls import *
import re

class Window(Frame):
    
    
    def __init__(s,master,width:int,height:int):
        # Constructor de Frame()
        super().__init__(master,width=width,height=height,background="gray")
        s.Width=width
        # empaquetando elementos dentro de su ventana contenedora
        s.Laberinto = None
        s.Centinela_Auto=False
        
        s.Laberinto_Txt = "Laberinto2.txt"
        s.createWidgets()
        s.changeWidgets()
        s.pack()
        
    # Aqui se crean todos los widgets del frame
    def createWidgets(s):
        # se define el tamaño estatico del canvas en pixeles y la posicion
        matriz_laberinto = np.loadtxt(s.Laberinto_Txt, dtype=int)
        s.Lab_cv=TableroFrame(master=s,matrix_laberinto=matriz_laberinto,cells_side=matriz_laberinto.shape[0],size_px=700)
        s.Lab_cv.place(x=(s.Width/2)+s.Lab_cv.SideCellPX, y=s.Lab_cv.SideCellPX)
        
        str_lbl_char = []
        str_lbl_num = []
        for n,l in zip(range(15),range(15)):
            # print(str(n+1)+str(chr(l+65)))
            str_lbl_char.append(str(chr(l+65)))
            str_lbl_num.append(str(n+1))
        
        LX = LY = s.Lab_cv.SideCellPX
        POS_X = (s.Width/2)+LX
        POS_Y = 0
        labels_X=[]
        for i,text in zip(range(15),str_lbl_char):
            labels_X.append(Label(s, text="|-"+text+"-|"))
            labels_X[i].place(x=POS_X+(LX*i),y=POS_Y,width=LX,height=LY)
        
        POS_X = (s.Width/2)
        POS_Y = LY
        labels_Y=[]
        for i, text in zip(range(15), str_lbl_num):
            labels_Y.append(Label(s, text="|-"+text+"-|"))
            labels_Y[i].place(x=POS_X, y=POS_Y+(LY*i), width=LX, height=LY)
            
        s.Controls=Controls(master=s)
        s.Controls.Fila_Origen.config(values=str_lbl_num)
        s.Controls.Columna_Origen.config(values=str_lbl_char)
        
        s.Controls.Fila_Destino.config(values=str_lbl_num)
        s.Controls.Columna_Destino.config(values=str_lbl_char)
        
        s.Controls.place(x=10, y=10)
        
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
        
        s.Controls.Cbtn_Vista_Agente.config(command=s.__Vista_Agente)
    
    def __Vista_Agente(s):
        if s.Controls.VistaAgente.get():
            s.Lab_cv.render()
        else:
            s.Lab_cv.hide()
    
    def __Cargar(s):
        
        if not len(s.Controls.Lbl_Estado_Orden["text"])==4:
            return
        list_orden_acciones = [a for a in s.Controls.Lbl_Estado_Orden["text"]]
        # print(list_orden_acciones)
        s.Laberinto = Laberinto(s.Laberinto_Txt, list_orden_acciones)
        
        s.f_o=s.Controls.Fila_Origen.get()
        s.c_o=s.Controls.Columna_Origen.get()
        s.f_d=s.Controls.Fila_Destino.get()
        s.c_d=s.Controls.Columna_Destino.get()
        
        print(s.f_o, s.c_o, s.f_d, s.c_d)
        
        # al se creado el agente esta listo para moverlo
        s.agente = Agente(s.Laberinto, origen=(int(s.f_o), s.c_o),
                          destino=(int(s.f_d), s.c_d), color=COLOR_3)
        if not s.agente.calcular(s.Controls.AlgoritmoNoInfo.get()):
            print("No se puede resolver")
            return None
        # Se coloca al agente en el estado inicial
        s.Lab_cv.drawAgent(s.agente.F, s.agente.C, None)
        
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
        
        s.__Vista_Agente()
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
        s.Lab_cv.drawAgent(s.agente.F, s.agente.C)
        return elem

    def __Camino_Next(s):
        elem = s.agente.nextCamino()
        s.Lab_cv.drawAgent(s.agente.F, s.agente.C)
        return elem
        
    def __Nodo_Back(s):
        elem = s.agente.backNode()
        s.Lab_cv.drawAgent(s.agente.F, s.agente.C)
        return elem
    def __Nodo_Next(s):
        elem = s.agente.nextNode()
        s.Lab_cv.drawAgent(s.agente.F, s.agente.C)
        return elem
    def __Estado_Back(s):
        elem=s.agente.backState()
        if isinstance(elem, Estado):
            s.Lab_cv.drawAgent(s.agente.F, s.agente.C)
        elif isinstance(elem, Accion):
            s.Lab_cv.drawAgent(s.agente.F, s.agente.C,True)
        return elem
    def __Estado_Next(s):
        elem=s.agente.nextState()
        if isinstance(elem, Estado):
            s.Lab_cv.drawAgent(s.agente.F, s.agente.C)
        elif isinstance(elem, Accion):
            s.Lab_cv.drawAgent(s.agente.F, s.agente.C,True)
        return elem
            
if __name__ == '__main__':
    root = Tk()
    root.title("Ventana Principal")
    app = Window(root, 1500, 800)
    app.mainloop()
