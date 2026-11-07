def ft_count_harvest_recursive(i: int = 1, max: int = 0):
    if i == 1:
        max = int(input("Days until harvest: "))
    print(f"Day {i}")
    i += 1
    if i <= max:
        ft_count_harvest_recursive(i, max)
    else:
        print("Harvest time!")
