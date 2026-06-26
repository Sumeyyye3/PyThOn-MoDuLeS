def    ft_water_reminder():
    day_total = int(input("Days since last watering: "))
    if day_total > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
