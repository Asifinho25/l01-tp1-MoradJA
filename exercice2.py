import math


def resoudreEquation(a, b, c):
    # TODO: Calculer le discriminant et assigner la valeur dans la variable "delta"
    delta = b**2-4*a*c

    # TODO: Déterminer la condition (bool) qui correspond à aucune solution de l'équation et mettre la valeur dans la variable "naPasDeSolution"
    naPasDeSolution = delta

    if naPasDeSolution<0:
        print('aucune racine')
        # ces ligne de code seront executé si il y'a aucune racine
        # TODO: afficher sur l'écran "Aucune racine"

        # ne pas modifier
        return None

    # TODO: Déterminer la condition (bool) qui correspond à une unique solution de l'équation et mettre la valeur dans "aUneSeuleSolution"
    aUneSeuleSolution = delta

    if aUneSeuleSolution==0:
        print('Une seule racine')

        # ces ligne de code seront executé si il y'a une seule racine
        # TODO: afficher sur l'écran "Une seule racine"

        # TODO: assigner a la variable x1 la valeur de la racine
        x1 = -b/(2*a)
        # ne pas modifier
        return x1

    # TODO: Déterminer la condition (bool) qui correspond à deux solutions de l'équation et mettre la valeur dans "aDeuxSolutions"
    aDeuxSolutions = delta

    if aDeuxSolutions>0:
        print('Deux racines')
        # TODO: afficher sur l'écran "Deux racines"

        # TODO: calculer la prmiere racine, assigner la a "x1"
        x1 = (-b-math.sqrt(delta))/2*a

        # TODO: calculer la deuxieme racine, assigner la a "x2"
        x2 = (-b+math.sqrt(delta))/2*a

        # ne pas modifier cette ligne
        return x1, x2


if __name__ == '__main__':
    a = int(input("Entrez a, non nul: "))
    b = int(input("Entrez b: "))
    c = int(input("Entrez c: "))

    print(resoudreEquation(a, b, c))
