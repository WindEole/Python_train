# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    iterator_comparison.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/15 17:06:13 by iderighe          #+#    #+#              #
#    Updated: 2022/10/15 17:11:46 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# pour chercher à l'intérieur d'une séquence d'éléments : utiliser le mot-clé in

if __name__ == '__main__':
	mamas_and_papas = ['Michelle', 'Cass', 'Denny', 'John']
	
	if 'Jill' in mamas_and_papas:
		print('Jill is not in The Mamas & Papas')
	elif 'Cass' in mamas_and_papas:
		print('Cass is in The Mamas & Papas')

# évite d'itérer sur toute la liste ! On cherche un élément précis !