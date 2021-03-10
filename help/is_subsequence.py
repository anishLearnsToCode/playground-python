def is_subsequence(array, subsequence) -> bool:
    i = 0
    for element in array:
        if element == subsequence[i]:
            if i == len(subsequence) - 1:
                return True
            else:
                i += 1
    return False


array = list(map(int, input().split()))
subsequence = list(map(int, input().split()))
print(is_subsequence(array, subsequence))
