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

# Try using optional arguments !! optional argument is an arg with a default value !

def text_analyzer(param=None):
	"""Analyse a text:

	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	"""

	# print(type(param))
	# print(param)

	try:
		if type(param) is int:
			raise Exception("argument is not a string")
		else:
			if (param == None):
				print(color.FIREBRICK + "What is the text to analyze ?" + color.RESET)
				inp = input(">> ")	# fct input("texte_d'amorce") pour récupérer le texte écrit sur stdin ! 
				print(inp)
				param = inp
				# for line in sys.stdin:		# trop compliqué pour le moment !
				# 	if 'q' == line.rstrip():
				# 		break
				# 	print(f'Input : {line}')
				# param = line
			i = 0
			n_lowcase = 0
			n_upcase = 0
			n_space = 0
			n_punctuation = 0
			while i < len(param):
				if (param[i].islower()):
					n_lowcase += 1
				elif (param[i].isupper()):
					n_upcase += 1
				elif (param[i].isspace()):
					n_space += 1
				elif (param[i].isdigit()):
					pass
				else:
					n_punctuation += 1
				i += 1
			print(color.LIMEGREEN + "The text contains", len(param), "character(s):" + color.RESET)
			print(color.ORANGE + "-", n_upcase, "upper letter(s)" + color.RESET)
			print(color.DEEPSKYBLUE + "-", n_lowcase, "lower letter(s)" + color.RESET)
			print(color.FUCHSIA + "-", n_punctuation, "punctuation mark(s)" + color.RESET)
			print(color.PALETURQUOISE + "-", n_space, "space(s)" + color.RESET)
	except Exception as e:
		print(e)

if __name__ == '__main__':
	# if (len(sys.argv) < 2):
	# 	print(color.FIREBRICK + "Not enough Arguments" + color.RESET)
	if (len(sys.argv) > 2):
		print(color.RED + "Too much Arguments" + color.RESET)
	elif (len(sys.argv) < 2):
		text_analyzer()
	else:
		text_analyzer(sys.argv[1])
