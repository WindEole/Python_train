# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    while_loop.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/17 11:41:19 by iderighe          #+#    #+#              #
#    Updated: 2022/10/17 11:44:17 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# le while du langage C s'utilise aussi en python !

if __name__ == '__main__':
	my_list = [1, 2, 3, 4, 5]
	
	print('my_list')
	i = 0
	while i < len(my_list):
		print(my_list[i])
		i += 1