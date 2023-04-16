
from math import floor
import numpy as np
from tkinter import ALL, Canvas, Frame, Tk
from Constantes import *


class TableroFrame(Frame):
    
    def __init__(self,master:Tk,matrix_laberinto,cells_side:int,size_px:int) -> None:
        super().__init__(master,width=size_px,height=size_px)
        # Tamaño del canva en pixeles
        self.SizePX=size_px
        # Tamaño del canvas en celdas
        self.CellsSide=cells_side
        # Tamaño de la celda en pixeles (calculo automatico)
        # lado_celula=lado_canvas/num_celulas
        self.SideCellPX = round(self.SizePX/self.CellsSide,2)
        
        self.Matrix_Laberinto=matrix_laberinto
        # self.LaberintoMatrix=np.zeros((self.CellsSide,self.CellsSide),dtype=int)
        
        self.Matrix_Explorer=np.zeros(self.Matrix_Laberinto.shape,dtype=int)
        self.Filas, self.Columnas = self.Matrix_Laberinto.shape
        
        self.CoordsAgent=(None,None)
        self.Orientation=(None,None)
        # empaquetando elementos dentro de su ventana contenedora
        self.createWidgets()
        self.pack()
        self.clear()
        
    def setCordsAgent(self, f: int, c: int):
        self.CoordsAgent=(f,c)
        
    def getCordsAgent(self):
        return self.CoordsAgent[0], self.CoordsAgent[1]
    
    def setOrientation(self, f: int, c: int):
        self.Orientation = (f, c)

    def getOrientation(self):
        return self.Orientation[0], self.Orientation[1]
        
    def createWidgets(self):
        self.canva=Canvas(self,width=self.SizePX,height=self.SizePX,background=WHITE)
        self.canva.pack()
        
        
    
        # pinta una cuadro y la dibujar usando el metodo directo de canvas
    def __drawCell(self,x0,y0,x1,y1,fill,outline):
        self.canva.create_rectangle(x0,y0,x1,y1,fill=fill,outline=outline)
    
        # realiza el calculo para dibujar los cuadros correspondientes a una coordenada recibida
    def drawCellCord(self, f: int, c: int, fill,outline=None):
        self.__drawCell(c*self.SideCellPX,f*self.SideCellPX,(c*self.SideCellPX)+self.SideCellPX,(f*self.SideCellPX)+self.SideCellPX,fill,outline)
    
        # Solo se recibe la coordenada, ya que el color los buscara solo
    def __paintCellCord(self, f: int, c: int):
        if self.Matrix_Laberinto[f][c]==1:
            self.drawCellCord(f, c, GRAY, BLACK)
        else:
            self.drawCellCord(f, c, WHITE, BLACK)
    
    def __paintTablero(self,color):
        self.canva.delete("all")
        for f in range(0, self.CellsSide):
            for c in range(0, self.CellsSide):
                self.drawCellCord(f, c,color)
        self.canva.pack()  # no quitar esta linea
    
        # renderiza el laberinto
    def render(self):
        self.canva.delete("all")
        for f in range(0, self.CellsSide):
            for c in range(0, self.CellsSide):
                self.__paintCellCord(f,c)
        self.canva.pack()  # no quitar esta linea
        
        # oculta el laberinto
    def hide(self):
        self.__paintTablero(BLACK)
        
        # Limpia el laberitno
    def clear(self):
        self.CoordsAgent = (None, None)
        self.Orientation = (None, None)
        self.Matrix_Explorer=np.zeros(self.Matrix_Laberinto.shape,dtype=int)
        self.__paintTablero(BLACK)
        
        # indicara donde esta el agente
        
    def __paintCellsNeighbors(self,f: int, c: int):
        if c-1 >= 0 :
            self.__paintCellCord(f ,c-1)
        if c+1 < self.Columnas :
            self.__paintCellCord(f ,c+1)
        if f-1 >= 0:
            self.__paintCellCord(f-1 ,c)
        if f+1 < self.Filas:
            self.__paintCellCord(f+1 ,c)
    
    # def __paintCellOrientation(self, f: int, c: int):
    #     if c-1 >= 0 and orientation == 'L':
    #         self.__paintCellCord(f, c-1)
    #     elif c+1 < self.Columnas and orientation == 'R':
    #         self.__paintCellCord(f, c+1)
    #     elif f-1 >= 0 and orientation == 'U':
    #         self.__paintCellCord(f-1, c)
    #     elif f+1 < self.Filas and orientation == 'D':
    #         self.__paintCellCord(f+1, c)
            
    def drawAgent(self,f:int,c:int,orientation:bool=False):
        f_aux,c_aux=self.getCordsAgent()
        
        if f_aux!=None and c_aux!=None:
            self.__paintCellCord(f_aux, c_aux)
        self.Matrix_Explorer[f][c]=1
        self.setCordsAgent(f,c)
        
        if orientation:
            print(self.CoordsAgent,orientation)
            self.__paintCellsNeighbors(f,c)
        
        self.__paintCellCord(f, c)
        self.canva.create_line(c*self.SideCellPX,f*self.SideCellPX,(c*self.SideCellPX)+self.SideCellPX,(f*self.SideCellPX)+self.SideCellPX)
        self.canva.create_line(c*self.SideCellPX,(f*self.SideCellPX)+self.SideCellPX,(c*self.SideCellPX)+self.SideCellPX,f*self.SideCellPX)
            
        self.canva.pack() # no quitar esta linea


        
if __name__ == '__main__':
    root=Tk()
    root.title("Ejemplo de canvas")
    app=TableroFrame(root,np.zeros((20,20),dtype=int),20,700)
    app.render()
    app.mainloop()
    