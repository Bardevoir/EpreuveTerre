# Determine si l'argument donné est pair ou impair#
# Gérer les entiers négatifs

import sys

def est_pair(nombre):
    if nombre < 0:
        nombre = nombre * -1
    if nombre %  2 == 1:
        return False
    else:
        return True
    

try:
    arg_user = int(sys.argv[1])
except IndexError:
    print("Tu me la mettras pas à l'envers (rentre quelque chose)")
except ValueError:
    print("Tu me la mettras pas à l'envers (rentre un nombre)")
else:
    if est_pair(arg_user):
        print("pair")
    else:
        print("impair")