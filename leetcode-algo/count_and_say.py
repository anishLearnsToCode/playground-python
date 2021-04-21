class Solution:
    def count_and_say(self, n: int) -> str:

        def print_number(s, number):
            if number == 1:
                return s
            new = ""
            start, end, count = 0, 0, 0

            while end <= len(s) - 1:
                if s[end] != s[start]:
                    new = new + str(count) + s[start]
                    start = end
                    count = 0
                else:
                    count = count + 1
                    end = end + 1

            new = new + str(count) + s[start]
            return print_number(new, number - 1)

        return print_number("1", n)
