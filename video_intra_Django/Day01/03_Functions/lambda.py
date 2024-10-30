# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    lambda.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/14 18:21:12 by iderighe          #+#    #+#              #
#    Updated: 2022/10/14 18:27:10 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# En python, on peut déclarer des fonctions anonymes avec le mot-clé lambda !

def apply_modifier(modifier, target): # grace a lambda, la variable modifier peut etre utilisée comme une fonction !!
	result = modifier(target)
	return result

if __name__ == '__main__' :
	a = 7
	modifier = lambda x : x / 2 # lambda prend x en paramètre, et le divise par 2 (n'y mettre que des mini-fonctions...)
	b = apply_modifier(modifier, a)
	print(b)