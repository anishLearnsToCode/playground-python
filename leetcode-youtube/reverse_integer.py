class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        is_negative = x < 0
        x = -x if is_negative else x
        while x > 0:
            r = 10 * r + x % 10
            x //= 10
        if r not in range(-2 ** 31, 2 ** 31 - 1):
            return 0
        return -r if is_negative else r
