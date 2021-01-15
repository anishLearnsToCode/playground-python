def binary(n: int) -> str:
    return bin(n)[2:]


def max_consecutive_ones_in_binary(number: int) -> int:
    binary_repr = binary(number)
    max_ones = 0
    current = 0
    for char in binary_repr:
        if char is '1':
            current += 1
        else:
            current = 0
        max_ones = max(max_ones, current)
    return max_ones


number = int(input())
print(max_consecutive_ones_in_binary(number))
