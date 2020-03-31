from colorama import init, Fore, Style
import numpy as np

def red_text(text):
    init(convert = True)
    return f"{Fore.RED}{text}{Style.RESET_ALL}"

class Ruler:

    def __init__(self, chaineA, chaineB):

        self.chaineA = chaineA
        self.chaineB = chaineB
        nbre_de_lignes = len(self.chaineA) + 1
        nbre_de_colonnes = len(self.chaineB) + 1
        self.A = [] #ChaineA une fois les différences avec la chaineB mises
        self.B = [] #ChaineB une fois les différences avec la chaineA mises
        self.differences = np.zeros((nbre_de_lignes, nbre_de_colonnes))

    @ property
    def distance(self):
        return self.differences[-1,-1]


    def compute(self, d = 1):

        nbre_de_lignes = len(self.chaineA) + 1
        nbre_de_colonnes = len(self.chaineB) + 1

        for i in range(nbre_de_lignes):
            self.differences[i,0] = d*i

        for j in range(nbre_de_colonnes):
            self.differences[0, j] = d*j

        for i in range(1, nbre_de_lignes):

            for j in range (1, nbre_de_colonnes):

                premier_choix = self.differences[i-1,j-1] + 1 if self.chaineA[i-1] != self.chaineB[j-1] else self.differences[i-1,j-1]
                deuxieme_choix = self.differences[i-1,j] + d
                troisieme_choix =  self.differences[i,j-1] + d
                self.differences[i,j] = min (premier_choix, deuxieme_choix, troisieme_choix)

        i = len(self.chaineA)
        j = len(self.chaineB)

        while i > 0 and j > 0 :

            score = self.differences[i,j]
            score_diag = self.differences[i-1,j-1]
            score_up = self.differences[i-1,j]
            score_left = self.differences [i,j-1]


            sab = int(self.chaineA[i-1] != self.chaineB[j-1]) #condition pour pas encombrer le code

            if score == score_diag + sab : #on gère tout les cas de mouvement dans la matrice
                if sab :
                    self.A.append(red_text(self.chaineA[i-1]))
                    self.B.append(red_text(self.chaineB[j-1]))
                else:
                    self.A.append(self.chaineA[i-1])
                    self.B.append(self.chaineB[j-1])
                i += -1
                j += -1

            elif score == score_up + d:
                self.A.append(self.chaineA[i-1])
                self.B.append(red_text("="))
                i += -1


            elif score == score_left + d:
                self.B.append(self.chaineB[j-1])
                self.A.append(red_text("="))
                j += -1

    def report(self):
        return ''.join(reversed(self.A)),''.join(reversed(self.B))