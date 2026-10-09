import random


def make_ball_box() -> list[int]:
    numbers: list[int] = list(range(1, 76))
    return random.sample(numbers, k=75)


if __name__ == "__main__":
    print(make_ball_box())
