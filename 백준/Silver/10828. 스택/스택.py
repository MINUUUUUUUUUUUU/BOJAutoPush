import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            node = Node(data)
            node.next = self.top
            self.top = node
        self.count += 1

    def pop(self):
        if self.top is None:
            return -1
        else:
            node = self.top
            self.top = self.top.next
            self.count -= 1
            return node.data

    def size(self):
        return self.count

    def empty(self):
        return int(self.top is None)

    def topp(self):
        if self.top is None:
            return -1
        else:
            return self.top.data

if __name__ == "__main__":
    s = Stack()
    n = int(sys.stdin.readline())

    commands = sys.stdin.read().splitlines()

    result = []
    for command in commands:
        op = command.split()[0]
        if op == 'push':
            s.push(int(command.split()[1]))
        elif op == 'pop':
            result.append(str(s.pop()))
        elif op == 'size':
            result.append(str(s.size()))
        elif op == 'empty':
            result.append(str(s.empty()))
        elif op == 'top':
            result.append(str(s.topp()))

    sys.stdout.write('\n'.join(result))