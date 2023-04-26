
from math import floor
import numpy as np
from tkinter import ALL, Canvas, Frame, Tk

COLOR_1="#17202A"
COLOR_2="#6E2C00"
COLOR_3="#CA6F1E"
COLOR_4="#7D6608"
COLOR_5="#2ECC71"
COLOR_6="#0B5345"
COLOR_7="#3498DB"
COLOR_8="#154360"
COLOR_9="#4A235A"
COLOR_10="#4B235A"
RED="#7B241C"
WHITE="#FFF"
BLACK="#000"

class Laberinto(Frame):
    
    def __init__(self,master:Tk,cells_side:int,size_px:int) -> None:
        super().__init__(master,width=size_px,height=size_px)
        # Tamaño del canva en pixeles
        self.SizePX=size_px
        # Tamaño del canvas en celdas
        self.CellsSide=cells_side
        # Tamaño de la celda en pixeles
        self.SideCellPX=None
        
        self.LaberintoMatrix=np.zeros((self.CellsSide,self.CellsSide),dtype=int)
        self.__Agentes=list()
        
        
        # empaquetando elementos dentro de su ventana contenedora
        self.createWidgets()
        self.pack()
        
    def createWidgets(self):
        self.canva=Canvas(self,width=self.SizePX,height=self.SizePX,background=WHITE)
        
        # self.canva.bind("<Button-1>",self._alterate) # clic izquierdo
        # self.canva.bind("<MouseWheel>", self.do_zoom)
        # self.canva.bind('<ButtonPress-3>', lambda event: self.canva.scan_mark(event.x, event.y))
        # self.canva.bind("<B3-Motion>", lambda event: self.canva.scan_dragto(event.x, event.y, gain=1))   
        # self.canva.bind('<space>', self.pausar)
        self.canva.pack()
    
    # def do_zoom(self, event):
    #     x = self.canva.canvasx(event.x)
    #     y = self.canva.canvasy(event.y)
    #     self.factor = 1.001 ** event.delta
    #     self.canva.scale(ALL, x, y, self.factor, self.factor)
    
    # def pausar(self):
    #     if not self.pausa:
    #         self.pausa = True
    #         self.boton_pausa.config(text="Play")
    #     else:
    #         self.pausa = False
    #         self.boton_pausa.config(text="Pausa")
            
    def drawMatrix(self):
        # Se calcula el lado del la celula 
        # lado_celula=lado_canvas/num_celulas
        self.SideCellPX=self.SizePX/self.CellsSide
        # limpia la memoria, esto para evitar que se tarde y trabe el programa
        self.canva.delete("all")
        try:
            self._drawLaberinto()
            #self._drawHeads()
        except :
            print("algo paso aqui")
    
    def _drawLaberinto(self):
        
        # c->columna: indicara la coodernada del eje X
        # f->fila: indicara la coordenada del eje Y
        # print(self.CellsSide)
        for f in range(0,self.CellsSide):
            for c in range(0,self.CellsSide):
                if self.LaberintoMatrix[f][c]==0:
                    # se dibuja la celda en blanco
                    self._drawCell(c*self.SideCellPX,f*self.SideCellPX,(c*self.SideCellPX)+self.SideCellPX,(f*self.SideCellPX)+self.SideCellPX,WHITE)
                else:
                    # se dibuja la celda correspondiente 
                    id_aux=int(self.LaberintoMatrix[f][c])
                    h_aux=self.Hormigas[self.Hormigas.index(id_aux)]
                    color=h_aux.Color
                    self._drawCell(c*self.SideCellPX,f*self.SideCellPX,(c*self.SideCellPX)+self.SideCellPX,(f*self.SideCellPX)+self.SideCellPX,color)
        
        self.canva.pack() # no quitar esta linea
        
    def _drawCell(self,x0,y0,x1,y1,color):
        self.canva.create_rectangle(x0,y0,x1,y1,fill=color,outline=BLACK)
        
    def _drawHeads(self):
        
        for a in self.Agentes:
            color=a.Color
            f=a.X_pos
            c=a.Y_pos
            self.canva.create_rectangle(c*self.SideCellPX,f*self.SideCellPX,(c*self.SideCellPX)+self.SideCellPX,(f*self.SideCellPX)+self.SideCellPX,fill=color,outline=BLACK)
            self.canva.create_line(c*self.SideCellPX,f*self.SideCellPX,(c*self.SideCellPX)+self.SideCellPX,(f*self.SideCellPX)+self.SideCellPX)
            self.canva.create_line(c*self.SideCellPX,(f*self.SideCellPX)+self.SideCellPX,(c*self.SideCellPX)+self.SideCellPX,f*self.SideCellPX)
            
        self.canva.pack() # no quitar esta linea
            
    def _alterate(self,event):
        var=(self.SizePX/self.CellsSide)
        c=floor(event.x/var)
        f=floor(event.y/var)
        try:
            if self.LaberintoMatrix[f][c]==0:
                h=self._RandomAnt(f,c)
                self.Hormigas.append(h)
                self._drawHeads()
            else:
                self.deleteAnt(int(self.LaberintoMatrix[f][c]))
                self._drawHeadsAnts()
        except:
            print("algo paso en alterar")
        
root=Tk()
root.title("Ejemplo de canvas")
app=Laberinto(root,20,500)
app.drawMatrix()
app.mainloop()