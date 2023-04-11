from tkinter import Frame
import numpy as np
from LaberintoFrame import *
from LaberintoTemplate import *
from Constantes import *
from Agente import *

class Window(Frame):
    
    
    def __init__(s,master,width:int,height:int):
        # Constructor de Frame()
        super().__init__(master,width=width,height=height,background="gray")
        # empaquetando elementos dentro de su ventana contenedora
        s.createWidgets()
        s.pack()
        
        s.createAgent()
    
    def createAgent(s):
        
        s.agente=Agente(origen=(10,'A'),destino=(2,'O'),color=COLOR_3)
        print(s.agente.Problema)
        print(s.agente.Arbol_Solucion)
        s.agente.calcula()
        
        print([nodo.__str__() for nodo in s.agente.Trayectoria])
        print(s.agente.Lista_Camino)
        
        
        s.laberinto_canvas.drawHideLaberinto()
        s.laberinto_canvas.drawTraceAgent(s.agente.F,s.agente.C,s.agente.Color)
        
    # Aqui se crean todos los widgets del frame
    def createWidgets(s):
        
        # se define el tamaño estatico del canvas en pixeles y la posicion
        s.laberinto_canvas=LaberintoFrame(master=s,cells_side=15,size_px=700)
        s.laberinto_canvas.place(relx=0.5,rely=0.01)
        
        
        
        
root = Tk()
root.title("Ventana Principal")
app = Window(root, 1500, 750)
app.mainloop()
