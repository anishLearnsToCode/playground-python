# Geometric Distribution II

numerator, denominator = map(int, input().split())
max_inspections = int(input())
probability_defect = numerator / denominator
probability_fine = 1 - probability_defect
result = 0
for i in range(5):
    result += (probability_fine ** i) * probability_defect

print(f'{result:.3f}')
