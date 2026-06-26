def ft_count_harvest_recursive():
    day_cnt = int(input("Days until harvest: "))
    def ft_recursive(cnt : int):
        if cnt>day_cnt:
            print("Harvest time!")
        else:
            print("Day",cnt)
            ft_recursive(cnt+1)
    ft_recursive(1)
