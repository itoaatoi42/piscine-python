
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height: float = height
        self._age: int = age

    def show(self) -> None:
        print(
            f"{self.name}: {self._height}cm, "
            f"{self._age} days old"
        )

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return

        self._age = age
        print(f"Age updated: {self._age}")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return

        self._height = height
        print(f"Height updated: {self._height}")

    def view(self) -> None:
        print(f"Current state: {self.name}:", end=" ")
        print(
            f"{self.get_height()}cm, "
            f"{self.get_age()} days old"
        )


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.has_bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")

        if not self.has_bloomed:
            print(f"{self.name} has not bloomed yet")

    def blooming(self) -> None:
        self.has_bloomed = True
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)

        if (
            isinstance(trunk_diameter, float)
            and trunk_diameter >= 0
        ):
            self._trunk_diameter = trunk_diameter
        else:
            raise ValueError(
                "Trunk diameter must be a positive float."
            )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height}cm long and "
            f"{self._trunk_diameter}cm wide."
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        nutritional_value: int
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def age(self, dayspassed: int) -> None:
        if dayspassed < 0:
            print("Error: days cannot be negative")
            return

        self.set_age(self._age + dayspassed)
        self.nutritional_value += dayspassed

    def grow(self) -> None:
        self.set_height(self._height + 42.0)


def main() -> None:
    print("=== Garden Plant Types ===")

    # FLOWER
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()

    print("[asking the rose to bloom]")
    rose.blooming()
    rose.show()

    # TREE
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()

    print("[asking the oak to produce shade]")
    oak.produce_shade()

    # VEGETABLE
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()

    print("[make tomato grow and age for 20 days]")
    tomato.grow()
    tomato.age(20)
    tomato.show()


if __name__ == "__main__":
    main()

