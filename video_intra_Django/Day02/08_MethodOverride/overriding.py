# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    overriding.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/17 15:25:12 by iderighe          #+#    #+#              #
#    Updated: 2022/10/17 15:35:07 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Dans le cadre de l'héritage, si l'enfant veut changer une méthode héritée du 
# parent : on utilise le polymorphisme (<=> method overriding)

class Dinosaur:
	des = 'All my friends are dead... :('

	def __init__(self):
		print('A dinosaur appeared.')
	
	def roar(self):
		print('ROAAAAR !')

	is_extinct = True

class Chicken(Dinosaur):
	des = 'Great camera stabilisator !'
	
	def __init__(self):
		super().__init__() 		# super permet d'accéder aux attributs et méthodes d'une classe parente ! dc ici on appelle le __init__ de Dinosaur
		print("It's a chicken !")
	
	def roar(self):
		print('Cot cot codec !')
	
	is_extinct = False

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

	print('\nChicken case : ')
	print('- Instanciation : ')
	c = Chicken()
	print('- Description : ')
	print(c.des)
	print('- Roar : ')
	c.roar()
	print('- Is this extinct ?')
	print(c.is_extinct)