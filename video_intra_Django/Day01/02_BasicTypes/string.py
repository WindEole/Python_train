# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    string.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/14 17:09:14 by iderighe          #+#    #+#              #
#    Updated: 2022/10/14 17:29:14 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == '__main__':
	a = 'This is a string'
	b = str("This is another string")
	c = str(b)

	print(a)
	print(c)
	
	# ---------- usage des quotes ---------- #
	
	# si on veut insérer des doubles quotes dans le texte : entourer de single quotes
	a = 'I can put double quotes " <- like this -> " '
	print(a)
	
	# si on veut insérer des single quotes dans le texte : entourer de double quotes
	a = "I can put single quotes ' <- like this -> ' "
	print(a)
	
	# si on veut une liberté totale : triple quotes (double ou simple)
	a = """ 
		'I can put what I "want' and tabulations and carriage 
	returns are	preserved'.
	"""
	print(a)
	
	a = '''
'I can put what I "want' and tabulations and carriage returns are
also preserved'. ATTENTION indentation en sortie !
		'''
	print(a)

	# ---------- afficher tout ou partie d'une string ---------- #
	beatles = "Hey Jude, don't make me bad !"
	print(beatles[0]) # affiche le char 0 de la string
	print(beatles[1]) # affiche le char 1 de la string
	print(beatles[2]) # affiche le char 2 de la string
	print(beatles[4:8]) # affiche du 4ème au 8ème char de la string
	
# ATTENTION ! En python, on ne peut pas changer un charactere dans une string en faisant : beatles[0] = 'Z' par exemple !
# donc si on veux changer un char, il faut passer par une copie de la string d'origine !