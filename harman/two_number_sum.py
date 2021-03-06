numbers = list(map(int, input().split()))
target = int(input())

frequency = {}
for i in numbers:
    frequency[i] = frequency.get(i, 0) + 1

result = []
for i in numbers:
    if frequency.get(i, 0) > 1:
        frequency[i] -= 1
    elif frequency.get(i, 0) == 1:
        del frequency[i]
    required = target - i
    if required in frequency:
        result.append(i)
        result.append(required)

print(result)
