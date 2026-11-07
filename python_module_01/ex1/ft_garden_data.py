class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    plant1 = Plant("Salvia", 42, 24)
    plant2 = Plant("Weed", 24, 42)
    plant3 = Plant("rose", 12, 15)

    plant1.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":
    main()
