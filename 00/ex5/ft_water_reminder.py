# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abenamir <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/11/06 14:44:39 by abenamir          #+#    #+#              #
#    Updated: 2026/11/06 14:46:36 by abenamir         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    warn = int(input("Days since last watering: "))
    if warn > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
