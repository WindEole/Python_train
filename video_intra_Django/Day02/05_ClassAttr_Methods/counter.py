# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    counter.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/17 14:48:52 by iderighe          #+#    #+#              #
#    Updated: 2022/10/17 14:57:43 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# ici on va utiliser un decorateur type : le classmethod, appelé via la syntaxe @

class Foo:
	counter = 0

	def __init__(self):						# Constructeur !
		self.increment_counter()
		print("Foo instance created. Number of instances : [%d]." % self.counter)
	
	def __del__(self):						# Destructeur !
		self.decrement_counter()
		print("Foo instance deleted. Number of instances : [%d]." % self.counter)
	
	@classmethod
	def increment_counter(cls):
		cls.counter += 1

	@classmethod
	def decrement_counter(cls):
		cls.counter -= 1

# cls <=> class ! donc ce sera le counter de la class qui sera appelé / incrémenté / décrémenté !

if __name__ == '__main__':
	a = Foo()
	del a 
	a = Foo()
	b = Foo()
	c = Foo()
	del b
	b = Foo()