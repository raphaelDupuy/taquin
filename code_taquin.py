#####################################################
# groupe LDDBI
# Raphael DUPUY
# Soumaya MEDIOUNI
# Ebeguy Yapo
# https://github.com/raphaelDupuy/projet_tas_de_sable
###########################################################################################################
# imports des modules
import random
import tkinter as tk

############################################################################################################
# constantes
grille = [[0]*4, [0]*4, [0]*4, [0]*4]
LARGEUR=400
HAUTEUR=400
grille=[[1, 2, 3,4],
       [ 5, 6,7,8],
       [9, 10, 11,12],
       [13,14,15,16]]
i_empty, j_empty=3,3       

############################################################################################################
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
    #si on clic sur un carre ses coordonees sont asssocie au nombre de celui ci
    global i_empty, j_empty
    i=event.y//100
    j=event.x//100
    print( i, j, grille[i][j])
    carre=grille[i][j]
    rectangle, texte=element[carre]
    #deplacement si possible
    if i+1 ==i_empty and j==j_empty:
         canvas.move(rectangle, 0, 100)
         canvas.move(texte, 0, 100)
    elif j+1 ==j_empty and i==i_empty:
        canvas.move(rectangle, 100, 0)
        canvas.move(texte, 100, 0)        
    elif i-1 ==i_empty and j==j_empty:
                    canvas.move(rectangle, 0, -100)
                    canvas.move(texte, 0, -100)
    elif j-1 ==j_empty and i==i_empty:
        canvas.move(rectangle, -100, 0)
        canvas.move(texte, -100, 0)
    
    
    else:
        return
    grille[i][j],grille[i_empty][j_empty]=(
        grille[i_empty][j_empty],grille[i][j])
    i_empty=i
    j_empty=j

    


def move(direction):
    global grille
    ligne = get_line()
    colonne = grille[ligne].index(0)
    # glisse une colonne vers le haut (u pour up)
    if direction == 'u':
        if ligne == 3:
            print('inutile')
        else:
            for i in range(ligne, 3):
                grille[i][colonne] = grille[i+1][colonne]
            grille[3][colonne] = 0
    
    # glisse une colonne vers le bas (d pour down)
    if direction == 'd':
        if ligne == 0:
            print('inutile')
        else:
            for i in range(0, ligne):
                grille[3-i][colonne] = grille[2-i][colonne]
            grille[0][colonne] = 0

    # glisse une ligne vers la droite (r pour right)
    if direction == 'r':
        if colonne == 0:
            print('inutile')
        else:
            for i in range(0, colonne):
                grille[ligne][3-i] = grille[ligne][2-i]
            grille[ligne][0] = 0

    # glisse une ligne vers la gauche (l pour left)
    if direction == 'l':
        if colonne == 3:
            print('inutile')
        else:
            for i in range(colonne, 3):
                grille[ligne][i] = grille[ligne][i+1]
            grille[ligne][3] = 0

    # verifie si la partie est finie ou non
    verif_victoire()    

    
def win():
    pass


def verif_victoire():
    # verifie la victoire
    global grille
    if grille == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]:
        win()

            


#######################################################################################################
# définition des widgets

racine = tk.Tk()
racine.title("Taquin")

canvas=tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg='orange')

bouton_save=tk.Button(text="save")
bouton_load=tk.Button(text="load")

# placement widgets
canvas.grid(row=1,column=1)
bouton_save.grid(row=1,column=2)
bouton_load.grid(row=2,column=2)
# programme principal

element=[None for i in range (17)]
for i in range(4):
    for j in range(4):
        x, y=100*j, 100*i
        a, b, c=(x, y), (x+100, y+100), (x+50, y+50)
        rectangle= canvas.create_rectangle(a, b, fill="grey")
        carre=grille[i][j]
        nombre= canvas.create_text(c, text=grille[i][j], fill="black")
        element[carre]=(rectangle,nombre)
#supprime la derniere case
canvas.delete(rectangle)
canvas.delete(nombre)
#liaison d evenement
canvas.bind("<Button-1>",mouvement)
#boucle principale
racine.mainloop()