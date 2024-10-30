# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    docstring.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/14 17:59:36 by iderighe          #+#    #+#              #
#    Updated: 2022/10/14 18:07:23 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Un docstring permet de documenter une fonction.
# syntax : Triple double quote + texte descriptif + Triple double quote

def hello_world():
	"""
		this function prints Hello World !
	"""
	print('Hello World !')

if __name__ == '__main__' :
	help(hello_world)
	hello_world()		# on appelle la fonction qu'on vient de définir

# pour avoir accès à cette documentation, on utilise le mot-clé help(nom_de_fct). Le built-in help va ouvrir une page (un peu comme un man)
# sur le terminal, et display le contenu du docstring entre triple double quote. Comme dans un man, on quitte avec Q