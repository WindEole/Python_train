# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    iterator_loop.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/17 11:47:42 by iderighe          #+#    #+#              #
#    Updated: 2022/10/17 11:53:59 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# autre utilisation du for : sur un dictionnaire

if __name__ == '__main__':
	my_dict = {
		'France':'Fr',
		'Italy':'It',
		'Spain':'Es',
		'Japan':'Jp',
	}
	print('my_dict')
	for key, value in my_dict.items(): # la méthode .items() permet d'accéder aux clés et aux valeurs, ensemble !
		print(key, ':',value)

# ATTENTION : l'ordre d'affichage à l'écran ne sera pas forcément le même que celui de l'initialisation du dico !