
from math import floor
import numpy as np
from tkinter import ALL, Canvas, Frame, Tk
from Constantes import *


class LaberintoFrame(Frame):
    
    def __init__(self,master:Tk,cells_side:int,size_px:int) -> None:
        super().__init__(master,width=size_px,height=size_px)
        # Tamaño del canva en pixeles
        self.SizePX=size_px
        # Tamaño del canvas en celdas
        self.CellsSide=cells_side
        # Tamaño de la celda en pixeles (calculo automatico)
        # lado_celula=lado_canvas/num_celulas
        self.SideCellPX = self.SizePX/self.CellsSide
        
        # self.LaberintoMatrix=np.zeros((self.CellsSide,self.CellsSide),dtype=int)
        
        # empaquetando elementos dentro de su ventana contenedora
        self.createWidgets()
        self.drawLaberinto()
        self.pack()
        
    def createWidgets(self):
        self.canva=Canvas(self,width=self.SizePX,height=self.SizePX,background=WHITE)
        self.canva.pack()
        
    def _drawCell(self,x0,y0,x1,y1,color):
        self.canva.create_rectangle(x0,y0,x1,y1,fill=color,outline=BLACK)
    
    def drawLaberinto(self,color=WHITE):
        self.canva.delete("all")
        # limpia la memoria, esto para evitar que se tarde y trabe el programa
        self.canva.delete("all")
        for f in range(0,self.CellsSide):
            for c in range(0,self.CellsSide):
                # se dibuja la celda en blanco
                self._drawCell(c*self.SideCellPX,f*self.SideCellPX,(c*self.SideCellPX)+self.SideCellPX,(f*self.SideCellPX)+self.SideCellPX,color)
        self.canva.pack() # no quitar esta linea
        
    def drawHideLaberinto(self):
        self.drawLaberinto(BLACK)
        
    def drawTraceAgent(self, f: int, c: int,color):
        # self.canva.delete("all")
        self._drawCell(c*self.SideCellPX,f*self.SideCellPX,(c*self.SideCellPX)+self.SideCellPX,(f*self.SideCellPX)+self.SideCellPX,color)
        
    def drawAgent(self,f:int,c:int,color):
        # self.canva.delete("all")
        self.canva.create_rectangle(c*self.SideCellPX,f*self.SideCellPX,(c*self.SideCellPX)+self.SideCellPX,(f*self.SideCellPX)+self.SideCellPX,fill=color,outline=BLACK)
        self.canva.create_line(c*self.SideCellPX,f*self.SideCellPX,(c*self.SideCellPX)+self.SideCellPX,(f*self.SideCellPX)+self.SideCellPX)
        self.canva.create_line(c*self.SideCellPX,(f*self.SideCellPX)+self.SideCellPX,(c*self.SideCellPX)+self.SideCellPX,f*self.SideCellPX)
            
        self.canva.pack() # no quitar esta linea
# root=Tk()
# root.title("Ejemplo de canvas")
# app=Laberinto(root,20,500)
# app.drawMatrix()
# app.mainloop()