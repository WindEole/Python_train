# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    identity_comparison.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/15 17:00:56 by iderighe          #+#    #+#              #
#    Updated: 2022/10/15 17:05:48 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == '__main__':
	a = int(1)
	b = float(1)
	print('a of type	', type(a), ' and value	', a)
	print('b of type	', type(b), ' and value	', b)

	if a == b :									# ici on compare les valeurs
		print('a has the same value as b')
	else :
		print('a has NOT the same value as b')

	if a is b :									# opérateur is : compare les types / classes / objects
		print("a is the same object as b")
	else :
		print("a is NOT the same object as b")