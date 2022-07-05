import tkinter
from PIL import Image, ImageTk
from Partida import Partida

class Pantalla():

    def __init__(self):
        self._finestra = tkinter.Tk()
        self._finestra.geometry("624x624")
        self._finestra.bind_all('<Button-3>', self.agafa_fitxa)
        self._finestra.bind_all('<Button-1>', self.deixa_fitxa)
        self._image = Image.open("tauler.png")
        self._image_tk = ImageTk.PhotoImage(self._image)
        self._tauler = tkinter.Label (self._finestra, image = self._image_tk) # el tauler es diferent a la array, en el tauler es columna*fila
        self._tauler.place(x = 0, y = 0)
        self._tauler["bd"] = 0
        self.menu()
        self._finestra.mainloop()
    
    def inicialitza_jug(self):
        self._partida = Partida()
        self._pos_ini_moviment = (int(), int())
        self._pos_final_moviment = (int(), int())
        self._partida.inicialitza()
        self._partida.visualitza(self._finestra)
        self.dos_jugadors_button.destroy()
        self.maquina_button.destroy()
    
    def inicialitza_maq(self):
        pass


    def agafa_fitxa(self, event):
        self._pos_ini_moviment = self._partida.get_posicio_tauler(event) #Primer click, que serveix per agafar la fitxa
                
    def deixa_fitxa(self, event):
        self._pos_final_moviment = self._partida.get_posicio_tauler(event)#Segon click, que serveix per deixar la fitxa seleccionada anteriorment
        self.processa_moviment(event)#Crido a la funció que ve a continuació

    def processa_moviment(self, event):
        self._partida.processa_moviment(self._pos_ini_moviment, self._pos_final_moviment, self._finestra)
    
    def menu(self):
        self.dos_jugadors_button = tkinter.Button(self._finestra, text = "JUGAR CONTRA UN AMIC/AMIGA", width = 30, command = self.inicialitza_jug, justify = 'center'\
            ,activebackground = 'lightblue', height = 5)
        self.dos_jugadors_button.place(x = 200, y = 150)
        self.maquina_button = tkinter.Button(self._finestra, text = "JUGAR CONTRA LA MAQUINA", width = 30, command = self.inicialitza_maq, justify = 'center'\
            ,activebackground = 'lightblue', height = 5)
        self.maquina_button.place(x = 200, y = 300)

        

p = Pantalla()
