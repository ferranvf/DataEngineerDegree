import tkinter
from tkinter import messagebox
import numpy as np
from Jugador import Jugador

class Partida():

    def __init__(self):
        self._estat_tauler = np.array #l'array es fila*columna
        self._jug_blanques = Jugador()
        self._jug_negres = Jugador()
        self._torn = 1
        self._coord = ()
        self._torna_a_matar = False
    
    @property
    def coord(self):
        return(self._coord)
    @coord.setter
    def coord(self, coordenada):
        self._coord = coordenada
    
    @property
    def torna_a_matar(self):
        return(self._torna_a_matar)
    @torna_a_matar.setter
    def torna_a_matar(self, torna):
        self._torna_a_matar = torna

    def inicialitza(self):
        self._estat_tauler = np.zeros((8, 8))#Creo l'array
        self._jug_blanques = Jugador(1)#Les fitxes del Jugador 1 són les blanques
        self._jug_negres = Jugador(2)#Les fitxes del Jugador 2 són les negres
        self._jug_blanques.inicialitza(self._estat_tauler)#Crido al inicialitza de Jugador 1
        self._jug_negres.inicialitza(self._estat_tauler)#Cirod al inicialitza de Jugador 2

    def get_posicio_tauler(self, event):
        return (event.widget.winfo_y() // 78 + event.y // 78,\
            event.widget.winfo_x() // 78  + event.x // 78)# Aqui processa el click, demanat en les funcions anteriors, agafa i deixa fitx

    def visualitza(self, finestra):
        self._jug_blanques.visualitza(finestra)#Aqui visualitza les fitxes blanques al tauler
        self._jug_negres.visualitza(finestra)#Aqui visualitza les fitxes negres al tauler

    def processa_moviment(self, inici, final, finestra):
        try:
            if self._torna_a_matar == True:
                if inici == self.coord:
                    tira = True
                else:
                    messagebox.showerror(message = 'No has seleccionat bé la fitxa')
            else:
                tira = True
            if self._torn == 1 and tira == True: #BLANQUES
                if self._estat_tauler[inici[0], inici[1]] == 1:#Comprova si el click inicial pertany a blanques o no.
                    mou, imatge, mata, dama, fi = self._jug_blanques.processa_moviment(inici, final, self._estat_tauler)#mou, imatge i m són variables que agafa del return 
                    #un cop hem cridat al processa moviment de jugador de blanques, al qual li passem com a paràmetres el click inicial i final
                    # i el tauler. 
                    if fi == True:#Comprobo que hi hagi més moviments
                        messagebox.showerror(message ='GUANYEN LES NEGRES, LES BLANQUES NO TENEN MÉS MOVIMENTS!!!!!')
                        finestra.destroy()
                    else:
                        if mou != False: #Si el que li arriva són coordenades que seguixi, sino vol dir que no ha agafat una bé.
                            if mata == True: #Això ho utilitzo per obligar matar.
                                self._estat_tauler[inici[0], inici[1]] = 0 #Com que pot matar, en les coordenades inicials del tauler possem un 0
                                self._estat_tauler[mou[0][0], mou[0][1]] = 0 #En les coordenades de la fitxa que mata també li possem un 0 al tauler
                                self._estat_tauler[final[0], final[1]] = 1 #Al lloc on va la fitxa li possem un 1, perquè es blanca
                                columna = final[1] #Ara la columna és la segona component de final
                                fila = final[0] #Fila és la primera component de final.
                                imatge.fila = final[0] #La fila del objecte triat és la primera component de final
                                imatge.columna = final[1] #La columna del objecte triat és la segona component de final.
                                self._jug_negres.mata_fitxa((mou[0]), self._estat_tauler) #Crido a la funció mata fitxa de les negres i li dic que mati la fitxa que es troba a les coordenades passades com a paràmetres.
                                imatge._image.place(x = columna * 78, y = fila * 78) #Aqui l'objecte triat li donc les coordenades on ha d'anar.
                                coord_mata = (final[0], final[1]) #coordenada on s'ha possat l'objecte un cop a matat
                                if dama == False: #Si l'objecte no és una dama que fagi el següent:
                                    if 0 <= coord_mata[0]+2 <= 7 and 0 <= coord_mata[1]+2 <= 7: #Comprobem que b no adjacent immediata surti del tauler
                                        if self._estat_tauler[coord_mata[0] + 2, coord_mata[1] + 2] == 0 and self._estat_tauler[coord_mata[0] + 1, coord_mata[1] + 1] == 2: #Comprobem que b pot tornar a matar
                                            self._torn = 1 #Si pot tornar a matar el torn torna a ser de blanques
                                            self.coord = final 
                                            self._torna_a_matar = True
                                            
                                        else:
                                            self._torn = 2
                                    else:
                                        self._torn = 2

                                    if 0 <= coord_mata[0]+2 <= 7 and 0 <= coord_mata[1]-2 <=7 and self._torn != 1:
                                        if self._estat_tauler[coord_mata[0] + 2, coord_mata[1] - 2] == 0 and self._estat_tauler[coord_mata[0] + 1, coord_mata[1] - 1] == 2:
                                            self._torn = 1 #Si pot tornar a matar el torn torna a ser de blanques
                                            self.coord = final 
                                            self._torna_a_matar = True 
                                            
                                        else:
                                            self._torn = 2
            
                                    if self._torn != 1:
                                        self._torn = 2
                                        peces_vives = self._jug_negres.n_peces_vives()
                                        self.coord = final 
                                        self._torna_a_matar = False
                        
                                    if final[0] == 7: #Si arriba al final es converteix en dama
                                        self._jug_blanques.converteix_dama(imatge, finestra, self._estat_tauler)
                                else: #El mateix si la fitxa triada es una dama
                                    canvi_torn1 = True
                                    canvi_torn2 = True
                                    canvi_torn3 = True
                                    canvi_torn4 = True
                                    for i in range(2,7):
                                        dreta_alt = (coord_mata[0] + i, coord_mata[1] + i) # Diagonal dreta dalt
                                        esquerra_alt = (coord_mata[0] - i, coord_mata[1] - i) # Diagonal esquerra dalt
                                        esquerra_baix = (coord_mata[0] + i, coord_mata[1] - i) # Diagonal esquerra avall
                                        dreta_baix = (coord_mata[0] - i, coord_mata[1] + i) # Diagonal dreta avall
                                        if 0 <= dreta_alt[0] <= 7 and 0 <= dreta_alt[1] <=7:
                                            if self._estat_tauler[dreta_alt[0] - 1, dreta_alt[1] - 1] == 2 and self._estat_tauler[dreta_alt[0],dreta_alt[1]] == 0:
                                                self._torn = 1
                                                self.coord = final 
                                                self._torna_a_matar = True
                                                break
                                            else:
                                                canvi_torn1 = False
                                                self.coord = final 
                                                self._torna_a_matar = False
                                        else:
                                            canvi_torn1 = False
                                            self.coord = final 
                                            self._torna_a_matar = False

                                        if 0 <= esquerra_alt[0] <= 7 and 0 <= esquerra_alt[1] <=7:
                                            if self._estat_tauler[esquerra_alt[0] + 1, esquerra_alt[1] + 1] == 2 and self._estat_tauler[esquerra_alt[0],esquerra_alt[1]] == 0:
                                                self._torn = 1
                                                self.coord = final 
                                                self._torna_a_matar = True
                                                break
                                            else:
                                                canvi_torn2 = False
                                                self.coord = final 
                                                self._torna_a_matar = False
                                        else:
                                            canvi_torn2 = False
                                            self.coord = final 
                                            self._torna_a_matar = False

                                        if 0 <= esquerra_baix[0] <= 7 and 0 <= esquerra_baix[1] <=7:
                                            if self._estat_tauler[esquerra_baix[0] - 1, esquerra_baix[1] + 1] == 2 and self._estat_tauler[esquerra_baix[0],esquerra_baix[1]] == 0:
                                                self._torn = 1
                                                self.coord = final 
                                                self._torna_a_matar = True
                                                break
                                            else:
                                                canvi_torn3 = False
                                                self.coord = final 
                                                self._torna_a_matar = False
                                        else:
                                            canvi_torn3 = False
                                            self.coord = final 
                                            self._torna_a_matar = False
                                        
                                        if 0 <= dreta_baix[0] <= 7 and 0 <= dreta_baix[1] <=7:
                                            if self._estat_tauler[dreta_baix[0] + 1, dreta_baix[1] - 1] == 2 and self._estat_tauler[dreta_baix[0],dreta_baix[1]] == 0:
                                                self._torn = 1
                                                self.coord = final 
                                                self._torna_a_matar = True
                                                break
                                            else:
                                                canvi_torn4 = False
                                                self.coord = final 
                                                self._torna_a_matar = False
                                        else:
                                            canvi_torn4 = False
                                            self.coord = final 
                                            self._torna_a_matar = False

                                        if canvi_torn1 == False and canvi_torn2 == False and canvi_torn3 == False and canvi_torn4 == False:
                                            self._torn = 2
                                            peces_vives = self._jug_negres.n_peces_vives()

                            else: # Sino puc matar faig el mateix.
                                self._estat_tauler[inici[0], inici[1]] = 0
                                self._estat_tauler[final[0], final[1]] = 1
                                columna = final[1]
                                fila = final[0]
                                imatge.fila = final[0]
                                imatge.columna = final[1]
                                imatge._image.place(x = columna*78, y = fila*78)
                                self._torn = 2
                                if final[0] == 7:
                                    self._jug_blanques.converteix_dama(imatge,finestra, self._estat_tauler)
                                peces_vives = self._jug_negres.n_peces_vives()

                        else:
                            messagebox.showerror(message = "No has mogut bé")
                            self._torn = 1
                else:
                    messagebox.showerror(message ='No és el teu torn, li toca a Blanques')
                
            else: #El mateix pero si la fitxa és negra
                if self._estat_tauler[inici[0], inici[1]] == 2:
                    mou, imatge, mata, dama, fi = self._jug_negres.processa_moviment(inici, final, self._estat_tauler)
                    if fi == True:
                        messagebox.showerror(message ='GUANYEN LES BLANQUES, LES NEGRES NO TENEN MÉS MOVIMENTS!!!!!')
                        finestra.destroy()
                    else:
                        if mou != False:
                            if mata == True:
                                self._estat_tauler[inici[0], inici[1]] = 0
                                self._estat_tauler[mou[0][0], mou[0][1]] = 0
                                self._estat_tauler[final[0], final[1]] = 2
                                columna = final[1]
                                fila = final[0]
                                imatge.fila = final[0]
                                imatge.columna = final[1]
                                self._jug_blanques.mata_fitxa((mou[0]), self._estat_tauler)
                                imatge._image.place(x = columna * 78, y = fila * 78)
                                coord_mata = (final[0], final[1])
                                if dama == False:  
                                    if 0 <= coord_mata[0]-2 <= 7 and 0 <= coord_mata[1]+2 <= 7: #Comprobem que b no adjacent immediata surti del tauler
                                        if self._estat_tauler[coord_mata[0] - 2, coord_mata[1] + 2] == 0 and self._estat_tauler[coord_mata[0] - 1, coord_mata[1] + 1] == 1: #Comprobem que b pot tornar a matar
                                            self._torn = 2 #Si pot tornar a matar el torn torna a ser de blanques
                                            self.coord = final 
                                            self._torna_a_matar = True
                                        else:
                                            self._torn = 1
                                    else:
                                        self._torn = 1

                                    if 0 <= coord_mata[0]-2 <= 7 and 0 <= coord_mata[1]-2 <=7 and self._torn != 2:
                                        if self._estat_tauler[coord_mata[0] - 2, coord_mata[1] - 2] == 0 and self._estat_tauler[coord_mata[0] - 1, coord_mata[1] - 1] == 1:
                                            self._torn = 2 #Si pot tornar a matar el torn torna a ser de blanques
                                            self.coord = final 
                                            self._torna_a_matar = True 
                                        else:
                                            self._torn = 1
                                    if self._torn != 2:
                                        self._torn = 1
                                        peces_vives = self._jug_blanques.n_peces_vives()
                                        self.coord = final 
                                        self._torna_a_matar = False

                                    if final[0] == 0:
                                        self._jug_negres.converteix_dama(imatge,finestra, self._estat_tauler)
                                else:
                                    canvi_torn1 = True
                                    canvi_torn2 = True
                                    canvi_torn3 = True
                                    canvi_torn4 = True
                                    for i in range(2,7):
                                        dreta_alt = (coord_mata[0] + i, coord_mata[1] + i)
                                        esquerra_alt = (coord_mata[0] - i, coord_mata[1] - i)
                                        esquerra_baix = (coord_mata[0] + i, coord_mata[1] - i)
                                        dreta_baix = (coord_mata[0] - i, coord_mata[1] + i)
                                        if 0 <= dreta_alt[0] <= 7 and 0 <= dreta_alt[1] <=7:
                                            if self._estat_tauler[dreta_alt[0] - 1, dreta_alt[1] - 1] == 1 and self._estat_tauler[dreta_alt[0],dreta_alt[1]] == 0:
                                                self._torn = 2
                                                self.coord = final 
                                                self._torna_a_matar = True
                                                break
                                            else:
                                                canvi_torn1 = False
                                                self.coord = final 
                                                self._torna_a_matar = False
                                        else:
                                            canvi_torn1 = False
                                            self.coord = final 
                                            self._torna_a_matar = False

                                        if 0 <= esquerra_alt[0] <= 7 and 0 <= esquerra_alt[1] <=7:
                                            if self._estat_tauler[esquerra_alt[0] + 1, esquerra_alt[1] + 1] == 1 and self._estat_tauler[esquerra_alt[0],esquerra_alt[1]] == 0:
                                                self._torn = 2
                                                self.coord = final 
                                                self._torna_a_matar = True
                                                break
                                            else:
                                                canvi_torn2 = False
                                                self.coord = final 
                                                self._torna_a_matar = False
                                        else:
                                            canvi_torn2 = False
                                            self.coord = final 
                                            self._torna_a_matar = False

                                        if 0 <= esquerra_baix[0] <= 7 and 0 <= esquerra_baix[1] <=7:
                                            if self._estat_tauler[esquerra_baix[0] - 1, esquerra_baix[1] + 1] == 1 and self._estat_tauler[esquerra_baix[0],esquerra_baix[1]] == 0:
                                                self._torn = 2
                                                self.coord = final 
                                                self._torna_a_matar = True 
                                                break
                                            else:
                                                canvi_torn3 = False
                                                self.coord = final 
                                                self._torna_a_matar = False
                                        else:
                                            canvi_torn3 = False
                                            self.coord = final 
                                            self._torna_a_matar = False
                                        
                                        if 0 <= dreta_baix[0] <= 7 and 0 <= dreta_baix[1] <=7:
                                            if self._estat_tauler[dreta_baix[0] + 1, dreta_baix[1] - 1] == 1 and self._estat_tauler[dreta_baix[0],dreta_baix[1]] == 0:
                                                self._torn = 2
                                                self.coord = final 
                                                self._torna_a_matar = True
                                                break
                                            else:
                                                canvi_torn4 = False
                                                self.coord = final 
                                                self._torna_a_matar = False
                                        else:
                                            canvi_torn4 = False
                                            self.coord = final 
                                            self._torna_a_matar = False

                                        if canvi_torn1 == False and canvi_torn2 == False and canvi_torn3 == False and canvi_torn4 == False:
                                            self._torn = 1
                                            peces_vives = self._jug_blanques.n_peces_vives()

                            else:
                                self._estat_tauler[inici[0], inici[1]] = 0
                                self._estat_tauler[final[0], final[1]] = 2
                                columna = final[1]
                                fila = final[0]
                                imatge.fila = final[0]
                                imatge.columna = final[1]
                                imatge._image.place(x = columna*78, y = fila*78)
                                self._torn = 1
                                if final[0] == 0:
                                    self._jug_negres.converteix_dama(imatge,finestra, self._estat_tauler)
                                peces_vives = self._jug_blanques.n_peces_vives()
                                    
                        else:
                            messagebox.showerror(message ='No has mogut bé')
                            self._torn = 2

                else:
                    messagebox.showerror(message ='No és el teu torn, li toca a negres')

            self.final_partida(peces_vives, finestra)

            if self._torn == 1:
                print('Torn de blanques')
            else:
                print('Torn de negres')

            print(self._estat_tauler)
    
        except:
            pass
        
    def final_partida(self, peces_vives, finestra): #Aquesta funció ens serveix per saber si s'acaba o no la partida
        if self._torn == 1:
            if peces_vives != 0:
                print('Queden ', peces_vives, 'fitxes blanques vives')
            else:
                messagebox.showerror(message ='LES NEGRES GUANYEN!!!!!')
                finestra.destroy()
        else:
            if peces_vives != 0:
                print('Queden ', peces_vives, 'fitxes negres vives')
            else:
                messagebox.showerror(message ='GUANYEN LES BLANQUES!!!!!')
                finestra.destroy()
            
