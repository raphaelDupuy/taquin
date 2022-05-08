#####################################################
# groupe LDDBI
# Raphael DUPUY
# Soumaya MEDIOUNI
# Ebeguy YAPO
# https://github.com/raphaelDupuy/projet_tas_de_sable
##############################################################################
# imports des modules
import random
import tkinter as tk

##############################################################################
# globaux / constantes
grille = [[0]*4, [0]*4, [0]*4, [0]*4]
element = [None for i in range(16)]
LARGEUR = 400
HAUTEUR = 400
i_empty, j_empty = 3, 3

##############################################################################
# fonctions


def random_start():
    global grille
    cnt, var = 0, []
    for i in range(0, 4):
        for j in range(0, 4):
            while cnt in var:
                cnt = random.randint(0, 15)
                if len(var) == 16:
                    break
            grille[i][j] = cnt
            var.append(cnt)
    a = grille[3][3]
    grille[0][0], grille[3][3] = a, 0


random_start()
print(grille)


def get_line():
    # return la ligne du 0
    global grille
    if 0 in grille[0]:
        ligne = 0
    elif 0 in grille[1]:
        ligne = 1
    elif 0 in grille[2]:
        ligne = 2
    elif 0 in grille[3]:
        ligne = 3
    return ligne


def mouvement(event):
    # si on clic sur un carre ses coordonees sont asssocie au nombre de celuici
    i_empty, j_empty = get_line(), grille[get_line()].index(0)
    i = event.y//100
    j = event.x//100
    print(i, j, grille[i][j])
    if grille[i][j]:
        carre = grille[i][j]
        rectangle, texte = element[carre]
        # deplacement si possible
        if i+1 == i_empty and j == j_empty:
            canvas.move(rectangle, 0, 100)
            canvas.move(texte, 0, 100)
        elif j+1 == j_empty and i == i_empty:
            canvas.move(rectangle, 100, 0)
            canvas.move(texte, 100, 0)
        elif i-1 == i_empty and j == j_empty:
            canvas.move(rectangle, 0, -100)
            canvas.move(texte, 0, -100)
        elif j-1 == j_empty and i == i_empty:
            canvas.move(rectangle, -100, 0)
            canvas.move(texte, -100, 0)
        else:
            return
        grille[i][j], grille[i_empty][j_empty] = (
            grille[i_empty][j_empty], grille[i][j])
        i_empty = i
        j_empty = j
        verif_victoire()


def win():
    print("victoire !")
    racine.destroy()


def verif_victoire():
    # verifie la victoire
    global grille
    print(grille)
    if grille == [[1, 2, 3, 4], [5, 6, 7, 8],
                  [9, 10, 11, 12], [13, 14, 15, 0]]:
        win()


def save():
    # sauvegarde la grille
    fic = open('grille.txt', 'w')
    for i in range(0, 4):
        for j in range(0, 4):
            fic.write(str(grille[i][j]) + '\n')
    fic.close()


def load():
    # charge la grille sauvegardée
    global grille, element
    fic = open('grille.txt', 'r')
    for i in range(0, 4):
        for j in range(0, 4):
            grille[i][j] = int(fic.readline())
    fic.close()
    canvas.delete("all")
    element = [None for i in range(16)]
    affiche_grille()
    # Il faut afficher la grille sauvegardée sur le canvas


##############################################################################
# définition des widgets

racine = tk.Tk()
racine.title("Taquin")

canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg='orange')

bouton_save = tk.Button(text="save", command=save)
bouton_load = tk.Button(text="load", command=load)

# placement widgets
canvas.grid(row=1, column=1, rowspan=2)
bouton_save.grid(row=1, column=2)
bouton_load.grid(row=2, column=2)


# programme principal
def affiche_grille():
    global grille, element
    for i in range(4):
        for j in range(4):
            if grille[i][j]:
                x, y = 100*j, 100*i
                a, b, c = (x, y), (x+100, y+100), (x+50, y+50)
                rectangle = canvas.create_rectangle(a, b, fill="grey")
                carre = grille[i][j]
                nombre = canvas.create_text(c, text=grille[i][j], fill="black")
                element[carre] = (rectangle, nombre)


affiche_grille()
# liaison d evenement
canvas.bind("<Button-1>", mouvement)
# boucle principale
racine.mainloop()
