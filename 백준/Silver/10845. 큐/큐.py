## 10845 큐
import sys

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.count = 0

  def push(self,data):
    if self.front is None:
      self.front = self.rear = Node(data)
    else:
      node = Node(data)
      self.rear.next = node
      self.rear = node
    self.count += 1

  def pop(self):
    if self.front is None:
      return -1
    node = self.front
    if self.front == self.rear:
      self.front = self.rear = None
    else:
      self.front = self.front.next
    self.count -= 1
    return node.data

  def size(self):
    if self.front is None:
      return 0
    else:
      return self.count

  def empty(self):
    return int(self.front is None)

  def frontt(self):
    if self.front is None:
      return -1
    else:
      return self.front.data
  
  def rearr(self):
    if self.rear is None:
      return -1
    else:
      return self.rear.data


if __name__ == "__main__":
    s = Queue()
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
        elif op == 'front':
            result.append(str(s.frontt()))
        elif op == 'back':
            result.append(str(s.rearr()))

    sys.stdout.write('\n'.join(result))