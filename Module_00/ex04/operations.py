import sys

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

def addition(param1, param2):
	""" displays the sum of param1 and param2 """

	addition = param1 + param2
	print(color.ORANGE + "Sum:		" + color.CYAN, addition, color.RESET)

def soustraction(param1, param2):
	""" displays the difference of param1 minus param2 """
	
	soustraction = param1 - param2
	print(color.ORANGE + "Difference:	" + color.CYAN, soustraction, color.RESET)

def muliplication(param1, param2):
	""" displays the product of param1 and param2 """
	
	multiplication = param1 * param2
	print(color.ORANGE + "Product:	" + color.CYAN, multiplication, color.RESET)

def division(param1, param2):
	""" displays, if possible, the division of param1 by param2 """

	if (param2 == 0):
		print(color.ORANGE + "Quotient:	" + color.FIREBRICK + "ERROR (division by zero)")
	else:
		division = param1 / param2
		print(color.ORANGE + "Quotient:	" + color.CYAN, division, color.RESET)

def reste(param1, param2):
	""" displays, if possible, the remainder of a division of param1 by param2 """

	if (param2 == 0):
		print(color.ORANGE + "Remainder:	" + color.FIREBRICK + "ERROR (modulo by zero)")
	else:
		reste = param1 % param2
		print(color.ORANGE + "Remainder:	" + color.CYAN, reste, color.RESET)

if __name__ == '__main__':
	if (len(sys.argv) > 3):
		print(color.RED + "Too many Arguments" + color.RESET)
	elif (len(sys.argv) < 3):
		print(color.INDIANRED + "Usage: python operations.py <number1> <number2>\n" + color.KHAKI + "Example:\n	python operations.py 10 3" + color.RESET)
	else:
		try:
			param1 = int(sys.argv[1])
			print(color.GOLD, type(param1), " | ", param1, color.RESET)
			param2 = int(sys.argv[2])
			print(color.GOLD, type(param2), " | ", param2, color.RESET)
			addition(param1, param2)
			soustraction(param1, param2)
			muliplication(param1, param2)
			division(param1, param2)
			reste(param1, param2)
		except ValueError:
			print(color.FIREBRICK + "Arguments are not both integers !" + color.RESET)

