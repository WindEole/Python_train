# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sequence.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/15 14:11:05 by iderighe          #+#    #+#              #
#    Updated: 2022/10/15 14:41:04 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# un container est une collection d'objects. Ces containers st divisés en 2 types:
#	- les séquences
#	- les hashmaps

# en python, pour séquencer des éléments, on dispose de plusieurs types :
# 	- type list (type mutable donc on peut changer les données sans créer une copie de liste)
#	- type tuple (comme des listes mais non mutable !)
#	- type range (intervalle numérique, type immutable ! Permet d'itérer facilement sur des valeurs numériques)

def list_type():					# | deux méthodes d'initialisation :
	my_list = ['a', 'b', 'c']		# | 1) crochet
	print("my_list		", my_list)	# |
	my_list = list()				# | 2) cast via list puis append pour rentrer les données
	my_list.append('d')
	my_list.append(2)
	my_list.append(3.0)
	print("my_list		", my_list)
	print("my_list[2]	", my_list[2])	# les crochets entourent l'index, qui permet d'accéder à chq élément de la liste comme s'il s'agissait d'un tableau

def tuple_type():					# le tuple est immutable, donc pas de fonctions pour changer / ajouter / remove ses données !
	my_tuple = tuple()
	my_tuple = (1, 'b', 3.0)
	print("\nmy_tuple	", my_tuple)
	print("my_tuple[2]	", my_tuple[2])

def range_type():							# ne prend que des valeurs numériques ! ATTENTION : pour imprimer un type range :
	my_range = range(5)						#	1) si print(my_range) : imprime range(début_intervalle, fin_intervalle) (ici, par défaut, début = 0)
	print("\nmy_range	", my_range)		#	2) pour imprimer tout ou partie des valeurs de notre range, il faut la tf en liste ! 
	print("my_range	", list(my_range))		#		on peut alors préciser ce qu'on veut (ici on affiche de deux en deux)
	my_range = range(2, 5)
	my_range = list(range(2, 10, 2))
	print("my_range	", my_range)

if __name__ == '__main__':
	list_type()
	tuple_type()
	range_type()