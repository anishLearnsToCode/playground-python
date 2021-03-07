"""
1 2 3 2 1 3 3 1 2 2 2 2
2
"""
from typing import List


def move_to_last(array: List[int], to_move: int) -> None:
    count_freq = False
    freq = 0

    for index in range(len(array) - 1, -1, -1):
        # count_freq = count_freq or array[index] != to_move
        if array[index] != to_move:
            count_freq = True
        if array[index] == to_move and count_freq:
            freq += 1
            del array[index]

    # append
    array.extend([to_move] * freq)


numbers = list(map(int, input().split()))
# numbers = [2, 1, 2, 2, 2, 3, 4, 2]
move_to_last(numbers, to_move=int(input()))
print(numbers)
