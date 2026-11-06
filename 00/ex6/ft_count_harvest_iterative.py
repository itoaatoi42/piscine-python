# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abenamir <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/11/06 14:49:34 by abenamir          #+#    #+#              #
#    Updated: 2026/11/06 15:35:51 by abenamir         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    max = int(input("Days until harvest: "))
    for i in range(1, max + 1):
              print(f"Day {i}")
