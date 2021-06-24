import random


def randomNumber(len=1) -> str:
    result = ''
    for i in range(len):
        result += str(random.randint(0, 9))
    return result


print(randomNumber(12))
