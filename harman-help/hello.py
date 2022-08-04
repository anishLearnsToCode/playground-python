class LetterFilter:
    _vowels = {'a', 'e', 'i', 'o', 'u'}

    def __init__(self, s: str):
        self.only_vowels = self._filter_consonants(s)
        self.only_consonants = self._filter_vowels(s)

    def _is_vowel(self, c: str) -> bool:
        return c in self._vowels

    def _is_consonant(self, c: str) -> bool:
        return not self._is_vowel(c)

    def _filter_vowels(self, s: str) -> str:
        result = ''
        for char in s:
            if self._is_consonant(char):
                result += char
        return result

    def filter_vowels(self) -> str:
        return self.only_consonants

    def _filter_consonants(self, s: str) -> str:
        result = ''
        for char in s:
            if self._is_vowel(char):
                result += char
        return result

    def filter_consonants(self) -> str:
        return self.only_vowels


obj = LetterFilter('hackerrank')
print(obj.filter_vowels())
print(obj.filter_consonants())
