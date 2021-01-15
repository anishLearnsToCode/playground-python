class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        divisor_sum = 0
        for divisor in range(2, n):
            if n % divisor == 0:
                divisor_sum += divisor
        return divisor_sum + n + (0 if n is 1 else 1)
