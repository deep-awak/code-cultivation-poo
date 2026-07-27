#!/usr/bin/env python3


def ft_garden_intro() -> str:
    name: str = "Rose"
    height: float = 25.0
    age: int = 30
    return (f"Plant: {name}\nHeight:{height}cm\nAge: {age} days \n")


def main() -> None:
    print("=== Welcome to My garden ===")
    print(ft_garden_intro())
    print("\n=== End of Program ===")


if __name__ == "__main__":
    main()
