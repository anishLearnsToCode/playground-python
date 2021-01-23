# Geometric Distribution I

numerator, denominator = map(int, input().split())
inspection_no = int(input())

probability_defect = numerator / denominator
probability_fine = 1 - probability_defect

result = (probability_fine ** (inspection_no - 1)) * probability_defect
print(f'{result:.3f}')
