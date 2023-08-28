# Principe de l'animation 

fond = [0]*10
ecran = fond.copy()


print(ecran)   # rien à afficher

position = 0
ecran[position] = 1  # copie de l'image
print(ecran)

for i in range(9):
    ecran[position] = 0     # effacer l'image
    position = position + 1 # déplacement
    ecran[position] = 1     # nouvel affichage
    print(ecran)