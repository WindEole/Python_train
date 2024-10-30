# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    inheritance.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/17 15:10:31 by iderighe          #+#    #+#              #
#    Updated: 2022/10/17 15:23:42 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Dinosaur:
	des = 'All my friends are dead... :('

	def __init__(self):
		print('A dinosaur appeared.')
	
	def roar(self):
		print('ROAAAAR !')

	is_extinct = True

class TRex(Dinosaur): 		# class enfant(parent) <-> enfant hérite de parent
	des = "If you're happy, clap your... oh, nevermind."

if __name__ == '__main__':
	print('Dinosaur case : ')
	print('- Instanciation : ')
	d = Dinosaur()
	print('- Description : ')
	print(d.des)
	print('- Roar : ')
	d.roar()
	print('- Is this extinct ?')
	print(d.is_extinct)
	
	print('\nTRex case : ')
	print('- Instanciation : ')
	t = TRex()
	print('- Description : ')
	print(t.des)
	print('- Roar : ')
	t.roar()
	print('- Is this extinct ?')
	print(t.is_extinct)

# ATTENTION l'enfant hérite de tout ! il doir simplement redéfinir les attributs ou méthodes dont
# il hérite, ou bien rajouter des méthodes en sus de celles dont il a hérité !
# pas de notions de public / privé / protégé comme en cpp !