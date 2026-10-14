from square import Square


class Line:
    def __init__(self, line: list[int | None]):
        self.data: list[Square] = []
        for square in line:
            if square == None:
                self.data.append(Square("FREE", True))
            else:
                self.data.append(Square(square))

    def show_line(self):
        numbers: list[str] = []
        for square in self.data:
            numbers.append(square.show_number())
        return numbers


class Card:
    def __init__(self, matrix: list[list[int | None]]):
        self.data: list[Line] = []
        for line in matrix:
            self.data.append(Line(line))

    def show_card(self):
        for line in self.data:
            print(line.show_line())


if __name__ == "__main__":
    matrix: list[list[int | None]] = [
        [1, 16, 31, 46, 61],
        [2, 17, 32, 47, 62],
        [3, 18, None, 48, 63],
        [4, 19, 34, 49, 64],
        [5, 20, 35, 50, 65],
    ]

    card: Card = Card(matrix)
    card.show_card()
