# Poisson Distribution II

lambda_1, lambda_2 = map(float, input().split())
cost_1 = 160 + 40 * (lambda_1 + lambda_1 ** 2)
cost_2 = 128 + 40 * (lambda_2 + lambda_2 ** 2)

print(f'{cost_1:.3f}')
print(f'{cost_2:.3f}')
