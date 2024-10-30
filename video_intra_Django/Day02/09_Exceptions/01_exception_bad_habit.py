# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    01_exception_bad_habit.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/17 15:36:48 by iderighe          #+#    #+#              #
#    Updated: 2022/10/17 15:48:12 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vegetables:
	pass

class Fries:
	pass

class Human:
	def eat(self, food):
		if isinstance(food, Vegetables):
			raise Exception("I don't like green food !")
		else:
			print('Miam !')

if __name__ == '__main__':
	h = Human()
	h.eat(Fries())
	h.eat(Vegetables())
	h.eat(Fries())

# ici on léve une exception, mais on ne la gére pas, donc le programme crache une erreur et s'arrête...
# ce n'est pas une bonne habitude ! il faut utiliser try / except !