

class Agente:
    ID_int=0
     # celula y la orientacion
        #      0   1   2
        #    +---+---+---+
        #  0 |   | N |   |
        #    +---+---+---+
        #  1 | O |   | E |
        #    +---+---+---+
        #  2 |   | S |   |
        #    +---+---+---+
    
    def __init__(self,*args):
        
        if len(args)==1:
            self.__ID=args[0]
        elif len(args)==3:
            self.__Constructor1(args)
        else:
            return None
        
        
    def __Constructor1(self,args):
        # args=(color,orientation,position:list(2))
        if args[1] == 'N' or args[1] == 'E' or args[1] == 'O' or args[1] == 'S':
            self.__Orientation=args[1]
        else:
            print("Fallo 1")
            return None
        if len(args[2])==2:
            #(x:int,y:int)
            # print(position)
            self.__X_pos=int(args[2][0]) 
            self.__Y_pos=int(args[2][1])
        else:
            print("Fallo 2")
            return None
        
        self.__Color=args[0]
        self.__ID=self.generateID()
        self.__Evaluate=False
    
    @classmethod
    def generateID(cls):
        cls.ID_int+=1
        return cls.ID_int
    
    @classmethod
    def deleteID(cls):
        cls.ID_int-=1
    """
    #------------------------------------
    @property
    def Atributo(self):
        # Documentacion de Atributo 
        return self.__Atributo
    
    @Atributo.setter
    def Atributo(self,new_Atributo):
        self.__Atributo=new_Atributo
    
    @Atributo.deleter
    def Atributo(self):
        del self.__Atributo
    #------------------------------------
    """
    #------------------------------------
    @property
    def Color(self):
        # Documentacion de Color 
        return self.__Color
    #------------------------------------
    
    #------------------------------------
    @property
    def ID(self):
        # Documentacion de ID 
        return self.__ID
    #------------------------------------
    
    #------------------------------------
    @property
    def X_pos(self):
        # Documentacion de X_pos 
        return self.__X_pos
    
    @X_pos.setter
    def X_pos(self,new_X_pos):
        self.__X_pos=new_X_pos
    
    @X_pos.deleter
    def X_pos(self):
        del self.__X_pos
    #------------------------------------
    
    #------------------------------------
    @property
    def Y_pos(self):
        # Documentacion de Y_pos 
        return self.__Y_pos
    
    @Y_pos.setter
    def Y_pos(self,new_Y_pos):
        self.__Y_pos=new_Y_pos
    
    @Y_pos.deleter
    def Y_pos(self):
        del self.__Y_pos
    #------------------------------------
    
    #------------------------------------
    @property
    def Orientation(self):
        # Documentacion de ID 
        return self.__Orientation
    @Orientation.setter
    def Orientation(self,new_Orientation):
        self.__Orientation=new_Orientation
    
    @Orientation.deleter
    def Orientation(self):
        del self.__Orientation
    #------------------------------------
    
    #------------------------------------
    @property
    def Evaluate(self):
        # Documentacion de Evaluate 
        return self.__Evaluate
    
    @Evaluate.setter
    def Evaluate(self,new_Evaluate):
        self.__Evaluate=new_Evaluate
    
    @Evaluate.deleter
    def Evaluate(self):
        del self.__Evaluate
    #------------------------------------
    
    def moveForward(self):
        if self.Orientation == 'N':
            self.Y_pos=self.Y_pos-1
        elif self.Orientation == 'O':
            self.X_pos=self.X_pos-1
        elif self.Orientation == 'S':
            self.Y_pos=self.Y_pos+1
        elif self.Orientation == 'E':
            self.X_pos=self.X_pos+1
    
    def rotate90Left(self): # Izq
        if self.Orientation == 'N':
            self.Orientation = 'O'
        elif self.Orientation == 'O':
            self.Orientation = 'S'
        elif self.Orientation == 'S':
            self.Orientation = 'E'
        elif self.Orientation == 'E':
            self.Orientation ='N'
            
    def rotate90Right(self): # Der
        if self.Orientation == 'N':
            self.Orientation = 'E'
        elif self.Orientation == 'E':
            self.Orientation = 'S'
        elif self.Orientation == 'S':
            self.Orientation = 'O'
        elif self.Orientation == 'O':
            self.Orientation ='N'
    
    def rotate180(self): # Atras
        if self.Orientation == 'N':
            self.Orientation = 'S'
        elif self.Orientation == 'S':
            self.Orientation = 'N'
        elif self.Orientation == 'E':
            self.Orientation = 'O'
        elif self.Orientation == 'O':
            self.Orientation ='E'
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o,Agente):
            return self.ID==__o.ID
        elif type(__o)==list:
            return __o[0]==self.X_pos and __o[1]==self.Y_pos
        elif type(__o)==int:
            return self.ID==__o