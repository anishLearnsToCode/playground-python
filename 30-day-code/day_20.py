# Bubble Sort

def bubble_sort(array: list) -> tuple:
    """"will return the sorted array, and number of swaps"""
    total_swaps = 0
    for i in range(len(array)):
        swaps = 0
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swaps += 1
                total_swaps += 1
        if swaps == 0:
            break

    return array, total_swaps


_ = int(input())
array = list(map(int, input().split()))
array, total_swaps = bubble_sort(array)
print(f'Array is sorted in {total_swaps} swaps.')
print(f'First Element: {array[0]}')
print(f'Last Element: {array[-1]}')
