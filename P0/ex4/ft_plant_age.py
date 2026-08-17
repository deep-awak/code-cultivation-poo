def ft_plant_age():
    plant_age_day = int(
        input("Enter plant age in days: ")
        )
    if (plant_age_day <= 60):
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")
