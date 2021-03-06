from typing import List


def max_area_under_histogram(array: List[int]):
    array.append(0)
    stack = []
    max_area = 0

    for index, element in enumerate(array):
        if len(stack) == 0 or stack[-1] <= element:
            stack.append(element)
        else:
            while len(stack) != 0 and stack[-1] > element:
                current = stack.pop()
                max_area = max(max_area, current * (index + 1)) if len(stack) == 0 else current * (index - stack[-1])
            stack.append(element)


    while len(stack) != 0:
      current = stack.pop()
      max_area = max(max_area, current * (len(array) + 1)) if len(stack) == 0 else current * (len(array) - stack[-1])


    return max_area


array = list(map(int, input().split()))
print(max_area_under_histogram(array))
