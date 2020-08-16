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


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root):
        self.root = root

    def preorder(self):
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                print(root.data)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)

root = Node(5, Node(2, Node(7, Node(4), Node(1)), Node(3)), Node(9, Node(6), Node(10)))
tree = Tree(root)
tree.preorder()


class HashTable:
    def __init__(self):
        self.table = [None] * 10

    @staticmethod
    def hash_func(key):
        return ord(key[0]) % 10

    def set(self, key, value):
        self.table[self.hash_func(key)] = value

    def get(self, key):
        return self.table[self.hash_func(key)]


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


class ChainedHashTable(HashTable):

    def insert(self, key, value):
        gen_key = hash(key)
        hash_value = self.hash_func(gen_key)
        if self.table[hash_value] != 0:
            for i in range(len(self.table)):
                if not self.table[hash_value][i]:
                    self.table[hash_value][i].append([value])
        else:
            self.table[hash_value] = [[gen_key, value]]

    def read(self, key):
        gen_key = hash(key)
        hash_value = self.hash_func(gen_key)
        if self.table[hash_value] != 0:
            for i in range(len(self.table[hash_value])):
                if self.table[hash_value][i][0] == gen_key:
                    return self.table[hash_value][i][1]
            return None
        else:
            return None
