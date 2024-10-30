# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scope.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/17 14:58:42 by iderighe          #+#    #+#              #
#    Updated: 2022/10/17 15:07:45 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# un scope est défini par son indentation !!

class Bar:
	des = 'Bar in main.'

class Foo:
	des = 'Foo in main'
	
	class Bar:
		des = 'Bar in Foo'
	
	class Foo:
		def method(self):
			print('This is a method in foo.foo')

if __name__ == '__main__':
	print('Description of Bar in main scope : ')
	print('- From class :')
	print(Bar.des)
	print('- From instance :')
	b = Bar()
	print(b.des)

	print('\nDescription of Bar in foo : ')
	print('- From class :')
	print(Foo.Bar.des)
	print('- From instance :')
	fb = Foo.Bar()
	print(fb.des)

	print('\nMethod class (method() from Foo.Foo instance')
	ff = Foo.Foo()
	ff.method()