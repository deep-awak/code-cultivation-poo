from math import sqrt


def get_player_pos() -> tuple[float, float, float]:
    while True:
        position = input("Enter new coordinates as floats in format 'x,y,z':")

        if not position.strip():
            print("Invalid syntax\n")
            continue
        parts = position.split(',')

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x, y, z = [float(value.strip()) for value in parts]
            return (x, y, z)

        except (ValueError, TypeError):
            for value in parts:
                try:
                    float(value.strip())
                except (ValueError, TypeError):
                    print(f"Error on parameter '{value.strip()}'\
: could not convert string to float: '{value.strip()}'")
                    break


def calcul_dist(
    p1: tuple[float, float, float], p2:
    tuple[float, float, float] = (0.0, 0.0, 0.0)
) -> float:
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 +
                (p1[2] - p2[2]) ** 2)


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    coordinates_1 = get_player_pos()
    print(f"Got a first tuple: {coordinates_1})")
    print(f"It include: X={coordinates_1[0]}, Y={coordinates_1[1]}, \
Z={coordinates_1[2]}")
    dist_center = calcul_dist(coordinates_1)
    print(f"Distance to center: {dist_center:.4f}")
    print("\nGet a second set of coordinates")
    coordinates_2 = get_player_pos()
    dist_between = calcul_dist(coordinates_1, coordinates_2)
    print(f"Distance between the 2 sets of coordinates: {dist_between:.4f}")


if __name__ == '__main__':
    main()
