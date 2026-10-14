class Square:
    def __init__(self, value, mark: bool = False):
        self.number = value
        self.marked = mark

    def show_number(self):
        value: str = str(self.number)
        if self.marked:
            return "(" + value + ")"
        return " " + value + " "

    def mark_square(self):
        self.marked = True

    def get_number(self):
        return self.number

    def is_marked(self):
        return self.marked


if __name__ == "__main__":
    square: Square = Square(5)
    print(f"number: {square.show_number()}")

    square.mark_square()
    print(f"number: {square.show_number()}")
