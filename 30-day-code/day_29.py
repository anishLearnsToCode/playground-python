def max_bitwise(n: int, k: int) -> int:
    max_bitwise_and = 0
    for i in range(1, n + 1):
        for j in range(1, i):
            current_bitwise_and = i & j
            if max_bitwise_and < current_bitwise_and < k:
                max_bitwise_and = current_bitwise_and
                if max_bitwise_and == k - 1:
                    return max_bitwise_and
    return max_bitwise_and


test_cases = int(input())
for _ in range(test_cases):
    n, k = [int(item) for item in input().split()]
    print(max_bitwise(n, k))
