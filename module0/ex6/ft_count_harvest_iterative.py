def ft_count_harvest_iterative():
    day_cnt = int(input("Days until harvest: "))
    cnt = 0
    while cnt != day_cnt:
        print("Day",cnt+1)
        cnt = cnt +1
    print("Harvest time!")
