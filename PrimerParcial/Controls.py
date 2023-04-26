from tkinter import BooleanVar, Checkbutton, IntVar, LabelFrame, Radiobutton, Tk, Label, Frame, Entry, Button, Scale
from tkinter.ttk import Combobox
from Constantes import *


class LFMenu(LabelFrame):
    
    def __init__(s, master):
        s.Width = 690
        s.Height = 80
        # Constructor de Frame()
        super().__init__(master,text="Menu", width=s.Width, height=s.Height, background=COLOR_8)
        s.Opcion_Tablero = IntVar()
        s.Opcion_Libre = BooleanVar()
        s.__controles(10, 10)

        s.pack()

    def __controles(s, POS_X: int, POS_Y: int):
        ANCHO = 100
        ALTURA = 30
        s.Rbtn_Laberintos=Radiobutton(s,text="Laberintos",variable=s.Opcion_Tablero,value=0)
        s.Rbtn_Laberintos.place(x=POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        
        s.Rbtn_Terrenos=Radiobutton(s,text="Terrenos",variable=s.Opcion_Tablero,value=1)
        s.Rbtn_Terrenos.place(x=POS_X+ANCHO+10, y=POS_Y, width=ANCHO, height=ALTURA)
        
        s.Cbtn_Libre = Checkbutton(
            s, text="Modo Libre", variable=s.Opcion_Libre, onvalue=1, offvalue=0)
        s.Cbtn_Libre.place(x=POS_X+(ANCHO*5)+10, y=POS_Y, width=ANCHO+20, height=ALTURA)
        

    def active(s):
        s.Rbtn_Laberintos.config(state="active")
        s.Rbtn_Terrenos.config(state="active")
        s.Cbtn_Libre.config(state="active")

    def disabled(s):
        s.Rbtn_Laberintos.config(state="disabled")
        s.Rbtn_Terrenos.config(state="disabled")
        s.Cbtn_Libre.config(state="disabled")

class LFPrincipal(LabelFrame):
    
    def __init__(s, master,modo_info=False):
        s.Width = 690
        s.Height = 200
        s.Bool_Info=modo_info
        # Constructor de Frame()
        super().__init__(master,text="Principal", width=s.Width, height=s.Height, background=COLOR_7)
        
        s.AlgoritmoNoInfo = IntVar()
        s.AlgoritmoInfo = IntVar()
        s.OpcionRecorrido = IntVar()
        s.VistaAgente = BooleanVar()
        s.Automatico = BooleanVar()
        
        s.__comboBox(350,105)
        s.__entradaOrigenDestino(10,10)
        s.__ordenEstados(230,10)
        if s.Bool_Info:
            s.__opcionesAlgoritmInfo(360, 10)
        else:
            s.__opcionesAlgoritmNoInfo(360, 10)
        s.__opcionesRecorridos(450,10)
        s.__otros(560,10)
        
        s.active()
        
        s.pack()
    
    def __comboBox(s,POS_X:int,POS_Y:int):
        ANCHO = 150
        ALTURA = 30
        s.Cbx_Archivos_Txt=Combobox(s,state="readonly")
        s.Cbx_Archivos_Txt.place(x=POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        
    def __opcionesAlgoritmNoInfo(s,POS_X:int,POS_Y:int):
        ANCHO = 80
        ALTURA = 30
        s.Rbtn_A_BFS=Radiobutton(s,text="BFS",variable=s.AlgoritmoNoInfo,value=0)
        s.Rbtn_A_BFS.place(x=POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        
        s.Rbtn_A_DFS=Radiobutton(s,text="DFS",variable=s.AlgoritmoNoInfo,value=1)
        s.Rbtn_A_DFS.place(x=POS_X, y=ALTURA+POS_Y, width=ANCHO, height=ALTURA)
        
        s.Rbtn_A_DFS_R=Radiobutton(s,text="DFS_R",variable=s.AlgoritmoNoInfo,value=2)
        s.Rbtn_A_DFS_R.place(x=POS_X, y=(ALTURA*2)+POS_Y, width=ANCHO, height=ALTURA)
    
    def __opcionesAlgoritmInfo(s, POS_X: int, POS_Y: int):
        ANCHO = 80
        ALTURA = 30
        s.Rbtn_A_Voraz=Radiobutton(s,text="Voraz",variable=s.AlgoritmoInfo,value=0)
        s.Rbtn_A_Voraz.place(x=POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        
        s.Rbtn_A_AE=Radiobutton(s,text="A*",variable=s.AlgoritmoInfo,value=1)
        s.Rbtn_A_AE.place(x=POS_X, y=ALTURA+POS_Y, width=ANCHO, height=ALTURA)
        
    def __entradaOrigenDestino(s,POS_X:int,POS_Y:int):
        ANCHO = 70
        ALTURA = 30
        
        s.lbl1 = Label(s, text="Origen")
        s.lbl1.place(x=POS_X, y=ALTURA+POS_Y, width=ANCHO, height=ALTURA)
        s.lbl2 = Label(s, text="Destino")
        s.lbl2.place(x=POS_X, y=ALTURA+ALTURA+POS_Y, width=ANCHO, height=ALTURA)
        
        s.lbl3 = Label(s, text="Fila")
        s.lbl3.place(x=ANCHO+POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        s.lbl4 = Label(s, text="Columna")
        s.lbl4.place(x=ANCHO+ANCHO+POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        
        s.Fila_Origen = Combobox(s,state="readonly")
        s.Fila_Origen.place(x=ANCHO+POS_X, y=ALTURA+POS_Y, width=ANCHO, height=ALTURA)

        s.Fila_Destino = Combobox(s, state="readonly")
        s.Fila_Destino.place(x=ANCHO+POS_X, y=ALTURA+ALTURA+POS_Y, width=ANCHO, height=ALTURA)
        
        s.Columna_Origen = Combobox(s, state="readonly")
        s.Columna_Origen.place(x=ANCHO+ANCHO+POS_X, y=ALTURA+POS_Y, width=ANCHO, height=ALTURA)

        s.Columna_Destino = Combobox(s, state="readonly")
        s.Columna_Destino.place(x=ANCHO+ANCHO+POS_X, y=ALTURA+ALTURA+POS_Y, width=ANCHO, height=ALTURA)
        
        s.Btn_Cargar = Button(s, text="Cargar")
        s.Btn_Cargar.place(x=POS_X, y=5+(ALTURA*3)+POS_Y, width=ANCHO*3, height=ALTURA)
        
    def __opcionesRecorridos(s,POS_X: int, POS_Y: int):
        ANCHO = 100
        ALTURA = 30
        s.Rbtn_Camino=Radiobutton(s,text="Camino",variable=s.OpcionRecorrido,value=0)
        s.Rbtn_Camino.place(x=POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        
        s.Rbtn_Nodos=Radiobutton(s,text="Nodos",variable=s.OpcionRecorrido,value=1)
        s.Rbtn_Nodos.place(x=POS_X, y=ALTURA+POS_Y, width=ANCHO, height=ALTURA)
        
        s.Rbtn_Estados=Radiobutton(s,text="Estados",variable=s.OpcionRecorrido,value=2)
        s.Rbtn_Estados.place(x=POS_X, y=ALTURA+ALTURA+POS_Y, width=ANCHO, height=ALTURA)

    def __ordenEstados(s,POS_X:int,POS_Y:int):
        
        ANCHO = 30
        ALTURA = 30
        
        s.Btn_Orden_Reiniciar = Button(
            s, text="Reiniciar Orden", command=s.__Orden_Reiniciar)
        s.Btn_Orden_Reiniciar.place(x=POS_X, y=POS_Y, width=ANCHO*4, height=ALTURA)
        
        s.Btn_Orden_L = Button(s, text="L",command=s.__Set_Orden_L)
        s.Btn_Orden_L.place(x=POS_X  , y=POS_Y+ALTURA,  width=ANCHO, height=ALTURA)
        
        s.Btn_Orden_R = Button(s, text="R", command=s.__Set_Orden_R)
        s.Btn_Orden_R.place(x=POS_X+(ANCHO), y=POS_Y+ALTURA, width=ANCHO, height=ALTURA)
        
        s.Btn_Orden_U = Button(s, text="U", command=s.__Set_Orden_U)
        s.Btn_Orden_U.place(x=POS_X+(ANCHO*2), y=POS_Y+ALTURA, width=ANCHO, height=ALTURA)
        
        s.Btn_Orden_D = Button(s, text="D", command=s.__Set_Orden_D)
        s.Btn_Orden_D.place(x=POS_X+(ANCHO*3), y=POS_Y+ALTURA, width=ANCHO, height=ALTURA)
        
        s.Lbl_Estado_Orden=Label(s,text="")
        s.Lbl_Estado_Orden.place(x=POS_X, y=POS_Y+(ALTURA*2), width=ANCHO*4, height=ALTURA)

    def __Orden_Reiniciar(s):
        s.Lbl_Estado_Orden.config(text="")
        s.Btn_Orden_L.config(state="active")
        s.Btn_Orden_R.config(state="active")
        s.Btn_Orden_U.config(state="active")
        s.Btn_Orden_D.config(state="active")

    def __Set_Orden_L(s):
        s.Lbl_Estado_Orden.config(text=s.Lbl_Estado_Orden.cget(
            "text")+s.Btn_Orden_L.cget("text"))
        s.Btn_Orden_L.config(state="disabled")

    def __Set_Orden_R(s):
        s.Lbl_Estado_Orden.config(text=s.Lbl_Estado_Orden.cget(
            "text")+s.Btn_Orden_R.cget("text"))
        s.Btn_Orden_R.config(state="disabled")

    def __Set_Orden_U(s):
        s.Lbl_Estado_Orden.config(text=s.Lbl_Estado_Orden.cget(
            "text")+s.Btn_Orden_U.cget("text"))
        s.Btn_Orden_U.config(state="disabled")

    def __Set_Orden_D(s):
        s.Lbl_Estado_Orden.config(text=s.Lbl_Estado_Orden.cget(
            "text")+s.Btn_Orden_D.cget("text"))
        s.Btn_Orden_D.config(state="disabled")
    
    def __otros(s, POS_X: int, POS_Y: int):
        ANCHO = 120
        ALTURA = 30
        
        s.Cbtn_Vista_Agente = Checkbutton(
            s, text="Vista Agente", variable=s.VistaAgente, onvalue=1, offvalue=0)
        s.Cbtn_Vista_Agente.place(x=POS_X, y=POS_Y, width=ANCHO, height=ALTURA)

        s.Cbtn_Automatico = Checkbutton(
            s, text="Automatico", variable=s.Automatico, onvalue=1, offvalue=0)
        s.Cbtn_Automatico.place(x=POS_X, y=ALTURA+POS_Y,width=ANCHO, height=ALTURA)
        
    def active(s):
        s.Cbx_Archivos_Txt.config(state="normal")
        s.Cbtn_Automatico.config(state="active")
        s.Cbtn_Vista_Agente.config(state="active")
        
        s.Btn_Cargar.config(state="active")

        s.Fila_Origen.config(state="normal")
        s.Columna_Origen.config(state="normal")

        s.Fila_Destino.config(state="normal")
        s.Columna_Destino.config(state="normal")

        if s.Bool_Info:
            s.Rbtn_A_Voraz.config(state="active")
            s.Rbtn_A_AE.config(state="active")
        else:
            s.Rbtn_A_BFS.config(state="active")
            s.Rbtn_A_DFS.config(state="active")
            s.Rbtn_A_DFS_R.config(state="active")
            
        s.Rbtn_Camino.config(state="active")
        s.Rbtn_Nodos.config(state="active")
        s.Rbtn_Estados.config(state="active")

        s.Cbtn_Vista_Agente.config(state="active")
        s.Cbtn_Automatico.config(state="active")

        s.Btn_Orden_Reiniciar.config(state="active")
        
    def disabled(s):
        s.Cbx_Archivos_Txt.config(state="disabled")
        s.Cbtn_Automatico.config(state="disabled")
        s.Cbtn_Vista_Agente.config(state="disabled")
        
        s.Btn_Cargar.config(state="disabled")

        s.Fila_Origen.config(state="disabled")
        s.Columna_Origen.config(state="disabled")

        s.Fila_Destino.config(state="disabled")
        s.Columna_Destino.config(state="disabled")

        
        if s.Bool_Info:
            s.Rbtn_A_Voraz.config(state="disabled")
            s.Rbtn_A_AE.config(state="disabled")
        else:
            s.Rbtn_A_BFS.config(state="disabled")
            s.Rbtn_A_DFS.config(state="disabled")
            s.Rbtn_A_DFS_R.config(state="disabled")
            
        s.Rbtn_Camino.config(state="disabled")
        s.Rbtn_Nodos.config(state="disabled")
        s.Rbtn_Estados.config(state="disabled")

        s.Cbtn_Vista_Agente.config(state="disabled")
        s.Cbtn_Automatico.config(state="disabled")

        s.Btn_Orden_Reiniciar.config(state="disabled")

class LFAutomatico(LabelFrame):
    
    def __init__(s, master):
        s.Width = 330
        s.Height = 140
        # Constructor de Frame()
        super().__init__(master,text="Automatico", width=s.Width, height=s.Height, background=COLOR_3)
        
        s.__controles(10,10)
        
        s.pack()
        
    def __controles(s, POS_X: int, POS_Y: int):
        ANCHO = 100
        ALTURA = 40
        s.Btn_Iniciar = Button(s, text="Iniciar")
        s.Btn_Iniciar.place(x=POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        s.Btn_Pausar = Button(s, text="Pausar")
        s.Btn_Pausar.place(x=ANCHO+POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        s.Btn_Cancelar = Button(s, text="Cancelar")
        s.Btn_Cancelar.place(x=ANCHO+ANCHO+POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        
        s.Scale_Velocidad = Scale(s, orient="horizontal",from_=0.01,to=4.0,resolution=0.05)
        s.Scale_Velocidad.place(x=POS_X, y=10+ALTURA+POS_Y, width=ANCHO*3, height=ALTURA)
    
    def active(s):
        s.Btn_Iniciar.config(state="active")
        s.Btn_Pausar.config(state="active")
        s.Btn_Cancelar.config(state="active")
        
        s.Scale_Velocidad.config(state="active")
    
    def disabled(s):
        s.Btn_Iniciar.config(state="disabled")
        s.Btn_Pausar.config(state="disabled")
        s.Btn_Cancelar.config(state="disabled")
        
        s.Scale_Velocidad.config(state="disabled")

class LFManual(LabelFrame):
    
    def __init__(s, master):
        s.Width = 330
        s.Height = 90
        # Constructor de Frame()
        super().__init__(master,text="Manual", width=s.Width, height=s.Height, background=COLOR_4)
        
        s.__controles(10,10)
        
        s.pack()
        
    def __controles(s, POS_X: int, POS_Y: int):
        ANCHO=100
        ALTURA=40
        s.Btn_Back = Button(s, text="<==Back==")
        s.Btn_Back.place(x=POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        s.Btn_Next = Button(s, text="==Next==>")
        s.Btn_Next.place(x=ANCHO+POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        s.Btn_Cancelar = Button(s, text="Cancelar")
        s.Btn_Cancelar.place(x=(ANCHO*2)+POS_X, y=POS_Y, width=ANCHO, height=ALTURA)

    def active(s):
        s.Btn_Back.config(state="active")
        s.Btn_Next.config(state="active")
        s.Btn_Cancelar.config(state="active")
        
    def disabled(s):
        s.Btn_Back.config(state="disabled")
        s.Btn_Next.config(state="disabled")
        s.Btn_Cancelar.config(state="disabled")
        
class LFLibre(LabelFrame):
    
    def __init__(s, master):
        s.Width = 150
        s.Height = 150
        # Constructor de Frame()
        super().__init__(master,text="Direccion", width=s.Width, height=s.Height, background=COLOR_5)
        s.__controles(10,10)
        
        s.pack()

    def __controles(s, POS_X: int, POS_Y: int):
        LADO = 40
        s.Btn_L = Button(s, text="L")
        s.Btn_L.place(x=POS_X, y=POS_Y+LADO, width=LADO, height=LADO)
        s.Btn_R = Button(s, text="R")
        s.Btn_R.place(x=(LADO*2)+POS_X, y=POS_Y+LADO, width=LADO, height=LADO)
        s.Btn_U = Button(s, text="U")
        s.Btn_U.place(x=LADO+POS_X, y=POS_Y, width=LADO, height=LADO)
        s.Btn_D = Button(s, text="D")
        s.Btn_D.place(x=LADO+POS_X, y=POS_Y+LADO, width=LADO, height=LADO)
        
    def active(s):
        s.Btn_L.config(state="active")
        s.Btn_R.config(state="active")
        s.Btn_U.config(state="active")
        s.Btn_D.config(state="active")

    def disabled(s):
        s.Btn_L.config(state="disabled")
        s.Btn_R.config(state="disabled")
        s.Btn_U.config(state="disabled")
        s.Btn_D.config(state="disabled")

class LFArbol(LabelFrame):
    
    def __init__(s, master):
        s.Width = 100
        s.Height = 100
        # Constructor de Frame()
        super().__init__(master,text="Arbol", width=s.Width, height=s.Height, background=COLOR_9)
        
        s.pack()
class Controls(Frame):

    def __init__(s, master):
        # Constructor de Frame()
        super().__init__(master, width=710, height=650, background=COLOR_6)

        # empaquetando elementos dentro de su ventana contenedora
        s.Menu = LFMenu(s)
        s.Menu.place(x=10, y=10)
        # s.Menu.Rbtn_Laberintos.config(command=s.updateWidgets)
        # s.Menu.Rbtn_Terrenos.config(command=s.updateWidgets)
        s.updateWidgets()
        
        s.pack()
        
    def updateWidgets(s):
        s.Principal=None
        
        if s.Menu.Opcion_Tablero.get()==0:
            s.Principal = LFPrincipal(s)
            s.Principal.place(x=10, y=100)
        elif s.Menu.Opcion_Tablero.get() == 1:
            s.Principal = LFPrincipal(s, True)
            s.Principal.place(x=10, y=100)
        
        s.Auto=LFAutomatico(s)
        s.Auto.place(x=10,y=310)
        s.Auto.disabled()
        
        s.Manual=LFManual(s)
        s.Manual.place(x=350,y=310)
        s.Manual.disabled()
        
        s.Arbol=LFArbol(s)
        s.Arbol.place(x=10,y=460)
        # s.pack()
        
    #     s.__pruebas()
    
    # def __pruebas(s):
    #     s.Principal.Btn_Cargar.config(command=s.cargar)
    #     s.Manual.Btn_Cancelar.config(command=s.cancelar)
    #     s.Auto.Btn_Cancelar.config(command=s.cancelar)
        
    def cargar(s):
        if not len(s.Principal.Lbl_Estado_Orden["text"]) == 4:
            return
        
        s.Principal.disabled()
        if s.Principal.Automatico.get():
            s.Auto.active()
        else:
            s.Manual.active()
            
    def cancelar(s):

        s.Principal.active()
        if s.Principal.Automatico.get():
            s.Auto.disabled()
        else:
            s.Manual.disabled()
            
    

if __name__ == '__main__':
    root=Tk()
    root.title("Controles Laberinto")
    app=Controls(root)
    app.mainloop()
    
    # root=Tk()
    # root.title("Controles Laberinto")
    # app=LFDireccion(root)
    # app.mainloop()
    
    
