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

#programme pricipal
