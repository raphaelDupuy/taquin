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
    a = grille[3][3]
    grille[0][0], grille[3][3] = a, 0
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
            pass
        else:
            for i in range(ligne, 3):
                grille[i][colonne] = grille[i+1][colonne]
            grille[3][colonne] = 0
    
    # glisse une colonne vers le bas (d pour down)
    if direction == 'd':
        if ligne == 0:
            print('inutile')
            pass
        else:
            print('oui')
            for i in range(0, ligne):
                grille[3-i][colonne] = grille[2-i][colonne]
            grille[0][colonne] = 0

    


    # verifie si la partie est finie ou non
    verif_victoire()    


def win():
    pass


def verif_victoire():
    global grille
    if grille == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]:
        win()

            

random_start()
move('d')
print(grille)
