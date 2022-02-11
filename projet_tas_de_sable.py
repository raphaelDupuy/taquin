#####################################################
# groupe LDDBI
# Raphael DUPUY
# Soumaya MEDIOUNI
# 
# https://github.com/raphaelDupuy/projet_tas_de_sable
#####################################################

# import librairie
import tkinter as tk


#####################################################

#constante
HAUTEUR= 600
LARGEUR= 600


#####################################################

#variables globales



#####################################################

#fonction



#####################################################

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
