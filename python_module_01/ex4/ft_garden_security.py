class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height: float = height
        self._age = age

    def show(self) -> None:
        print(f"Created: {self.name}: {self._height}cm, {self._age} days old")

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age uptade rejected")
            return
        else:
            self._age = age
            print(f"Age updated: {self._age}")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age uptade rejected")
            return
        else:
            self._height = height
            print(f"Height updated: {self._height}")

    def view(self) -> None:
        print(f"Current state: {self.name}:", end=" ")
        print(f"{self.get_height()}cm, {self.get_age()} days old")


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    rose.show()
    print("\n")
    rose.set_height(25)
    rose.set_age(30)
    print("\n")
    rose.set_height(-42)
    rose.set_age(-42)
    print("\n")
    rose.show()


if __name__ == "__main__":
    main()
