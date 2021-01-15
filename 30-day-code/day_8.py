users = int(input())
directory = {}

for _ in range(users):
    name, number = input().split()
    directory[name] = number

while True:
    try:
        query = input()
        if query not in directory:
            print('Not Found')
        else:
            print(f'{query}={directory[query]}')
    except EOFError:
        break
