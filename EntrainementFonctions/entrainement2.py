"""
EXO 1:
Supprimer tout les espaces d'une
chaine de caractère

EXO 2:
Supprimer le mot le plus long
depuis la liste créer avec la méthode delSpace

AIDE: split
"""


def delSpace(l: str) -> str:
    x = l.split(" ")
    return x


def delWord(l: list, mot="", count=0):
    for i in range(len(l)):
        if mot < l[i]:
            mot = l[i]
            count += 1
    l.pop(count)
    return l


if __name__ == '__main__':
    print(delSpace("Salut les amis j'aime le Python"))
    print(delWord(delSpace("Salut les amis j'aime le python")))
