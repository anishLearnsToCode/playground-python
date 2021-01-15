from typing import List


def max_hourglass_sum(matrix: List[List[int]]) -> int:
    max_sum = -float('inf')
    for i in range(4):
        for j in range(4):
            max_sum = max(max_sum, hourglass_sum(matrix, i, j))
    return max_sum


def hourglass_sum(matrix: List[List[int]], row: int, column: int) -> int:
    return sum(matrix[row][column + i] + matrix[row + 2][column + i] for i in range(3)) + matrix[row + 1][column + 1]


if __name__ == '__main__':
    matrix = []
    for _ in range(6):
        matrix.append(list(map(int, input().split())))
    print(max_hourglass_sum(matrix))
