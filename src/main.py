import ball_box
import matrix
from card import Card


def main() -> None:
    balls: list = ball_box.make_ball_box()
    card: Card = Card(matrix.get_matrix())

    for index, ball_number in enumerate(balls, 1):
        card.mark_number(ball_number)

        print(f"ball[{index}]:{ball_number}")
        card.show_card()
        print(f"REACH: {card.count_reach()}")
        print(f"BINGO: {card.count_bingo()}")
        print("-------------")


if __name__ == "__main__":
    main()
