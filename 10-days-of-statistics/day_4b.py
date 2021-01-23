from math import factorial

def C(n: int, r: int) -> int:
    return factorial(n) // (factorial(n - r) * factorial(r))


def P(n: int, r: int, p: float, q: float) -> float:
    return C(n, r) * (p ** r) * (q ** (n - r))


probability_defective, batch_size = map(float, input().split())
probability_defective, batch_size = probability_defective / 100, int(batch_size)
p, q = probability_defective, 1 - probability_defective

# no more than 2 defective pistons
result = P(10, 0, p, q) + P(10, 1, p, q) + P(10, 2, p, q)
print(f'{result:.3f}')

# at least 2 rejects
result = 1 - result + P(10, 2, p, q)
print(f'{result:.3f}')
