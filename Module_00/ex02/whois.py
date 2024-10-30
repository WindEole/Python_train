import sys

class color:
	GRAY = '\033[90m' # ------------- GRIS ------ #
	REALGRAY = '\033[38;2;128;128;128m'
	SILVER = '\033[38;2;192;192;192m'
	LIGHTSLATEGRAY = '\033[38;2;119;136;153m'
	RED = '\033[91m' # ------------- ROUGE ------ #
	ORANGE = '\033[38;2;255;165;0m'
	FIREBRICK = '\033[38;2;178;34;34m'
	INDIANRED = '\033[38;2;205;92;92m'
	GREEN = '\033[92m' # ------------ VERT ------ #
	LIMEGREEN = '\033[38;2;50;205;50m'
	FORESTGREEN = '\033[38;2;34;139;34m'
	SPRINGGREEN = '\033[38;2;0;255;127m'
	YELLOW = '\033[93m' # ---------- JAUNE ------ #
	KHAKI = '\033[38;2;240;230;140m'
	REALYELLOW = '\033[38;2;255;255;0m'
	GOLD = '\033[38;2;255;215;0m'
	BLUE = '\033[94m' # ------------- BLEU ------ #
	REALBLUE = '\033[38;2;0;0;255m'
	DEEPSKYBLUE = '\033[38;2;0;191;255m'
	ROYALBLUE = '\033[38;2;65;105;225m'
	PURPLE = '\033[95m' # --------- VIOLET ------ #
	FUCHSIA = '\033[38;2;255;0;255m'
	DARKVIOLET = '\033[38;2;148;0;211m'
	DARKMAGENTA = '\033[38;2;139;0;139m'
	CYAN = '\033[96m' # ------------- CYAN ------ #
	AQUAMARINE = '\033[38;2;127;255;212m'
	PALETURQUOISE = '\033[38;2;175;238;238m'
	TEAL = '\033[38;2;0;128;128m'
	RESET = '\033[0m' # ------------ RESET ------ #

if (len(sys.argv) < 2):
	print(color.FIREBRICK + "Not enough Arguments" + color.RESET)
elif (len(sys.argv) > 2):
	print(color.RED + "Too much Arguments" + color.RESET)
else:
	try:
		num = int(sys.argv[1])
		print(color.GREEN + "Argument is an integer" + color.RESET)
		print(num)
		if (num == 0):
			print(color.SPRINGGREEN + "I am Zero" + color.RESET)
		elif (num % 2) == 0:
			print(color.LIMEGREEN + "I am even" + color.RESET)
		else:
			print(color.FORESTGREEN + "I am odd" + color.RESET)
	except ValueError :
		print(color.INDIANRED + "Argument is not an integer" + color.RESET)
