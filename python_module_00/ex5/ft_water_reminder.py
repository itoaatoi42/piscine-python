def ft_water_reminder():
    warn = int(input("Days since last watering: "))
    if warn > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
