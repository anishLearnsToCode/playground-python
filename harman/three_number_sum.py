numbers = list(map(int, input().split()))
target = int(input())

frequency = {}
for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

result = []

for i, a1 in enumerate(numbers):
    # removing a1
    if frequency[a1] == 1:
        del frequency[a1]
    else:
        frequency[a1] -= 1

    # dict copy
    iteration_freq = frequency.copy()

    # pairs
    for j in range(i + 1, len(numbers)):
        a2 = numbers[j]
        if iteration_freq[a2] == 1:
            del iteration_freq[a2]
        else:
            iteration_freq[a2] -= 1
        required = target - a1 - a2
        if required in iteration_freq:
            result.append([a1, a2, required])

print(result)
