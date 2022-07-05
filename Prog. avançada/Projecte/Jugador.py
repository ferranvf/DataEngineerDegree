import tkinter
from tkinter import messagebox
from Fitxa import Fitxa, Peo, Dama

class Jugador():

    def __init__(self, color = 0):
        self._color = color
        self._fitxes = list()
        self._image = 0


    @property
    def image(self):
        return(self._image)
    @image.setter
    def image(self, image):
        self._image = image
    
    def inicialitza(self, tauler): #Inicialitzem totes les fitxes i les afegim a la llista de fitxes
        if self._color == 1:
            for i in range(0, 7, 2):
                self._fitxes.append(Peo(1, 0, i+1))
                tauler[0,i+1] = 1
                self._fitxes.append(Peo(1, 1, i))
                tauler[1,i] = 1
                self._fitxes.append(Peo(1, 2, i+1))
                tauler[2, i+1] = 1
        elif self._color == 2:
            for j in range(0, 7, 2):
                self._fitxes.append(Peo(2, 5, j))
                tauler[5,j] = 2
                self._fitxes.append(Peo(2, 6, j+1))
                tauler[6, j+1] = 2
                self._fitxes.append(Peo(2, 7, j))
                tauler[7, j] = 2

        
    def visualitza(self, finestra): #Cridem al visualitza per veure cada fitxa en el tauler
        for i in self._fitxes:
            i.visualitza(finestra)

    def processa_moviment(self, inici, final, tauler): # En aquesta funció el que fem és comprobar i possar en llistas els possibles moviments, matar dama i peo, moure dama i peo 
        try:
            diag1 = dict()
            diag2 = dict()
            diag3 = dict()
            diag4 = dict()
            mou_p = list()
            mata_p = list()
            coord_mou_p = dict()
            coord_mata_p = dict()
            mou_d = list()
            mata_d = list()
            coord_mou_d = dict()
            coord_mata_d = dict()
            estat_dama = list()
            estat_peo = list()
            oblig_matar = False
            col_mov = 0 # col_mou i col_mata són variables que van canviant en funció del torn, ens serveix per no repetir codi a la hora de comprobar els moviments de la dama
            col_mat = 0
            if self._color == 1:
                col_mov = 1
                col_mat = 2
            else:
                col_mov = 2
                col_mat = 1

            for f in self._fitxes:
                if f.estat() == 'dama':
                    estat_dama.append(f)
                else:
                    estat_peo.append(f)

            if estat_dama != []: # si hi ha una dama a la llista de fitxes s'omplen les llistes de les quatre diagonals
                for dama in estat_dama:
                    diag1[(dama.fila, dama.columna)] = []
                    diag2[(dama.fila, dama.columna)] = []
                    diag3[(dama.fila, dama.columna)] = []
                    diag4[(dama.fila, dama.columna)] = []
                    for i in range(1, 7):
                        if 0 <= (dama.fila - i) <= 7 and 0 <= (dama.columna - i) <= 7:
                            if (dama.fila - i, dama.columna - i) not in diag1:
                                diag1[(dama.fila, dama.columna)].append((dama.fila- i, dama.columna - i))

                    for i in range(1, 7):
                        if 0 <= (dama.fila - i) <= 7 and 0 <= (dama.columna + i) <= 7:
                            if (dama.fila - i, dama.columna + i) not in diag2:
                                diag2[(dama.fila, dama.columna)].append((dama.fila - i, dama.columna + i))

                    for i in range(1, 7):
                        if 0 <= (dama.fila + i) <= 7 and 0 <= (dama.columna - i) <= 7:
                            if (dama.columna + i, dama.columna - i) not in diag3:
                                diag3[(dama.fila, dama.columna)].append((dama.fila + i, dama.columna - i))

                    for i in range(1, 7):
                        if 0 <= (dama.fila + i) <= 7 and 0 <= (dama.columna + i) <= 7:
                            if (dama.fila + i, dama.columna + i) not in diag4:
                                diag4[(dama.fila, dama.columna)].append((dama.fila + i, dama.columna + i))


            if estat_dama != []: #Omplo les llistes de moure i mata de dama si exiteix alguna
                for dama in estat_dama:
                    coord_mata_d[(dama.fila, dama.columna)] = []
                    coord_mou_d[(dama.fila, dama.columna)] = []
                    matar = False
                    bloc1 = False
                    bloc2 = False
                    if (dama.fila, dama.columna) in diag1.keys():
                        valor = (diag1[(dama.fila, dama.columna)])
                        for i in valor:
                            if tauler[i[0], i[1]] == col_mov and 0 <= i[1]-1 <= 7 and 0 <= i[0]-1 <= 7:
                                if tauler[i[0] - 1, i[1] - 1] == 0 and 0 <= i[1]-1 <= 7 and 0 <= i[0]-1 <= 7:
                                    bloc1 = True
                                    bloc2 = True
                                    break
                                else:    
                                    coord_mou_d[(dama.fila, dama.columna)].append((i[0]-1,i[1]-1))
                                    break  
                            elif tauler[i[0], i[1]] == col_mat and 0 <= i[1]-1 <= 7 and 0 <= i[0]-1 <= 7:
                                bloc1 = True
                                if tauler[i[0] - 1, i[1] - 1] == 0 and 0 <= i[1]-1 <= 7 and 0 <= i[0]-1 <= 7:
                                    matar = True
                                    break
                                else:
                                    bloc2 = True
                                    break
                            else:
                                coord_mou_d[(dama.fila, dama.columna)].append(i)  

                        if matar == True:
                            coord_mata_d[(dama.fila, dama.columna)].append([(i[0],i[1]),(i[0] - 1, i[1] - 1)])
                        elif bloc1 == True and bloc2 == True:
                            if inici > final > (i[0], i[1]):
                                coord_mou_d[(dama.fila, dama.columna)].append(i)

                    matar = False
                    bloc1 = False
                    bloc2 = False
                    if (dama.fila, dama.columna) in diag2.keys():
                        valor = (diag2[(dama.fila, dama.columna)])
                        for i in valor:
                            if tauler[i[0], i[1]] == col_mov and 0 <= i[1]+1 <= 7 and 0 <= i[0]-1 <= 7:
                                if tauler[i[0] - 1, i[1] + 1] == 0 and 0 <= i[1]+1 <= 7 and 0 <= i[0]-1 <= 7:
                                    bloc1 = True
                                    bloc2 = True
                                    break
                                else:    
                                    coord_mou_d[(dama.fila, dama.columna)].append((i[0]-1,i[1]+1))
                                    break  
                            elif tauler[i[0], i[1]] == col_mat and 0 <= i[1]+1 <= 7 and 0 <= i[0]-1 <= 7:
                                bloc1 = True
                                if tauler[i[0] - 1, i[1] + 1] == 0 and 0 <= i[1]+1 <= 7 and 0 <= i[0]-1 <= 7:
                                    matar = True
                                    break
                                else:
                                    bloc2 = True
                                    break
                            else:
                                coord_mou_d[(dama.fila, dama.columna)].append(i)  

                        if matar == True:
                            coord_mata_d[(dama.fila, dama.columna)].append([(i[0],i[1]),(i[0]-1, i[1]+1)])
                        elif bloc1 == True and bloc2 == True:
                            if inici > final > (i[0], i[1]):
                                coord_mou_d[(dama.fila, dama.columna)].append(i)
                    
                    matar = False
                    bloc1 = False
                    bloc2 = False
                    if (dama.fila, dama.columna) in diag3.keys():
                        valor = (diag3[(dama.fila, dama.columna)])
                        for i in valor:
                            if tauler[i[0], i[1]] == col_mov and 0 <= i[1]-1 <= 7 and 0 <= i[0]+1 <= 7:
                                if tauler[i[0] + 1, i[1] - 1] == 0 and 0 <= i[1]-1 <= 7 and 0 <= i[0]+1 <= 7:
                                    bloc1 = True
                                    bloc2 = True
                                    break
                                else:    
                                    coord_mou_d[(dama.fila, dama.columna)].append((i[0]+1,i[1]-1))
                                    break  
                            elif tauler[i[0], i[1]] == col_mat and 0 <= i[1]-1 <= 7 and 0 <= i[0]+1 <= 7:
                                bloc1 = True
                                if tauler[i[0] + 1, i[1] - 1] == 0 and 0 <= i[1]-1 <= 7 and 0 <= i[0]+1 <= 7:
                                    matar = True
                                    break
                                else:
                                    bloc2 = True
                                    break
                            else:
                                coord_mou_d[(dama.fila, dama.columna)].append(i)  

                        if matar == True:
                            coord_mata_d[(dama.fila, dama.columna)].append([(i[0],i[1]),(i[0]+1, i[1]-1)])
                        elif bloc1 == True and bloc2 == True:
                            if inici < final < (i[0], i[1]):
                                coord_mou_d[(dama.fila, dama.columna)].append(i)

                    matar = False
                    bloc1 = False
                    bloc2 = False
                    if (dama.fila, dama.columna) in diag4.keys():
                        valor = (diag4[(dama.fila, dama.columna)])
                        for i in valor:
                            if tauler[i[0], i[1]] == col_mov and 0 <= i[1]+1 <= 7 and 0 <= i[0]+1 <= 7:
                                if tauler[i[0] + 1, i[1] + 1] == 0 and 0 <= i[1]+1 <= 7 and 0 <= i[0]+1 <= 7:
                                    bloc1 = True
                                    bloc2 = True
                                    break
                                else:    
                                    coord_mou_d[(dama.fila, dama.columna)].append((i[0]+1,i[1]+1))
                                    break  
                            elif tauler[i[0], i[1]] == col_mat and 0 <= i[1]+1 <= 7 and 0 <= i[0]+1 <= 7:
                                bloc1 = True
                                if tauler[i[0] + 1, i[1] + 1] == 0 and 0 <= i[1]+1 <= 7 and 0 <= i[0]+1 <= 7:
                                    matar = True
                                    break
                                else:
                                    bloc2 = True
                                    break  
                            else:
                                coord_mou_d[(dama.fila, dama.columna)].append(i)  
                    
                        if matar == True:
                            coord_mata_d[(dama.fila, dama.columna)].append([(i[0],i[1]),(i[0]+1, i[1]+1)])
                        elif bloc1 == True and bloc2 == True:
                            if inici < final < (i[0], i[1]):
                                coord_mou_d[(dama.fila, dama.columna)].append(i)
            # print(diag1, 'diag1')
            # print(diag2, 'diag2')
            # print(diag3, 'diag3')
            # print(diag4, 'diag4')

            for fitxa in (self._fitxes): #Omplo les llistes de mou i mata de peó en funició de si el torn és blanca o negre
                if self._color == 1:
                    if estat_peo != []:
                        coord_mata_p[(fitxa.fila, fitxa.columna)] = []
                        coord_mou_p[(fitxa.fila, fitxa.columna)] = []
                        dreta_alt = (fitxa.fila + 2, fitxa.columna + 2)
                        esquerra_alt = (fitxa.fila + 2, fitxa.columna - 2)
                        mitj_dreta = (dreta_alt[0] - 1, dreta_alt[1] - 1)
                        mitj_esquerra = (esquerra_alt[0] - 1, esquerra_alt[1] + 1)
                        if 0 <= dreta_alt[0] <= 7 and 0 <= dreta_alt[1] <= 7:
                            if tauler[dreta_alt[0], dreta_alt[1]] == 0 and tauler[mitj_dreta[0], mitj_dreta[1]] == 2:
                                coord_mata_p[(fitxa.fila, fitxa.columna)].append([mitj_dreta,dreta_alt])
                                oblig_matar = True 

                        if 0 <= esquerra_alt[0] <= 7 and 0 <= esquerra_alt[1] <= 7:
                            if tauler[esquerra_alt[0], esquerra_alt[1]] == 0 and tauler[mitj_esquerra[0], mitj_esquerra[1]] == 2:
                                coord_mata_p[(fitxa.fila, fitxa.columna)].append([mitj_esquerra,esquerra_alt])
                                oblig_matar = True
                        
                        if oblig_matar != True:                    
                            dreta_altB = (fitxa.fila + 1, fitxa.columna + 1)
                            esquerra_altB = (fitxa.fila + 1, fitxa.columna - 1)
                            coord_mou_p[(fitxa.fila, fitxa.columna)] = []
                            if 0 <= dreta_altB[0] <=7 and 0 <= dreta_altB[1] <= 7:
                                if tauler[dreta_altB[0], dreta_altB[1]] == 0:
                                    coord_mou_p[(fitxa.fila, fitxa.columna)].append(dreta_altB)

                            if 0 <= esquerra_altB[0] <=7 and 0 <= esquerra_altB[1] <= 7:
                                if tauler[esquerra_altB[0], esquerra_altB[1]] == 0:
                                    coord_mou_p[(fitxa.fila, fitxa.columna)].append(esquerra_altB)

                else:
                    if estat_peo != []:
                        coord_mata_p[(fitxa.fila, fitxa.columna)] = []
                        coord_mou_p[(fitxa.fila, fitxa.columna)] = []
                        dreta_baix = (fitxa.fila - 2, fitxa.columna + 2)
                        esquerra_baix = (fitxa.fila - 2, fitxa.columna - 2)
                        mitj_dreta = (dreta_baix[0] + 1, dreta_baix[1] - 1)
                        mitj_esquerra = (esquerra_baix[0] + 1, esquerra_baix[1] + 1)
                        if 0 <= dreta_baix[0] <=7 and 0 <= dreta_baix[1] <= 7:
                            if tauler[dreta_baix[0], dreta_baix[1]] == 0 and tauler[mitj_dreta[0], mitj_dreta[1]] == 1:
                                coord_mata_p[(fitxa.fila, fitxa.columna)].append([mitj_dreta,dreta_baix])
                                oblig_matar = True

                        if 0 <= esquerra_baix[0] <=7 and 0 <= esquerra_baix[1] <= 7:
                            if tauler[esquerra_baix[0], esquerra_baix[1]] == 0 and tauler[mitj_esquerra[0], mitj_esquerra[1]] == 1:
                                coord_mata_p[(fitxa.fila, fitxa.columna)].append([mitj_esquerra,esquerra_baix])
                                oblig_matar = True

                        if oblig_matar != True:
                            dreta_baixN = (fitxa.fila - 1, fitxa.columna + 1)
                            esquerra_baixN = (fitxa.fila - 1, fitxa.columna - 1)
                            coord_mou_p[(fitxa.fila, fitxa.columna)] = []
                            if 0 <= dreta_baixN[0] <=7 and 0 <= dreta_baixN[1] <= 7:
                                if tauler[dreta_baixN[0], dreta_baixN[1]] == 0:
                                    coord_mou_p[(fitxa.fila, fitxa.columna)].append(dreta_baixN)


                            if 0 <= esquerra_baixN[0] <=7 and 0 <= esquerra_baixN[1] <= 7:
                                if tauler[esquerra_baixN[0], esquerra_baixN[1]] == 0:
                                    coord_mou_p[(fitxa.fila, fitxa.columna)].append(esquerra_baixN)


            coord_mata_p = {k:v for k,v in coord_mata_p.items() if v} #Elimino els valors que estiguin buits del diccionari
            coord_mata_d = {k:v for k,v in coord_mata_d.items() if v}
            coord_mou_d = {k:v for k,v in coord_mou_d.items() if v}
            coord_mou_p = {k:v for k,v in coord_mou_p.items() if v}
            # print(coord_mata_d, 'mata dama')
            # print(coord_mata_p, 'mata peo')
            # print(coord_mou_d, 'mou dama')
            # print(coord_mou_p, 'mou peo')
            if coord_mata_d == {} and coord_mata_p == {} and coord_mou_d == {} and coord_mou_p == {}:
                return(False, False, False, False, True)

            for fitxa in self._fitxes:
                if (fitxa.fila, fitxa.columna) == inici: #Comprobo que la fitxa selecciondad és correcte
                    if coord_mata_p != {} or coord_mata_d != {}: #Si els diccionaris de mata peo i mata dama no estan buits que fagi el següent
                        if fitxa.estat() == 'peo':
                            mata_p = coord_mata_p[(fitxa.fila, fitxa.columna)] #Omplo una llista amb la coordenada on ha d'anar l'objecte i la coordenda de l'objecte a eliminar
                            mata = fitxa.mata(mata_p, final) #Crido a la funció mata de Fitxa
                            m = True #Significa que pot matar 
                            dama = False #Significa que no és dama
                            fi = False
                            return(mata, fitxa, m, dama, fi) #Retorno les coordenades on ha d'anar la fitxa i la que ha de matar, l'objecte, si pot matar o no, si és dama o no
                        else:
                            mata_d = coord_mata_d[(fitxa.fila, fitxa.columna)]
                            mata = fitxa.mata(mata_d, final)
                            m = True
                            dama = True
                            fi = False
                            return(mata, fitxa, m, dama, fi)
                    else:
                        if fitxa.estat() == 'peo':
                            mou_p = coord_mou_p[(fitxa.fila, fitxa.columna)]
                            mou = fitxa.mou(mou_p, final)
                            m = False
                            dama = False
                            fi = False
                            return(mou, fitxa, m, dama, fi)
                        else:
                            mou_d = coord_mou_d[(fitxa.fila, fitxa.columna)]
                            mou = fitxa.mou(mou_d, final)
                            m = False
                            dama = True
                            fi = False
                            return(mou, fitxa, m, dama, fi)
        except:
           messagebox.showerror(message ='HAS DE MATAR OBLIGATORIAMENT') #Si puc matar i selecciono una altre fitxa em retorna aquest print       
    

    def mata_fitxa(self, coord, tauler): #Elimina la fitxa que està a la coordenada passada com a paràmetre.
        for image in self._fitxes:
            if coord[0] == image.fila and coord[1] == image.columna:
                image._image.destroy() 
                self._fitxes.remove(image)

    def converteix_dama(self, imatge, finestra, tauler): #Converteixo a dama l'objecte passat com a paràmetre.
        self.mata_fitxa((imatge.fila, imatge.columna), tauler)
        self._fitxes.append(Dama(self._color, imatge.fila, imatge.columna))
        self._fitxes[-1].visualitza(finestra)

                    
    def n_peces_vives(self): #Retorna la llargada de la llista de fitxes.
        return(len(self._fitxes))
