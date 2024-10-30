# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    arguments.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/14 17:33:54 by iderighe          #+#    #+#              #
#    Updated: 2022/10/14 17:55:11 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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

def my_fct():
	print('Always look on the bright side')

def my_fct2(argument):
	print(argument)

def my_fct3(argument="(Whistle)"):
	print(argument)

def my_fct4(argument, argument2):
	print(argument, argument2)

if __name__ == '__main__' :
	print(color.GREEN + "my_fct : l'argument est en dur dans le print" + color.RESET)
	my_fct()
	print(color.LIMEGREEN + "my_fct2 : l'argument est donné lors de l'appel de la fonction" + color.RESET)
	my_fct2('of life...')
	print(color.FORESTGREEN + "my_fct3 : l'argument est défini dans le paramètre de la fonction" + color.RESET)
	my_fct3()
	print(color.SPRINGGREEN + "my_fct4 : les deux arguments sont donnés (possiblement dans le désordre) lors de l'appel de la fonction" + color.RESET)
	my_fct4(argument2 = 'of life...', argument = 'Always look on the light side')