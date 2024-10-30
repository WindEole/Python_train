# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    attributes_methods.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/17 13:39:52 by iderighe          #+#    #+#              #
#    Updated: 2022/10/17 14:02:10 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Dans une classe, on peut definir des attributs (<=> variables) et des méthodes (<=> fonctions)

class Car:
	def drive(self):
		print('Vroom')

	def paint(self, color):
		self.color = color 		# ATTENTION, ici on définit un attribut .color, qui va prendre la valeur color !
		print('%s is now the new color' % str(color))

	def get_color(self):
		return self.color

if __name__ == '__main__':
	x = Car()					# on instancie un objet Car()
	print('Drive method called : ')
	x.drive()					# on n'a pas besoin de préciser le param self !

	print('\nChanging attribute value with a setter : ')
	x.paint('red')
	print('\nPrint getter return : ')
	print(x.get_color())		# ATTENTION : l'attribut color est défini dans la méthode paint. Si on appelle get_color avant paint : crash !
								# ceci peut être évité grâce aux méthodes Constructeur et Destructeur !

	print('\nDirect access to attribute : ')
	x.color = 'blue'
	print(x.color)

# lorsqu'on définit une méthode de class, son 1er paramètre sera toujours self. Self doit tjs être présent !!
# self représente l'instance courante (<=> this en cpp sauf que this est un param fantome)