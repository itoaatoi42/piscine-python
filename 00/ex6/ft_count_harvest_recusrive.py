# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recusrive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abenamir <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/11/06 14:54:35 by abenamir          #+#    #+#              #
#    Updated: 2026/11/06 15:35:58 by abenamir         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(i: int = 1, max: int = 0):
    if i == 1:
        max = int(input("Days until harvest: "))
    print(f"Day {i}")
    i += 1
    if i <= max:
        ft_count_harvest_recursive(i, max)
