from typing import Dict


def getCharFrequencies(s: str) -> Dict[str, int]:
    frequencies = {}
    for char in s:
        frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies


def getUniqueCharacters(s: str) -> int:
    charFrequencies = getCharFrequencies(s)
    for index, char in enumerate(s):
        if charFrequencies[char] is 1:
            return index + 1
    return -1
