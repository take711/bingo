import random


def get_candidates(row_number: int) -> list[int]:
    match row_number:
        case 1:
            return list(range(1, 16))
        case 2:
            return list(range(16, 31))
        case 3:
            return list(range(31, 46))
        case 4:
            return list(range(46, 61))
        case 5:
            return list(range(61, 76))


def get_matrix() -> list[list[int | str]]:
    row_range: int = 6
    line_range: int = 5
    matrix: list[list[int | str]] = []

    for row_number in range(1, row_range):
        candidates: list[int] = get_candidates(row_number)

        # FREEが入るため、3列目のみ数字が一つ少なくなる
        if row_number == 3:
            matrix.append(random.sample(candidates, k=line_range - 1))
        else:
            matrix.append(random.sample(candidates, k=line_range))

    # カードの真ん中にFREEを配置
    matrix[2].insert(2, "FREE")
    return matrix
