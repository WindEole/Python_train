# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    numeric.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/14 17:05:14 by iderighe          #+#    #+#              #
#    Updated: 2022/10/14 17:12:15 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# il existe trois types numeric en python : int, float et complex (complex ne nous intéresse pas pour l'instant)

if __name__ == '__main__':
	a = 1			# déclaration int implicite
	a = int(1)		# déclaration int explicite
	b = int(a)		# déclaration int explicite

	print(a)
	print(b)

	a = 1.0			# déclaration float implicite
	a = float(1.0)	# déclaration float explicite
	b = float(a)	# déclaration float explicite

	print(a)
	print(b)