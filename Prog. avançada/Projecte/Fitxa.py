import tkinter
from PIL import Image, ImageTk


class Fitxa():

    def __init__(self, color = 0, fila = 0, columna = 0):
        self._fila = fila
        self._columna = columna
        self._color = color

    @property
    def color(self):
        return(self._color)
    @color.setter
    def color(self, color):
        self._color = color

    @property
    def fila(self):
        return(self._fila)
    @fila.setter
    def fila(self, fila):
        self._fila = fila

    @property
    def columna(self):
        return(self._columna)
    @columna.setter
    def columna(self, columna):
        self._columna = columna
    
    def mou(self, coord, final): #Comprova que el lloc on vull deixar la fitxa coincideixi amb alguna de les coordenades passades com paràmetre.
        for c in coord:
            if c == final:
                return(c)   
        return(False)
        
    def mata(self, coord, final): #El mateix que a mou
        for c in coord:
            if c[1] == final:
                return(c)
        return(False)

class Peo(Fitxa):

    def __init__(self, color, fila, columna):
        super().__init__(color, fila, columna)
    
    def estat(self): #Serveix per saber si la fitxa agafada és un peó o una dama.
        return('peo')
        
    def visualitza(self, finestra): #Em "possa" al tauler totes les fitxes
        self._image_fitxaB = Image.open("fitxa_blanca.png")
        self._image_tk_fitxaB = ImageTk.PhotoImage(self._image_fitxaB)

        self._image_fitxaN = Image.open("fitxa_negra.png")
        self._image_tk_fitxaN = ImageTk.PhotoImage(self._image_fitxaN)

        if self._color == 1:
            self._image = tkinter.Label(finestra, image = self._image_tk_fitxaB)
            self._image["bd"] = 0
            self._image.place(x = self.columna * 78, y = self.fila * 78)

        elif self._color == 2:
            self._image = tkinter.Label(finestra, image = self._image_tk_fitxaN)
            self._image["bd"] = 0
            self._image.place(x = self.columna * 78, y = self.fila * 78)
            

class Dama(Fitxa):
    
    def __init__(self,color, fila, columna):
        super().__init__(color, fila, columna)

    def estat(self):
        return ('dama')
    
    def visualitza(self, finestra): #Un cop converteixo a dama crido a aquesta funció perquè "possi" la dama al tauler.
        self._image_damaB = Image.open("dama_blanca.png")
        self._image_tk_damaB = ImageTk.PhotoImage(self._image_damaB)

        self._image_damaN = Image.open("dama_negra.png")
        self._image_tk_damaN = ImageTk.PhotoImage(self._image_damaN)

        if self._color == 1:
            self._image = tkinter.Label(finestra, image = self._image_tk_damaB)
            self._image["bd"] = 0
            self._image.place(x = self.columna * 78, y = self.fila * 78)

        elif self._color == 2:
            self._image = tkinter.Label(finestra, image = self._image_tk_damaN)
            self._image["bd"] = 0
            self._image.place(x = self.columna * 78, y = self.fila * 78)


