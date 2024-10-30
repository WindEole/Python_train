# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    conditions.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/15 16:56:19 by iderighe          #+#    #+#              #
#    Updated: 2022/10/15 16:59:43 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# conditions = if / elif / else :

def what_is_love(love):
	if love == True :
		print('Love is true')
	elif love == False :
		print('Love is not true')
	else:
		print("What is love ? Baby don't hurt me, no more")

if __name__ == '__main__':
	what_is_love(None)