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


configuration_courrante = []


#####################################################

#fonctions
def init_config_courrante():
    global configuration_courrante
    for i in range(0, 3):
        configuration_courrante.append([0, 0, 0])
        

def init_random_config(config):
    global configuration_courrante
    for i in configuration_courrante:
        for j in i:
            i[j] = random.randint(1, 3)



#####################################################

#programme pricipale







#####################################################
#widget
racine = tk.Tk()
racine.title("Configuration courante")
canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR)
boutton = tk.Button(racine, text="aléatoire")
# placement des widgets
canvas.grid(column=1, row=0)
boutton.grid(column=0, row=1)

init_config_courrante()
print(configuration_courrante)

# boucle principale
racine.mainloop()
