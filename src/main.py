import ball_box
import matrix

ball_box: list = ball_box.make_ball_box()

for index, ball_number in enumerate(ball_box, 1):
    print(f"ball[{index}]:{ball_number}")


card_org: list[list[int]] = matrix.get_matrix()
card: list[list[int]] = [[row] for row in zip(*card_org)]

count_reach: int = 0
count_bingo: int = 0

for row in card:
    print(row)
print(f"REACH: {count_reach}")
print(f"BINGO: {count_bingo}")
print("-------------")
