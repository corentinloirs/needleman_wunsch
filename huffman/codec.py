#Codec va faire appel à la libraire heapq, pour gérer l'ordonnancement des noeuds selon leur valeur
#On pourrait s'en passer, en triant à chaque itération la liste de
#dictionnaire des noeuds selon les keys. heapq le fera pour nous
#Heapq.heappop pop le dico de key la plus basse
#Heapq.heappush ajoute le noeud au heap
#C'est juste une gestion de pile automatisée

import heapq
import os

class node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other): #on va avoir besoin du comparateur < pour heapq (comme on en aurait besoin pour trier la pile)
            if(other == None):
                return -1
            if(not isinstance(other,node)):
                return -1
            return self.freq < other.freq

class builder:

    def __init__(self,text):
        self.heap = [] #liste des nodes, qu'on gérera facilement grâce à heapq
        self.text = text

    def make_frequency_dict(self): #dictionnaire des fréquences des lettres
            frequency = {}
            for character in self.text:
                if not character in frequency:
                    frequency[character] = 0
                frequency[character] += 1
            return frequency

    def heap_maker(self, frequency): #on construit la liste des nodes
        for key in frequency:
            noeud = node(key, frequency[key])
            print(noeud.freq, noeud.char)
            heapq.heappush(self.heap, noeud)

    def tree_maker(self): #maintenant on relie les noeuds entre eux

        while(len(self.heap)> 1): #On traite les noeuds jusqu'à ce qu'il ne reste que le noeud du haut, i.e. l'arbre binaire

            noeud1 = heapq.heappop(self.heap) #on sort le noeud de frequency la plus basse
            noeud2 = heapq.heappop(self.heap) #on sort le noeud de frequency la plus basse encore
            merged = node(None, noeud1.freq + noeud2.freq) #On relie les noeuds, l'info sur les chars sera dans les noeuds fils
            merged.left = noeud1 #on met bien le plus petit à gauche
            merged.right = noeud2 #et le plus grand à droite
            print(merged.freq)
            heapq.heappush(self.heap, merged) #et on remet ce noeud dans la liste des noeuds à traiter !

    def tree(self):
        frequency = self.make_frequency_dict()
        self.heap_maker(frequency)
        self.tree_maker()
        print(frequency)
        return self.heap[0]

def TreeBuilder(text):
    return builder(text)

class codec:

    def __init__(self, tree):
        self.tree = tree
        self.codes = {} #dico, à une lettre on associe un code
        self.reversemapping = {} #dico inversé, à un code on associe une lettre

    def codemaker(self):
        root = self.tree
        current_code = ""
        self.codemaker_assist1(root, current_code)

    def codemaker_assist1(self, root, current_code): #fonction d'assistance à codemaker

        if root == None:
            return

        if root.char != None: #on est sur un noeud en bout de branche, qui est associé à un charactère
            self.codes[root.char] = current_code #dictionnaire de codage
            self.reversemapping[current_code] = root.char #dictionnaire de décodage
            return

        self.codemaker_assist1(root.left, current_code + "0")
        self.codemaker_assist1(root.right, current_code + "1")

    def get_encoded_text(self, text):
            encoded_text = ""
            for char in text:
                encoded_text += self.codes[char]
            return encoded_text

    def encode(self,text):
        self.codemaker()
        encoded_text = self.get_encoded_text(text)
        print(self.codes)
        return encoded_text

    def decode(self, encoded_text):
        self.codemaker()
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if(current_code in self.reversemapping):
                character = self.reversemapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text

def Codec(tree):
    return codec(tree)











