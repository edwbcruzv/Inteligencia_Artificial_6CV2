import os
from time import sleep
from tkinter import Frame, Label, Tk
from tkinter.ttk import Notebook
from TableroFrame import *
from Controls import *
from LaberintoTemplate import *
from TerrenoTemplate import *
from Agente import *

class App(Frame):
    
    def __init__(s,master,width:int,height:int):
        s.Width=width
        s.Height=height
        # Constructor de Frame()
        super().__init__(master,width=s.Width,height=s.Height,background="gray")
        
        s.__changeMenu()
        s.__updateWidgets()
        
    def __changeMenu(s):
        s.CTL=Controls(s)
        s.CTL.place(x=10, y=10)
        s.CTL.Menu.Rbtn_Laberintos.config(command=s.__updateWidgets)
        s.CTL.Menu.Rbtn_Terrenos.config(command=s.__updateWidgets)
        s.pack()
        
        
    def __updateWidgets(s):
        s.CTL.updateWidgets()
        
        s.CTL.Principal.Btn_Cargar.config(command=s.__Cargar)
        
        s.CTL.Auto.Btn_Iniciar.config(command=s.__Iniciar)
        s.CTL.Auto.Btn_Pausar.config(command=s.__Pausar)
        s.CTL.Auto.Btn_Cancelar.config(command=s.__Cancelar)
        s.CTL.Manual.Btn_Cancelar.config(command=s.__Cancelar)
        # s.CTL.Libre.Btn_L.config(command=s.__L)
        # s.CTL.Libre.Btn_R.config(command=s.__R)
        # s.CTL.Libre.Btn_U.config(command=s.__U)
        # s.CTL.Libre.Btn_D.config(command=s.__D)
        s.CTL.Manual.Btn_Back.config(command=s.__Back)
        s.CTL.Manual.Btn_Next.config(command=s.__Next)
        s.CTL.Manual.Btn_Cancelar.config(command=s.__Cancelar)
        
        list_values =[]
        if s.CTL.Menu.Opcion_Tablero.get() == 0 and os.path.exists('Laberintos'):
            list_values=os.listdir('Laberintos')
        elif s.CTL.Menu.Opcion_Tablero.get() == 1 and os.path.exists('Terrenos'):
            list_values = os.listdir('Terrenos')
        else:
            return 
            
        s.CTL.Principal.Cbx_Archivos_Txt.config(values=list_values)
        s.CTL.Principal.Cbx_Archivos_Txt.bind('<<ComboboxSelected>>',s.__changeTablero)
        s.CTL.Principal.Cbtn_Vista_Agente.config(command=s.__Vista_Agente)
        s.pack()
        
    def __changeTablero(s,event):
        # se define el tamaño estatico del canvas en pixeles y la posicion
        if s.CTL.Menu.Opcion_Tablero.get() == 0:
            s.Archivo_Txt = "Laberintos/" + s.CTL.Principal.Cbx_Archivos_Txt.get()
            matriz_tablero = np.loadtxt(s.Archivo_Txt, dtype=int)
            # Laberinto
            s.Tablero_cv = TableroFrame(master=s, matrix_laberinto=matriz_tablero,
                                        cells_side=matriz_tablero.shape[0], size_px=700)
        elif s.CTL.Menu.Opcion_Tablero.get() == 1:
            s.Archivo_Txt = "Terrenos/" + s.CTL.Principal.Cbx_Archivos_Txt.get()
            matriz_tablero = np.loadtxt(s.Archivo_Txt, dtype=int)
            # Terreno
            list_aux = s.CTL.Principal.Cbx_Archivos_Txt.get().split('.')
            if list_aux[0] == "Humano":
                s.Tablero_cv = HumanoFrame(master=s, matrix_laberinto=matriz_tablero,
                                        cells_side=matriz_tablero.shape[0], size_px=700)
            elif list_aux[0] == "Monkey":
                s.Tablero_cv = MonkeyFrame(master=s, matrix_laberinto=matriz_tablero,
                                        cells_side=matriz_tablero.shape[0], size_px=700)
            elif list_aux[0] == "Octopus":
                s.Tablero_cv = OctopusFrame(master=s, matrix_laberinto=matriz_tablero,
                                        cells_side=matriz_tablero.shape[0], size_px=700)
            elif list_aux[0] == "Sasquatch":
                s.Tablero_cv = SasquatchFrame(master=s, matrix_laberinto=matriz_tablero,
                                        cells_side=matriz_tablero.shape[0], size_px=700)
            else:
                return None
        else:
            return None
        
        s.Tablero_cv.place(x=(s.Width/2)+s.Tablero_cv.SideCellPX,
                       y=s.Tablero_cv.SideCellPX)

        str_lbl_char = []
        str_lbl_num = []
        for n, l in zip(range(15), range(15)):
            # print(str(n+1)+str(chr(l+65)))
            str_lbl_char.append(str(chr(l+65)))
            str_lbl_num.append(str(n+1))

        LX = LY = s.Tablero_cv.SideCellPX
        POS_X = (s.Width/2)+LX
        POS_Y = 0
        labels_X = []
        for i, text in zip(range(15), str_lbl_char):
            labels_X.append(Label(s, text="|-"+text+"-|"))
            labels_X[i].place(x=POS_X+(LX*i), y=POS_Y, width=LX, height=LY)

        POS_X = (s.Width/2)
        POS_Y = LY
        labels_Y = []
        for i, text in zip(range(15), str_lbl_num):
            labels_Y.append(Label(s, text="|-"+text+"-|"))
            labels_Y[i].place(x=POS_X, y=POS_Y+(LY*i), width=LX, height=LY)
            
        s.CTL.Principal.Fila_Origen.config(values=str_lbl_num)
        s.CTL.Principal.Columna_Origen.config(values=str_lbl_char)
        s.CTL.Principal.Fila_Destino.config(values=str_lbl_num)
        s.CTL.Principal.Columna_Destino.config(values=str_lbl_char)
        
        
        s.__Vista_Agente()
        s.pack()
    
    def __Vista_Agente(s):
        if s.CTL.Principal.VistaAgente.get():
            s.Tablero_cv.render()
        else:
            s.Tablero_cv.hide()
            
    def __Cargar(s):

        if not len(s.CTL.Principal.Lbl_Estado_Orden["text"]) == 4:
            return
        list_orden_acciones = [a for a in s.CTL.Principal.Lbl_Estado_Orden["text"]]
        # print(list_orden_acciones)
            
        s.f_o = s.CTL.Principal.Fila_Origen.get()
        s.c_o = s.CTL.Principal.Columna_Origen.get()
        s.f_d = s.CTL.Principal.Fila_Destino.get()
        s.c_d = s.CTL.Principal.Columna_Destino.get()

        print(s.f_o, s.c_o, s.f_d, s.c_d)

        if s.CTL.Menu.Opcion_Tablero.get() == 0:
            # Laberinto
            laberinto = Laberinto(s.Archivo_Txt, list_orden_acciones)
            s.agente = Agente(laberinto, origen=(int(s.f_o), s.c_o),
                              destino=(int(s.f_d), s.c_d), color=COLOR_3)
            if not s.agente.calcular(s.CTL.Principal.AlgoritmoNoInfo.get()):
                print("No se puede resolver")
                return None
            
        elif s.CTL.Menu.Opcion_Tablero.get() == 1:
            # Terreno
            terreno= Terreno(s.Archivo_Txt, list_orden_acciones)
            s.agente = Agente(terreno, origen=(int(s.f_o), s.c_o),
                              destino=(int(s.f_d), s.c_d), color=COLOR_4)
            if not s.agente.calcular(s.CTL.Principal.AlgoritmoInfo.get(),True):
                print("No se puede resolver")
                return None
        
        # Se coloca al agente en el estado inicial
        s.Tablero_cv.drawAgent(s.agente.F, s.agente.C, None)

        s.CTL.cargar()
        s.Centinela_Auto = True

    def __Iniciar(s):
        
        while s.Centinela_Auto and s.__Next():
            s.Tablero_cv.update()
            sleep(s.CTL.Auto.Scale_Velocidad.get())
        print("hecho")

    def __Pausar(s):
        pass

    def __Cancelar(s):
        s.Centinela_Auto = False
        #2inicia los controles
        s.CTL.cancelar()
        # se resetea el laberinto
        s.Tablero_cv.clear()

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
        if s.CTL.Principal.OpcionRecorrido.get() == 0:
            return s.__Camino_Back()
        elif s.CTL.Principal.OpcionRecorrido.get() == 1:
            return s.__Nodo_Back()
        elif s.CTL.Principal.OpcionRecorrido.get() == 2:
            return s.__Estado_Back()
        return None

    def __Next(s):
        if s.CTL.Principal.OpcionRecorrido.get() == 0:
            return s.__Camino_Next()
        elif s.CTL.Principal.OpcionRecorrido.get() == 1:
            return s.__Nodo_Next()
        elif s.CTL.Principal.OpcionRecorrido.get() == 2:
            return s.__Estado_Next()
        return None

    def __Camino_Back(s):
        elem = s.agente.backCamino()
        s.Tablero_cv.drawAgent(s.agente.F, s.agente.C)
        return elem

    def __Camino_Next(s):
        elem = s.agente.nextCamino()
        s.Tablero_cv.drawAgent(s.agente.F, s.agente.C)
        return elem

    def __Nodo_Back(s):
        elem = s.agente.backNode()
        s.Tablero_cv.drawAgent(s.agente.F, s.agente.C)
        return elem

    def __Nodo_Next(s):
        elem = s.agente.nextNode()
        s.Tablero_cv.drawAgent(s.agente.F, s.agente.C)
        return elem

    def __Estado_Back(s):
        elem = s.agente.backState()
        if isinstance(elem, Estado):
            s.Tablero_cv.drawAgent(s.agente.F, s.agente.C)
        elif isinstance(elem, Accion):
            s.Tablero_cv.drawAgent(s.agente.F, s.agente.C, True)
        return elem

    def __Estado_Next(s):
        elem = s.agente.nextState()
        if isinstance(elem, Estado):
            s.Tablero_cv.drawAgent(s.agente.F, s.agente.C)
        elif isinstance(elem, Accion):
            s.Tablero_cv.drawAgent(s.agente.F, s.agente.C, True)
        return elem

if __name__ == '__main__':
    root = Tk()
    root.title("Ventana Principal")
    app = App(root, 1500, 800)
    app.mainloop()
