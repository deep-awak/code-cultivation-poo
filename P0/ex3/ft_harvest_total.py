def ft_harvest_total():
    totals = (
        int(input("Day 1 harvest: "))
        + int(input("Day 2 harvest: "))
        + int(input("Day 3 harvest: "))
    )
    print(f"Total harvest: {totals}")
