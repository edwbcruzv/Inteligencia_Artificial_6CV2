from tkinter import BooleanVar, Checkbutton, IntVar, PhotoImage, Radiobutton, Tk, Label, Frame, Entry, Button, Scale
from tkinter.ttk import Combobox


class Controls(Frame):

    def __init__(s, master):
        # Constructor de Frame()
        super().__init__(master, width=580, height=440, background="gray")

        # s.InverterColorCells = BooleanVar()
        # s.OptionBorder = IntVar()
        
        s.AlgoritmoNoInfo = IntVar()
        s.AlgoritmoInfo = IntVar()
        s.OpcionRecorrido = IntVar()
        s.VistaAgente = BooleanVar()
        s.Automatico = BooleanVar()

        # empaquetando elementos dentro de su ventana contenedora
        s.createWidgets()
        s.pack()
        s.reiniciar()
        
        
    def reiniciar(s):
        s.Automatico.set(True)
        s.automatico()
        s.Cbtn_Automatico.config(state="disabled")
        s.Cbtn_Vista_Agente.config(state="disabled")
        s.Btn_Iniciar.config(state="disabled")
        s.Btn_Pausar.config(state="disabled")
        s.Btn_Cancelar.config(state="disabled")
        
        s.Btn_Cargar.config(state="active")
        
        s.Fila_Origen.config(state="normal")
        s.Columna_Origen.config(state="normal")

        s.Fila_Destino.config(state="normal")
        s.Columna_Destino.config(state="normal")
        
        s.Scale_Velocidad.config(state="active")

        s.Rbtn_A_Voraz.config(state="active")
        s.Rbtn_A_AE.config(state="active")

        s.Rbtn_Camino.config(state="active")
        s.Rbtn_Nodos.config(state="active")
        s.Rbtn_Estados.config(state="active")
        
        s.Cbtn_Vista_Agente.config(state="active")
        s.Cbtn_Automatico.config(state="active")
        
        s.Btn_Orden_Reiniciar.config(state="active")
        # s.Btn_Orden_L.config(state="active")
        # s.Btn_Orden_R.config(state="active")
        # s.Btn_Orden_U.config(state="active")
        # s.Btn_Orden_D.config(state="active")
        
    def cargar(s):
        s.automatico()
        s.Cbtn_Automatico.config(state="active")
        s.Cbtn_Vista_Agente.config(state="active")
        
        s.Btn_Iniciar.config(state="active")
        s.Btn_Pausar.config(state="active")
        s.Btn_Cancelar.config(state="active")
        
        s.Btn_Cargar.config(state="disabled")
        
        s.Fila_Origen.config(state="disabled")
        s.Columna_Origen.config(state="disabled")
        
        s.Fila_Destino.config(state="disabled")
        s.Columna_Destino.config(state="disabled")
        
        s.Scale_Velocidad.config(state="disabled")
        
        s.Rbtn_A_Voraz.config(state="disabled")
        s.Rbtn_A_AE.config(state="disabled")
        
        s.Rbtn_Camino.config(state="disabled")
        s.Rbtn_Nodos.config(state="disabled")
        s.Rbtn_Estados.config(state="disabled")
        
        s.Cbtn_Vista_Agente.config(state="disabled")
        s.Cbtn_Automatico.config(state="disabled")
        
        s.Btn_Orden_Reiniciar.config(state="disabled")

    # Aqui se crean todos los widgets del frame
    def createWidgets(s):
        tabla = PhotoImage(file="Borrame.png")
        imagen = Label(s, image=tabla)
        imagen.place(x=130, y=10)
        
        s.__controles1()
        s.__controles2()
        s.__controles3()
        s.__controles4()
        s.__controles5()
        s.__controles6()
        s.__controles7()
        s.__controles8()
        
    
    def __controles1(s):
        LADO1=40
        POS_X = 340
        POS_Y = 490
        s.Btn_L=Button(s,text="L")
        s.Btn_L.place(x=POS_X, y=POS_Y, width=LADO1, height=LADO1)
        s.Btn_R = Button(s, text="R")
        s.Btn_R.place(x=LADO1+LADO1+POS_X, y=POS_Y, width=LADO1, height=LADO1)
        s.Btn_U=Button(s,text="U")
        s.Btn_U.place(x=LADO1+POS_X, y=POS_Y-LADO1, width=LADO1, height=LADO1)
        s.Btn_D=Button(s,text="D")
        s.Btn_D.place(x=LADO1+POS_X, y=POS_Y, width=LADO1, height=LADO1)
        
        
    def __controles2(s):
        ANCHO=100
        ALTURA=40
        POS_X = 200
        POS_Y = 380
        s.Btn_Back = Button(s, text="<==Back==")
        s.Btn_Back.place(x=ANCHO+POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        s.Btn_Next = Button(s, text="==Next==>")
        s.Btn_Next.place(x=ANCHO+ANCHO+POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
    
    def __controles3(s):
        ANCHO = 100
        ALTURA = 40
        POS_X = 250
        POS_Y = 130 +200
        s.Btn_Iniciar = Button(s, text="Iniciar")
        s.Btn_Iniciar.place(x=POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        s.Btn_Pausar = Button(s, text="Pausar")
        s.Btn_Pausar.place(x=ANCHO+POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        s.Btn_Cancelar = Button(s, text="Cancelar")
        s.Btn_Cancelar.place(x=ANCHO+ANCHO+POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        
    
    def __controles4(s):
        ANCHO = 120
        ALTURA = 30
        POS_X = 450
        POS_Y = 200
        
        s.Cbtn_Vista_Agente = Checkbutton(
            s, text="Vista Agente", variable=s.VistaAgente, onvalue=1, offvalue=0)
        s.Cbtn_Vista_Agente.place(x=POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        
        s.Cbtn_Automatico = Checkbutton(
            s, text="Automatico", variable=s.Automatico, onvalue=1, offvalue=0)
        s.Cbtn_Automatico.place(x=POS_X, y=ALTURA+POS_Y, width=ANCHO, height=ALTURA)
        
    def automatico(s):
        if s.Automatico.get():
            s.Btn_L.config(state="disabled")
            s.Btn_R.config(state="disabled")
            s.Btn_U.config(state="disabled")
            s.Btn_D.config(state="disabled")
            s.Btn_Back.config(state="disabled")
            s.Btn_Next.config(state="disabled")
        else:
            s.Btn_L.config(state="active")
            s.Btn_R.config(state="active")
            s.Btn_U.config(state="active")
            s.Btn_D.config(state="active")
            s.Btn_Back.config(state="active")
            s.Btn_Next.config(state="active")
            
    def __controles5(s):
        ANCHO = 80
        ALTURA = 30
        POS_X = 250
        POS_Y = 200
        s.Rbtn_A_Voraz=Radiobutton(s,text="Voraz",variable=s.AlgoritmoNoInfo,value=0)
        s.Rbtn_A_Voraz.place(x=POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        
        s.Rbtn_A_AE=Radiobutton(s,text="A*",variable=s.AlgoritmoNoInfo,value=1)
        s.Rbtn_A_AE.place(x=POS_X, y=ALTURA+POS_Y, width=ANCHO, height=ALTURA)
        
    def __controles6(s):
        ANCHO = 70
        ALTURA = 30
        POS_X = 10
        POS_Y = 200
        
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
        
        s.Scale_Velocidad = Scale(s, orient="horizontal",from_=0.01,to=4.0,resolution=0.05)
        s.Scale_Velocidad.place(x=10, y=10+(ALTURA*4)+POS_Y, width=ANCHO*3, height=40)
        
    def __controles7(s):
        ANCHO = 100
        ALTURA = 30
        POS_X = 340
        POS_Y = 200
        s.Rbtn_Camino=Radiobutton(s,text="Camino",variable=s.OpcionRecorrido,value=0)
        s.Rbtn_Camino.place(x=POS_X, y=POS_Y, width=ANCHO, height=ALTURA)
        
        s.Rbtn_Nodos=Radiobutton(s,text="Nodos",variable=s.OpcionRecorrido,value=1)
        s.Rbtn_Nodos.place(x=POS_X, y=ALTURA+POS_Y, width=ANCHO, height=ALTURA)
        
        s.Rbtn_Estados=Radiobutton(s,text="Estados",variable=s.OpcionRecorrido,value=2)
        s.Rbtn_Estados.place(x=POS_X, y=ALTURA+ALTURA+POS_Y, width=ANCHO, height=ALTURA)
        
    def __controles8(s):
        
        ANCHO = 30
        ALTURA = 30
        POS_X = 10
        POS_Y = 20
        
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
        s.Lbl_Estado_Orden.config(text=s.Lbl_Estado_Orden.cget("text")+s.Btn_Orden_L.cget("text"))
        s.Btn_Orden_L.config(state="disabled")
    def __Set_Orden_R(s):
        s.Lbl_Estado_Orden.config(text=s.Lbl_Estado_Orden.cget("text")+s.Btn_Orden_R.cget("text"))
        s.Btn_Orden_R.config(state="disabled")
    def __Set_Orden_U(s):
        s.Lbl_Estado_Orden.config(text=s.Lbl_Estado_Orden.cget("text")+s.Btn_Orden_U.cget("text"))
        s.Btn_Orden_U.config(state="disabled")
    def __Set_Orden_D(s):
        s.Lbl_Estado_Orden.config(text=s.Lbl_Estado_Orden.cget("text")+s.Btn_Orden_D.cget("text"))
        s.Btn_Orden_D.config(state="disabled")
        
if __name__ == '__main__':
    root=Tk()
    root.title("Controles Laberinto")
    app=Controls(root)
    app.mainloop()
