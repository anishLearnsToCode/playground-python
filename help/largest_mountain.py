# array = list(map(int, input().split()))
array = [1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5]
largest_mountain = 0
ascending = True

i = 1
mountain_start_index = 0

while i < len(array):
    if ascending and array[i] < array[i - 1]:
        ascending = False
    if not ascending and array[i] > array[i - 1]:
        largest_mountain = max(largest_mountain, i - mountain_start_index)
        mountain_start_index = i - 1
        ascending = True
    i += 1
largest_mountain = max(largest_mountain, i - mountain_start_index)

print(largest_mountain)
