# 1. 링크드 리스트로 큐 구현하기.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        if self.front is None:
            return print(True)
        else:
            return print(False)

    def put(self, data):
        if self.front is None:
            self.front = Node(data)
            self.tail = self.front
        else:
            node = self.front
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.rear = new

    def get(self):
        if self.front is None:
            return print(None)

        temp = self.front
        self.front = self.front.next
        print(temp.data)
        del temp

    def peek(self):
        if self.front is None:
            return print(None)
        return print(self.front.data)


linked_queue = LinkedQueue()
linked_queue.is_empty()
for data in range(1, 10):
    linked_queue.put(data)

linked_queue.is_empty()

linked_queue.peek()
linked_queue.get()
linked_queue.peek()
linked_queue.get()
linked_queue.peek()


# 2. 스택으로 문자열로 오는 후위연산자 계산하기

class Stack:
    def __init__(self):
        self.list = list()

    def push(self, data):
        self.list.append(data)

    def pop(self):
        return self.list.pop()


class Calculator:
    def __init__(self):
        self.stack = Stack()

    def calculate(self, string):
        CALCULATOR = ['+', '-', '/', '*']
        string = string.split(' ')
        for cal in string:
            if cal not in CALCULATOR:
                self.stack.push(cal)
            else:
                operate2 = int(self.stack.pop())
                operate1 = int(self.stack.pop())
                if cal is CALCULATOR[0]:
                    result = operate1 + operate2
                elif cal is CALCULATOR[1]:
                    result = operate1 - operate2
                elif cal is CALCULATOR[2]:
                    result = operate1 / operate2
                else:
                    result = operate1 * operate2
                self.stack.push(result)
        return self.stack.pop()

calc = Calculator()
print(calc.calculate('4 6 * 2 / 2 +'))
print(calc.calculate('2 5 + 3 * 6 - 5 *'))
