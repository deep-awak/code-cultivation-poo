def ft_count_harvest_iterative():
    day_harvest = int(input("Days until harvest: "))
    for days in range(1, day_harvest + 1):
        print(f"Day {days}")
    print("Harvest time!")
