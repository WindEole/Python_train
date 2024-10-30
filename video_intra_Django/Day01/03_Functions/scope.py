# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scope.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: iderighe <iderighe@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/14 18:08:12 by iderighe          #+#    #+#              #
#    Updated: 2022/10/14 18:19:43 by iderighe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Toujours faire attention à l'endroit ou les variables sont déclarées !

global_var =  "This var is in the global module namespace"

def my_fct():
	local_fct_var = "This var is in the fct namespace"
	
	def inner_fct():
		enclose_fct_var = "This var is in the enclosed fct namespace"
		print('[inner_fct] - ', global_var)
		print('[inner_fct] - ', local_fct_var)
		print('[inner_fct] - ', enclose_fct_var, '\n')
	
	inner_fct()

	print('[my_fct] - ', global_var)
	print('[my_fct] - ', local_fct_var, '\n')
	# print('[my_fct] - ', enclose_fct_var, '\n') # ceci ne fonctionnera pas car enclose_fct_var n'est pas dans le scope my_fct !

if __name__ == '__main__' :
	my_fct()
	print('[global scope] - ', global_var, '\n')
	# print('[global scope] - ', local_fct_var, '\n')  # ceci ne fonctionnera pas car local_fct_var n'est pas dans le scope global !