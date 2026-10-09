count_pick: int = 1
ball_number: int = 1

card: list[int[int]] = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

count_reach: int = 0
count_bingo: int = 0

print(f"ball[{count_pick}]:{ball_number}")
for row in card:
    print(row)
print(f"REACH: {count_reach}")
print(f"BINGO: {count_bingo}")
print("-------------")
