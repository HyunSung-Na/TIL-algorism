class PriorityQueue:
    def __init__(self):
        self.heap_array = list()
    def is_empty(self):
        if self.heap_array:
            return False
        return True

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def put(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)

        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx //2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]

    def move_down(self,poped_idx):
        left_child_popped_idx = poped_idx * 2
        right_child_popped_idx = poped_idx * 2 + 1
        # case1 왼쪽 자식 노드가 없을때
        if left_child_popped_idx >= len(self.heap_array):
            return False
        # case2 오른쪽 자식 노드가 없을때
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False
        # case 3 왼쪽, 오른쪽 자식 노드 둘다 있을때
        else:
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[poped_idx] < self.heap_array[right_child_popped_idx]:
                    return True
                else:
                    return False

    def get(self):
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1
            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[
                                                                                              left_child_popped_idx], \
                                                                                          self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx
            else:
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[
                                                                                                  left_child_popped_idx], \
                                                                                              self.heap_array[
                                                                                                  popped_idx]
                        popped_idx = left_child_popped_idx
                else:
                    if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[
                                                                                                   right_child_popped_idx], \
                                                                                               self.heap_array[
                                                                                                   popped_idx]
                        popped_idx = right_child_popped_idx

        return print(returned_data)

    def peek(self):
        if len(self.heap_array) <= 1:
            return None
        return print(self.heap_array[1])

pri = PriorityQueue()
pri.put(10)
pri.put(11)
pri.put(15)
pri.put(12)
pri.put(9)
pri.get()
pri.peek()

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
    th = {}

    while True:
        temp = 0
        for c in str(n):
            temp += int(c) * int(c)
        if temp == 1:
            return True

        n = temp

        if temp in th:
            return False
        else:
            th[temp] = 1


print(solution(19))  # True
print(solution(61))  # False