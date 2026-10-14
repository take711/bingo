class Square:
    def __init__(self, value, mark: bool = False):
        self.number = value
        self.is_marked = mark

    def show_number(self):
        value: str = str(self.number)
        if self.is_marked:
            return "(" + value + ")"
        return " " + value + " "

    def mark_square(self):
        self.is_marked = True

    def get_number(self):
        return self.number


if __name__ == "__main__":
    square: Square = Square(5)
    print(f"number: {square.show_number()}")

    square.mark_square()
    print(f"number: {square.show_number()}")
