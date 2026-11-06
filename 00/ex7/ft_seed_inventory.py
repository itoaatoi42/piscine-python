# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abenamir <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/11/06 15:37:09 by abenamir          #+#    #+#              #
#    Updated: 2026/11/06 16:04:21 by abenamir         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit:str):
    seed_type = seed_type.capitalize()
    if unit == "packets":
        print(f"{seed_type} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{seed_type} seeds: {quantity} {unit} total")
    elif  unit == "area":
        print(f"{seed_type} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
