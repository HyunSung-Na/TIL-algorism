class PriorityQueue:
    def __init__(self):
        self.heap_array = list()

    def is_empty(self):
        if self.heap_array:
            return False
        return True

    def put(self, data):
        pass

    def get(self):
        pass

    def peek(self):
        pass


def countUniques(a):
    stack = []
    for number in a:
        if not stack:
            stack.append(number)
        else:
            if stack[-1] == number:
                continue
            else:
                stack.append(number)
    return len(stack)

print(countUniques([-1, 1, 1, 1, 1, 4, 4, 4, 4, 10, 14, 14]))  # 5
print(countUniques([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))  # 2


def solution(a):
    stack = []
    num_stack = []
    num = 0
    for char_list in a:
        if not stack:
            stack = list(char_list)
            continue
        else:
            for index in range(len(stack)):
                next_char = list(char_list)
                if stack[index] == next_char[index]:
                    num += 1
                else:
                    break
            num_stack.append(num)
            num = 0
    return min(num_stack)


print(solution(['abcd', 'abce', 'abchg', 'abcfwqw', 'abcdfg']))  # 3
print(solution(['abcd', 'gbce', 'abchg', 'abcfwqw', 'abcdfg']))  # 0


def solution(n):

    return True


print(solution(19))  # True
print(solution(61))  # False