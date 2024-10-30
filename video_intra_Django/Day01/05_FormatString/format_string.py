# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_string.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/15 13:55:07 by iderighe          #+#    #+#              #
#    Updated: 2022/10/15 14:07:58 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# .format est une méthode du type str, qui permet de formater une string.
# le formatage se fait via l'implémentation de brackets

if __name__ == '__main__':
	base_str = "{0} bites the {1}"	# on peut formater avec des numero, le remplacement se fera de manière consécutive
	print(base_str)
	new_str = base_str.format('Another one', 'dust')
	print(new_str + '\n')

	base_str = "{who} bites the {what}"	# on peut formater avec des variables
	print(base_str)
	new_str = base_str.format(what= 'Another one', who= 'dust')
	print(new_str + '\n')

	base_str = "%s bites the %s"	# on peut formater avec les % (comme dans printf) -> ici %s pour string
	print(base_str)
	new_str = base_str%('She', 'life to the fullest')
	print(new_str)

	base_str = "%d bites the %s"	# on peut formater avec les % (comme dans printf) -> ici %d pour int
	print(base_str)
	new_str = base_str%(42, 'life to the fullest')
	print(new_str)