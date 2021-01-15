n = int(input())
names = []
for _ in range(n):
    name, email= input().split()
    if email.endswith('@gmail.com'):
        names.append(name)

names.sort()
for name in names:
    print(name)
