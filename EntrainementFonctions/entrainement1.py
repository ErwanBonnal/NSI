"""
Créer une méthode permettant de
retourner le nombre de caractère dans
uene chaine de caractère

Créer une méthode permettant de
retourner le plus nombre d'une liste

Créer une méthode permettant de supprimer
le plus grand nombre d'une liste
"""

def getString(c: list):
    count = 0
    for i in range(len(c)):
        count += 1
    print("il y a " + str(count) + " caractères dans la chaîne")

def getMax(c: list, count=1):
    max = 0
    for i in range(len(c)):
        if max < c[i]:
            max = c[i]
            count += 1
    print("le nombre le plus grand de la list est " + str(max))
    return count


def supprimeMax(c: list) -> list:
    c.pop(getMax(c))
    print("la nouvelle list est " + str(c))


if __name__ == '__main__':
    getString([0, 5, 1, 17, 4, 2])
    getMax([0, 5, 1, 17, 4, 2])
    supprimeMax([0, 5, 1, 17, 4, 2])