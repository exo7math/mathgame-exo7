## Mathgame
## Algorithme minimax

import random
import math



##### A. Préliminaires #####

def evaluation(jeu):
    """ Evaluation de la position courante. Ici un nb au hasard. """
    N = 20
    val = random.randint(1,N)
    return val

def joue_un_coup(jeu, coup):
    """ Change la situation selon le coup joué. Ici ne fait rien. """
    nouveau_jeu = jeu  # normalement le jeu évolue
    return nouveau_jeu


##### B. Algorithme minimax #####

def minimax(jeu, profondeur, coups_prec, joueur_maximise):
    """ Fonction récursive qui renvoie le max (resp. le min) que je peux espérer à partir de 'jeu', en anticipant sur nb de coups 'profondeur'  
    La fonction renvoie aussi quel prochain coup permet d'atteindre ce max (resp. min).
    On retient aussi l'historique des coups à jouer dans 'coups_prec'.
    Le booléen 'joueur_maximise' détermine si on cherche à rélaiser le maximum ou le minimum. """

    M = 3 # Ici M coups possibles à chaque fois
    if profondeur == 0:              # On est à une feuille
        score = evaluation(jeu)
        print('Coups :',coups_prec, 'score :', score)
        return (score, coups_prec)
    else:
        if joueur_maximise:
            score_max = -math.inf
            for coup in range(M):
                nouveau_jeu = joue_un_coup(jeu, coup)  # ici ne fait rien
                score, nouv_coups_prec = minimax(nouveau_jeu, profondeur-1, coups_prec + [coup], False)
                if score > score_max:
                    score_max = score
                    coups_max = nouv_coups_prec
            return (score_max, coups_max)
        else:
            score_min = +math.inf
            for coup in range(M):
                nouveau_jeu = joue_un_coup(jeu, coup)
                score, nouv_coups_prec = minimax(nouveau_jeu, profondeur-1, coups_prec + [coup], True)
                if score < score_min:
                    score_min = score
                    coups_min = nouv_coups_prec
            return (score_min, coups_min)




# Test
# jeu = None # Car ici on n'a pas de vrai jeu
# print("Coups à jouer ",minimax(jeu, 3, [], True))


##### C. Elagage alpha-beta #####

def alphabeta(jeu, profondeur, alpha, beta, coups_prec, joueur_maximise):
    M = 3 # Ici M coups possibles à chaque fois
    if profondeur == 0:
        score = evaluation(jeu)
        print(score, coups_prec)
        return (score, coups_prec)
    else:
        if joueur_maximise:
            score_max = -math.inf
            for coup in range(M):
                nouveau_jeu = joue_un_coup(jeu, coup)
                score, nouv_coups_prec = alphabeta(nouveau_jeu, profondeur-1, alpha, beta, coups_prec + [coup], False)
                if score > score_max:
                    score_max = score
                    coups_max = nouv_coups_prec
                if score >= beta:  # Coupure alpha
                    break          # On arrête de chercher les coups suivants
                alpha = max(alpha, score)
            return (score_max, coups_max)
        else:
            score_min = +math.inf
            for coup in range(M):
                nouveau_jeu = joue_un_coup(jeu, coup)
                score, nouv_coups_prec = alphabeta(nouveau_jeu, profondeur-1, alpha, beta, coups_prec + [coup], True)
                if score < score_min:
                    score_min = score
                    coups_min = nouv_coups_prec
                if score <= alpha: # Coupure beta
                    break          # On arrête de chercher les coups suivants
                beta = min(beta, score)
            return (score_min, coups_min)



# Test
jeu = None # Car ici on n'a pas de vrai jeu
print("Coups à jouer ",alphabeta(jeu, 3, -math.inf, +math.inf, [], True))

