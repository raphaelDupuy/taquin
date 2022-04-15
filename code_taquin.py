# imports
import random

# globaux
grille = [[0]*4, [0]*4, [0]*4, [0]*4]

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
    # a = grille[3][3]
    # grille[0][0], grille[3][3] = a, 0
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

def sauvegarde():
    """Sauvegarde la config courante dans le fichier sauvegarde"""
    fic = open("sauvegarde", "w")
    fic.write(str(N)+"\n")
    for i in range(1, N+1):
        for j in range(1, N+1):
            fic.write(str(config_cur[i][j]))
            fic.write("\n")
    fic.close()
    
 def load():
    fic = open("sauvegarde", "r")
    config = [[0 for i in range(N+2)] for j in range(N+2)]
    ligne = fic.readline()
    n = int(ligne)
    if n != N:
        fic.close()
        return config
    i = j = 1
    for ligne in fic:
        config[i][j] = int(ligne)
        j += 1
        if j == N + 1:
            j = 1
            i += 1
    fic.close()
    return config


def load_bouton():
    global config_cur, add_active, sous_active
    if add_active:
        config_cur = addition(config_cur, load())
        add_active = False
    elif sous_active:
        config_cur = soustraction(config_cur, load())
        sous_active = False
    else:
        config_cur = load()
    affiche_grille(config_cur)   
    
def win():
    pass


def verif_victoire():
    # verifie la victoire
    global grille
    if grille == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]:
        win()

            

random_start()
print(grille)
