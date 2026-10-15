import random


def make_ball_box() -> list[int]:
    return random.sample(list(range(1, 76)), k=75)


if __name__ == "__main__":
    print(make_ball_box())
