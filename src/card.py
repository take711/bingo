from square import Square


class Row:
    def __init__(self, row: list[int | None]):
        self.data: list[Square] = []
        for square in row:
            if square == None:
                self.data.append(Square("FREE", True))
            else:
                self.data.append(Square(square))

    def show_row(self):
        numbers: list[str] = []
        for square in self.data:
            numbers.append(square.show_number())
        return numbers

    def mark_number(self, number: int):
        for square in self.data:
            if square.get_number() == number:
                square.mark_square()

    def is_reach(self):
        count_marked: int = 0
        for square in self.data:
            if square.is_marked():
                count_marked += 1
        return count_marked == 4

    def is_marked(self, column_number: int):
        return self.data[column_number].is_marked()


class Card:
    def __init__(self, matrix: list[list[int | None]]):
        self.data: list[Row] = []
        for row in matrix:
            self.data.append(Row(row))

    def show_card(self):
        for row in self.data:
            print(row.show_row())

    def mark_number(self, number: int):
        for row in self.data:
            row.mark_number(number)

    def count_reach(self):
        count_row: int = 0
        count_column: int = 0
        count_diagonal: int = 0

        # 行方向のリーチをカウント
        for row in self.data:
            if row.is_reach():
                count_row += 1

        # 列方向のリーチをカウント
        index_range: int = 5
        for column_index in range(index_range):
            count_column_marked: int = 0
            for column in self.data:
                if column.is_marked(column_index):
                    count_column_marked += 1
            if count_column_marked == 4:
                count_column += 1

        # 左上→右下方向の対角線上のリーチをカウント
        count_upper_left_to_lower_right: int = 0
        for index, row in enumerate(self.data, 0):
            if row.is_marked(index):
                count_upper_left_to_lower_right += 1
        if count_upper_left_to_lower_right == 4:
            count_diagonal += 1

        # 右上→左下方向の対角線上のリーチをカウント
        count_upper_right_to_lower_left: int = 0
        for index, row in enumerate(self.data, 0):
            if row.is_marked(4 - index):
                count_upper_right_to_lower_left += 1
        if count_upper_right_to_lower_left == 4:
            count_diagonal += 1

        return count_row + count_column + count_diagonal

    def count_bingo(self):
        count_row: int = 0
        count_column: int = 0
        count_diagonal: int = 0


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

    # test_number: int = 1
    # card.mark_number(test_number)
    card.mark_number(1)
    card.mark_number(2)
    card.mark_number(3)
    card.mark_number(4)

    card.mark_number(16)
    card.mark_number(31)
    card.mark_number(46)

    card.mark_number(17)
    card.mark_number(49)

    card.mark_number(19)
    card.mark_number(47)
    card.mark_number(61)

    card.show_card()
    print(f"reach: {card.count_reach()}")
