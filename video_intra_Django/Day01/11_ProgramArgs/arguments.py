# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    arguments.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/17 12:18:48 by iderighe          #+#    #+#              #
#    Updated: 2022/10/17 12:21:36 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Comment passer des arguments à notre programme ?

import sys

if __name__ == '__main__':
	print(sys.argv)

# sys est un module, argv est un de ses attributs. Ensuite on pourra se balader dans les arg...