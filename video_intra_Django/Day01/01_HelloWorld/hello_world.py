# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    hello_world.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/14 15:56:43 by iderighe          #+#    #+#              #
#    Updated: 2022/10/14 17:03:45 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# le header 42 est facultatif

# fichier script python hello_world.py = module !

#---------- DEBUT DU BLOC ----------#
if __name__ == '__main__':	# cette condition ouvre un bloc. Syntaxe : finit toujours par :
	s = 'Hello World !' 	# variable s à laquelle on assigne la string Hello World / pas besoin de définir son type.
	print(s) 				# imprime sur la sortie écran
#----------- FIN DU BLOC -----------#
# les blocs sont définis par indentation (il n'y a pas de brackets)

# __main__ |-->	en python, il n'y a pas de fonction main() (en fait, la fct main() est implicitement au top de tout le code...)

# __name__ |-->	c'est une sorte d'include guard. Cette variable est set dès qu'on run un code python. 
# 				Cette variable sert à limiter les exécutions du module si jamais celui-ci n'est pas utilisé comme main program
# 				(c'est à dire s'il est importé)

# pour mieux comprendre l'utilité de __name__ == __main__ : regarder one.py et two.py