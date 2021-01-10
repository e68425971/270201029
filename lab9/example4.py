def sumoflist(liste):
    if liste == []:
        return 0
    if isinstance(liste[0],list):
        return sumoflist(liste[0]) + sumoflist(liste[1:])
    else:
        return liste[0] + sumoflist(liste[1:])