class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height: float = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def aging(self) -> None:
        self.age += 1

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)


def main() -> None:
    plant = Plant("Salvia", 42, 24)
    tot_height = plant.height
    print("=== Garden Plant Growth ===")
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.aging()
        plant.grow()
        plant.show()
    tot_height = round(plant.height - tot_height, 1)
    print(f"Growth this week: {tot_height}cm")


if __name__ == "__main__":
    main()
