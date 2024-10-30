# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    comprehension.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/17 11:55:11 by iderighe          #+#    #+#              #
#    Updated: 2022/10/17 12:02:39 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# les Compréhensions sont une particularité de python : elles permettent de créer
# des listes de façon concise 

if __name__ == '__main__':
	l = []						# 1ère façon : on initialise une liste vide
	for i in range(10):			# boucle sur un range de 10 
		if i % 2 == 0:			# on ne veut que les pairs 
			l.append(i ** 2)	# et on remplit la liste avec la méthode .append() après avoir mis le nb au carré (** = exposant)
	print(l)

	l = [i ** 2 for i in range(10) if i % 2 == 0]	# 2ème façon : la compréhesion ! Tout sur une seule ligne !
	print(l)