# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    class.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/15 11:19:17 by iderighe          #+#    #+#              #
#    Updated: 2022/10/15 11:24:12 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == '__main__':
	a = "To be or not to be"	# str
	print(type(a))
	
	b = 5						# int
	print(type(b))

	c = False					# bool
	print(type(c))

	d = None					# correspond a NULL et c'est un type : Nonetype
	print(type(d))

	print(type(type(a)))		# affiche "type"... càd sa classe !