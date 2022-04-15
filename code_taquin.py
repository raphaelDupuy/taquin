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
            

random_start()
print(grille)
