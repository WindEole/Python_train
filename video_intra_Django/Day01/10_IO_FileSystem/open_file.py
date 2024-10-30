# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    open_file.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/17 12:05:26 by iderighe          #+#    #+#              #
#    Updated: 2022/10/17 12:14:00 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# comment ouvrir, écrire et fermer un fichier en python

if __name__ == '__main__':
	filename = 'my_file.txt'

	f = open(filename, 'a')		# open est une built-in, 'a' for appending text !
	f.write('Hard as a rock !')	# .write() et .close() sont des méthodes associées à l'objet f créé par le built-in open
	f.close()

# la built-in open |--> open(path_to_file, mode)
# 	- path_to_file = chemin vers le fichier
# 	- mode : 3 mode possibles :
# 		+ 'r' <-> open for reading text
# 		+ 'w' <-> open for writing text
# 		+ 'a' <-> open for appending text