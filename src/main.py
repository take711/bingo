import ball_box

ball_box: list = ball_box.make_ball_box()

for index, ball_number in enumerate(ball_box, 1):
    print(f"ball[{index}]:{ball_number}")


card: list[int[int]] = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

count_reach: int = 0
count_bingo: int = 0

for row in card:
    print(row)
print(f"REACH: {count_reach}")
print(f"BINGO: {count_bingo}")
print("-------------")
