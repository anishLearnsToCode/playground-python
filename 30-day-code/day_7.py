n = int(input())
numbers = list(map(int, input().split()))

for index in range(n):
    print(numbers[n - 1 - index], end=' ')
