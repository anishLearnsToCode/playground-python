l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

result = []
min_abs = float('inf')

for n in l1:
    for m in l2:
        if abs(m - n) < min_abs:
            min_abs = abs(m - n)
            result = [n, m]

print(result)
