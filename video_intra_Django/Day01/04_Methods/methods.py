# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    methods.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/15 11:24:35 by iderighe          #+#    #+#              #
#    Updated: 2022/10/15 12:06:41 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# TEST de quelques méthodes associées au type str !

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

if __name__ == '__main__':
	print(color.GOLD + "test replace : remplace un morceau de string par un autre !" + color.RESET)
	var = str('This is a string')
	var2 = var.replace(' string', 'mazing !')	# par défaut, le 3ème param est -1 -> replace all occurences
	print(var2)
	
	var = str('to be or not to be')
	var2 = var.replace('be', 'think', 1)		# 3ème param définit le nb d'occurence à remplacer
	print(var2)

	print(color.GOLD + "\ntest index : return the lowest index in string where substring is found !" + color.RESET)
	var2 = var.index('be')
	print(var2)

	print(color.GOLD + "\ntest count : return the number of non-overlapping occurences of substring !" + color.RESET)
	var2 = var.count('be')
	print(var2)

	print(color.GOLD + "\ntest center : return a centered string of length width, with a padding !" + color.RESET)
	var2 = var.center(26, "*")	# default padding = space
	print(var2)

	print(color.GOLD + "\ntest expandtabs : tabs char are expanded using spaces !" + color.RESET)
	var = str('to		be	or not	to			be')
	var2 = var.expandtabs()		# default tab size = 8
	var3 = var.expandtabs(3)
	var4 = var.expandtabs(10)
	print(var2)
	print(var3)
	print(var4)

	print(color.GOLD + "\ntest casefold : return a version of the string suitable for caseless comparisons (met la string en lowercase) !" + color.RESET)
	var = str('TO BE or NOT TO be')
	var2 = var.casefold()
	print(var2)

	
# pour savoir quelles sont les methodes associées à un type :
#	- entrer dans la console python : python3
#	- taper help(type_recherché) (exemple help(str))
#	- pour rechercher une fonction en particulier : /replace\(
#	- si help est trop détaillé et qu'on veut juste une liste des méthodes : dir(type_recherché)(exemple dir(str))