# Spearman's Rank Correlation Coefficient
from typing import List


def rank(data: List[float]) -> List[int]:
    sorted_elements = sorted(set(data))
    rank_map = {element: index for index, element in enumerate(sorted_elements)}
    return [rank_map[element] + 1 for element in data]


n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

r_x = rank(X)
r_y = rank(Y)
d_squared_sum = sum(map(lambda x: (x[0] - x[1]) ** 2, zip(r_x, r_y)))
result = 1 - (6 * d_squared_sum) / (n * (n ** 2 - 1))
print(round(result, 3))
