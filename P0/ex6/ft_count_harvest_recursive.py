def ft_count_harvest_recursive():
    days_harvest = int(input("Days until harvest: "))

    def recursive(i):
        if (i < (days_harvest + 1)):
            print(f"Day {i}")
            recursive(i + 1)
        else:
            print("Harvest time!")
    recursive(1)
