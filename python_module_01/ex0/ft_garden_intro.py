def ft_garden_intro(name: str, height: int, age: int) -> None:
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}\nHeight: {height}\nAge: {age} days\n")
    print("=== End of Program ===")


def main() -> None:
    ft_garden_intro("Salvia", 42, 24)


if __name__ == "__main__":
    main()
