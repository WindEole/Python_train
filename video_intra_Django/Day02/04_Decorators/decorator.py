# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    decorator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/17 14:28:43 by iderighe          #+#    #+#              #
#    Updated: 2022/10/17 14:47:19 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Un Décorateur, c'est une fonction qui prend en paramétre une autre fonction afin
# d'en modifier son comportement !

import datetime

# Raw function |--> fonction témoin pour voir comment a se comporte sans décorateur
def raw_fct(s):
	return s

# with decorator |--> prend en param la fct f et la modifie
def decorator(f):
	def function(s):
		return (datetime.datetime.now().__str__() + ' ' + f(s))
	return function

# ----- 2 façons d'utiliser le decorateur ----- #

	# 1) fct identique à la fct témoin + redefinition de la fct dec_fct_assign

def dec_fct_assign(s):
	return s

dec_fct_assign = decorator(dec_fct_assign)

	# 2) appeler officiellement un decorator avec @ : python modifiera automatiquement la fct qui suit

@decorator
def dec_function_def(s):
	return s

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
	print("Without decorator : ")
	print(raw_fct('foo'))
	
	print("\nWith decorator (decorated fct as variable) : ")
	print(dec_fct_assign('foo'))

	print("\nWith decorator (@ syntax)")
	print(dec_function_def('foo'))

# on n'aura pas svt a définir ses propres décorateurs, mais il pourra arriver qu'on ait besoin
# d'implementer des décorateurs fournis par d'autres...