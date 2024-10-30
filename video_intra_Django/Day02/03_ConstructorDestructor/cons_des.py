# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cons_des.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/17 14:04:03 by iderighe          #+#    #+#              #
#    Updated: 2022/10/17 14:25:05 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Warrior:
	def __init__(self, name='Bob'):			# Constructeur ! Ici, Bob sera la valeur par defaut. Overridé si on donne un nom lors de l'appel
		self.name = name
		print("A warrior appeared ! His name is %s." % name)
	
	def __del__(self):						# Destructeur !
		print("%s just died..." % self.name)

if __name__ == '__main__':
	bob = Warrior()			# On instancie avec le name par défaut
	tom = Warrior("Tom")	# On instancie avec un nom
	del tom 				# on appelle en dur le Destructeur de tom, mais on n'est pas obligé

# python possède (comme cpp) un ramasse-miette / garbage collector : quand le programme se termine, toutes les 