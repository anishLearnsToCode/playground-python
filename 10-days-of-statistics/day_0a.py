from typing import List


def mean(numbers: List[int]) -> str:
    return f'{sum(numbers) / len(numbers) :.1f}'


def median(numbers: List[int]) -> str:
    numbers.sort()
    result = numbers[len(numbers) // 2]
    if len(numbers) % 2 == 0:
        result = (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
    return f'{result:.1f}'


def mode(number: List[int]) -> str:
    counter = {}
    for number in numbers:
        counter[number] = counter.get(number, 0) + 1
    max_frequency = max(counter.values())
    current_min = float('inf')
    for key, value in counter.items():
        if value == max_frequency and key < current_min:
            current_min = key
    return current_min


input()
numbers = list(map(int, input().split()))

print(mean(numbers))
print(median(numbers))
print(mode(numbers))
