def solve_coin_change(denominations, amount):
  solution = [0] * (amount + 1)
  solution[0] = 1
  for den in denominations:
    for i in range(den, amount + 1):
      solution[i] += solution[i - den] 

  return solution[len(solution) - 1]


print(solve_coin_change([1, 2, 5], 7))
