test_cases = int(input())

for _ in range(test_cases):
    string = input()
    print(f'{string[::2]} {string[1::2]}')
