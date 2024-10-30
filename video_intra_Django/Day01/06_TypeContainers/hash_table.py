# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    hash_table.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/15 14:42:05 by iderighe          #+#    #+#              #
#    Updated: 2022/10/15 14:55:53 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# un hash map, c'est un dictionnaire !!! qui fonctionne sur le principe clé | valeur
# le type dict est mutable mais il n'est pas ordonné

if __name__ == '__main__':
	my_dict = {'type' : 'dictionnary'}	# 1er type d'initialisation
	my_dict = dict()					# 2ème type d'initialisation
	my_dict['type'] = 'dictionnary'
	print("my_dict	", my_dict)
	print(my_dict['type'])

	my_dict2 = {'type' : 'dictionnary', 'str' : 'hello', 'int' : '42'}
	print("\nmy_dict2	", my_dict2)
	print(my_dict2['str'])

	my_dict3 = dict()
	my_dict3['un'] = 'onze'
	my_dict3['deux'] = 'vingt-deux'
	my_dict3['trois'] = 'trente-trois'
	print("\nmy_dict3	", my_dict3)
	print(my_dict3['deux'])