from typing import Union


class Calculator:
    def power(self, base: int, exponent: int) -> Union[ValueError, int, float]:
        if base < 0 or exponent < 0:
            return ValueError('n and p should be non-negative')
        return base ** exponent
