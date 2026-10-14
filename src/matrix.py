import random


def get_candidates(column_number: int) -> list[int]:
    match column_number:
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


def transpose_matrix(matrix_org: list[list[int | None]]):
    return [column for column in zip(*matrix_org)]


def get_matrix() -> list[list[int | None]]:
    column_range: int = 6
    row_range: int = 5
    matrix_org: list[list[int | str]] = []

    for column_number in range(1, column_range):
        candidates: list[int] = get_candidates(column_number)

        # FREEが入るため、3列目のみ数字が一つ少なくなる
        if column_number == 3:
            matrix_org.append(random.sample(candidates, k=row_range - 1))
        else:
            matrix_org.append(random.sample(candidates, k=row_range))

    # カードの真ん中にFREEを配置
    matrix_org[2].insert(2, None)

    matrix: list[list[int | None]] = transpose_matrix(matrix_org)

    return matrix
