import sys # import, c'est comme #include, par convention on les mets en haut du fichier !

class color:
	GRAY = '\033[90m' # ------ GRIS ------ #
	REALGRAY = '\033[38;2;128;128;128m'
	SILVER = '\033[38;2;192;192;192m'
	LIGHTSLATEGRAY = '\033[38;2;119;136;153m'
	RED = '\033[91m' # ------ ROUGE ------ #
	ORANGE = '\033[38;2;255;165;0m'
	FIREBRICK = '\033[38;2;178;34;34m'
	INDIANRED = '\033[38;2;205;92;92m'
	GREEN = '\033[92m' # ------ VERT ------ #
	LIMEGREEN = '\033[38;2;50;205;50m'
	FORESTGREEN = '\033[38;2;34;139;34m'
	SPRINGGREEN = '\033[38;2;0;255;127m'
	YELLOW = '\033[93m' # ------ JAUNE ------ #
	KHAKI = '\033[38;2;240;230;140m'
	REALYELLOW = '\033[38;2;255;255;0m'
	GOLD = '\033[38;2;255;215;0m'
	BLUE = '\033[94m' # ------ BLEU ------ #
	REALBLUE = '\033[38;2;0;0;255m'
	DEEPSKYBLUE = '\033[38;2;0;191;255m'
	ROYALBLUE = '\033[38;2;65;105;225m'
	PURPLE = '\033[95m' # ------ VIOLET ------ #
	FUCHSIA = '\033[38;2;255;0;255m'
	DARKVIOLET = '\033[38;2;148;0;211m'
	DARKMAGENTA = '\033[38;2;139;0;139m'
	CYAN = '\033[96m' # ------ CYAN ------ #
	AQUAMARINE = '\033[38;2;127;255;212m'
	PALETURQUOISE = '\033[38;2;175;238;238m'
	TEAL = '\033[38;2;0;128;128m'
	RESET = '\033[0m' # ------ RESET ------ #

print(color.LIMEGREEN + "Test 1 : print direct" + color.RESET)
print(sys.argv)

print(color.LIMEGREEN + "\nTest 2 : recuperer les arguments de la ligne de commande et print" + color.RESET)
for arg in reversed(sys.argv[1:]):
	print(color.FIREBRICK + arg[::-1].swapcase(), end=' ' + color.RESET)

# ATTENTION, ici on n'a fait que print ! Si on merge les arguments :
print(color.LIMEGREEN + "\n\nTest 3 : recuperer les arguments de la ligne de commande et merge avant de print" + color.RESET)
if __name__ == '__main__':
	# final = list()					# l'impression d'une liste ne donne pas le résultat attendu !
	# i = len(sys.argv) - 1
	# while i > 0:
	# 	final.append(sys.argv[i])
	# 	i -= 1
	# print('\n',final)
	final = str()
	for arg in reversed(sys.argv[1:]):
		final += str(arg[::-1]).swapcase() + ' '
	print(color.INDIANRED + final + color.RESET)