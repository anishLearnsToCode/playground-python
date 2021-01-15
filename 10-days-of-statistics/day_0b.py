n = int(input())
numbers = list(map(int, input().split()))
weights = list(map(int, input().split()))

result = 0
for index in range(n):
    result += numbers[index] * weights[index]

result /= sum(weights)
print(round(result, 1))
