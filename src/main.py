import ball_box
import matrix
from card import Card


def main() -> None:
    balls: list = ball_box.make_ball_box()
    card: Card = Card(matrix.get_matrix())
    count_reach: int = 0
    count_bingo: int = 0

    for index, ball_number in enumerate(balls, 1):
        print(f"ball[{index}]:{ball_number}")
        card.show_card()
        print(f"REACH: {count_reach}")
        print(f"BINGO: {count_bingo}")
        print("-------------")


if __name__ == "__main__":
    main()
