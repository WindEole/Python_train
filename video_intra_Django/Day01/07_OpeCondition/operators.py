# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operators.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/15 16:40:33 by iderighe          #+#    #+#              #
#    Updated: 2022/10/15 16:55:45 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# en python, on utilise les opérateurs mathématiques habituels...

def math_operators():
	print(5 - 1)
	print(2 + 1.0)
	print(3 * 2)
	print(42 / 41) 	# /  -> le résultat sera un nb réel (donc possiblement un float)
	print(42 // 42)	# // -> le résultat sera un int !
	print(42 % 42)

def comparison_operators():
	print(1 == 2)
	print(1 != 2)
	print(1 > 2)
	print(1 < 2)
	print(1 >= 2)
	print(1 <= 2)

def concatenation_operators():	# on peut concatener des string en python !
	print('FUUUUUUU' + 'SIOOOOOONNNN !!')
	print(0 + 'This will fail miserably') # par contre on ne peut pas concaténer des types différents !

if __name__ == '__main__':
	math_operators()
	print()
	comparison_operators()
	print()
	concatenation_operators()