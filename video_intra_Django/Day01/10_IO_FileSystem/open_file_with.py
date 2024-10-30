# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    open_file_with.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/17 12:14:20 by iderighe          #+#    #+#              #
#    Updated: 2022/10/17 12:17:35 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == '__main__':
	filename = 'my_file.txt'

	with open(filename, 'r') as f:
		for line in f:
			print(line)

# le mot clé with permet de s'assurer qu'après la lecture du fichier, celui-ci sera correctement fermé !
