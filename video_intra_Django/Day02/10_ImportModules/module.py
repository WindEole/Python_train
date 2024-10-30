# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    module.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/17 15:50:14 by iderighe          #+#    #+#              #
#    Updated: 2022/10/17 16:23:02 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# On pourrait écrire des fichiers python de 10 kilomètres... pas très pratique.
# Mais on peut aussi diviser le code en module puis les importer... C'est mieux !

# RAPPEL : texte entre triple double quote = docstring pour le help de python !

""" This is the description of the module. """

var = 'This is a variable'

class Foo:
	""" Foo class description """

	def __str__(self):
		""" Foo.__str__() method description """
		return ("This is a Foo instance")

def fct1():
	""" fct1 description """
	print("This is a call of fct1()")

def fct2(param : int)-> str :
	""" fct2 description :  il takes an int and returns a str !"""
	print("This is a call of fct2()")
	return str(param)

# Une fois ce module créé, il faut l'importer dans la console python!
# 	- taper python3
# 	- import nom_du_module (ATTENTION, sans son extension .py !)
# 	- help(nom_du_module) : va donner tout le descriptif du module

# Ensuite, on peut accéder au contenu de notre module (tjs dans la console python3)
# 	- module.var |-> affiche la valeur de var
# 	- f = module.Foo() puis f |-> donne l'adresse de l'instance f
# 	- module.fct1()
# 	- module.fct2(42)

# si on ne veut importer qu'une partie du module, on peut aussi utiliser une autre syntaxe : 
# 	- from module import var
# 	- var |-> donne la valeur de var
# 	- from module import fct1, fct2
# 	- fct2(42)
