import re


class Node:
    def __init__(self):
        self.port = ''

    def __setattr__(self, key, value):
        if key == 'Port':
            self.port = int(value)
        else:
            super.__setattr__(self, key, value)


file = open('output.txt', 'r')

pattern = re.compile('^sahasrat_')
equals_to = re.compile('=')
node = Node()
nodes = []

for line in file.readlines():
    if len(pattern.findall(line)) > 0:
        nodes.append(node)
        node = Node()
    else:
        match = equals_to.search(line)
        if match:
            node.__setattr__(line[0:match.start()].strip(), line[match.end():].strip())

nodes.append(node)
nodes = nodes[1:]

print(nodes[1].__dict__)
