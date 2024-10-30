# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    classes.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/17 13:32:24 by iderighe          #+#    #+#              #
#    Updated: 2022/10/17 13:36:43 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# la Classe est le moule à gateau dont on sort l'instance objet

class Foo:
	pass

class Bar:
	pass

if __name__ == '__main__':
	f = Foo()
	b = Bar()
	i = int(1)
	print(type(f))
	print(type(b))
	print(type(i))

# The pass statement is used as a placeholder for future code. When the pass statement is
# executed, nothing happens, but you avoid getting an error when empty code is not allowed. 
# Empty code is not allowed in loops, function definitions, class definitions, or in if statements.