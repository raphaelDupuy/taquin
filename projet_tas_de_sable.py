#####################################################
# groupe LDDBI
# Raphael DUPUY
# Soumaya MEDIOUNI
# 
# https://github.com/raphaelDupuy/projet_tas_de_sable
#####################################################

# imports librairies
import tkinter as tk
import random


#####################################################

#constantes
HAUTEUR = 600
LARGEUR = 600


#####################################################

#variables globales


configuration_courrante = [[0, 0, 0]] * 3


#####################################################

#fonctions
def init_config_courrante(config):
    pass

def init_random_config(config):
    for i in config:
        for j in i:
            i[j] = random.randint(1, 3)
    return config



#####################################################

<<<<<<< HEAD
#programme pricipal
=======
#programme pricipale







#####################################################
#widget
racine= tk.TK()
racine.title("Configuration courante")
canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR)
boutton=tk.Button(racine, text=aleatoire)
# placement des widgets
canvas.grid(column=1, row=0)
boutton.grid(column=0, row=1)

init_terrain()

# boucle principale
racine.mainloop()
>>>>>>> 618741c6f1fa7cc891003c954b6121c999e58095
