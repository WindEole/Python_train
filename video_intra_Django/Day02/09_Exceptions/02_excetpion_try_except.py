# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_excetpion_try_except.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/17 15:43:35 by iderighe          #+#    #+#              #
#    Updated: 2022/10/17 15:48:32 by iderighe         ###   ########.fr        #
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
	try:
		h.eat(Vegetables())
	except Exception as e:
		print(e)
	h.eat(Fries())

# le bloc try/except est équivalent au try/catch du cpp. L'exception est gérée, et le code peut continuer !