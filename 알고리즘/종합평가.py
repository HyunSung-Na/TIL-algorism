def is_palindrome(word):
    list_word = list(word)
    for i in range(0, len(list_word) // 2):

        if list_word[i] == list_word[len(list_word) - 1 - i]:
            continue
        else:
            return False

    return True

def solution1(s):
    words_front = []
    if is_palindrome(s):
        return ''
    else:
        for i in range(0, len(s) // 2):
            words_front.append(s[i])
        answer = ''.join(words_front + words_front[::-1])
    return answer


n = int(input())
t = []
p = []
dp = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)
for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])


def solution4(N, duration, cost):
    dp = [0] * (N + 1)

    def dynamic_programming():
        max_val = 0
        for i in range(N - 1, -1, -1):
            if duration[i] + i > N:
                dp[i] = dp[i + 1]
            else:
                dp[i] = max(dp[i + 1], cost[i] + dp[i + duration[i]])

        return max_val

    result = dynamic_programming()
    return result


print(dp[0])

s = 'abcdcba'
print(solution(s))

s = 'bannana'
print(solution(s))

s = 'wabe'
print(solution(s))


class Node:
    def __init__(self):
        self.alpha = {}
        self.count = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        temp = self.root

        for w in word:
            if temp.alpha.get(w):
                temp = temp.alpha[w]
            else:
                temp.alpha[w] = Node()
                temp = temp.alpha[w]
            temp.count += 1

    def search(self, que):
        cnt = 0
        if que == '':
            for val in self.root.alpha.values():
                cnt += val.count
            return cnt
        temp = self.root
        for w in que:
            if temp.alpha.get(w):
                temp = temp.alpha[w]
                cnt = temp.count
            else:
                return 0
        return cnt


def solution5(words, queries):
    t_a = [Trie() for i in range(10001)]
    r_a = [Trie() for i in range(10001)]

    # words => Tries
    for word in words:
        t_a[len(word)].insert(word)
        r_a[len(word)].insert(word[::-1])

    # Search => queries
    answer = [0 for _ in range(len(queries))]
    for idx, que in enumerate(queries):
        if que[0] != '?':  # queries => t_a
            s_que = que.split('?')[0]
            answer[idx] = t_a[len(que)].search(s_que)
        else:  # queries => r_a
            s_que = que.split('?')[-1]
            answer[idx] = r_a[len(que)].search(s_que[::-1])

    return answer


from itertools import permutations

weaks = []


def make_weaks(n, weak):
    cnt = 1
    weaks.append(weak)
    while cnt != len(weak):
        temp = []
        for i in range(cnt, len(weak)):
            temp.append(weak[i])
        for i in range(cnt):
            temp.append(weak[i] + n)
        weaks.append(temp)
        cnt += 1


def check(per):
    for weak in weaks:
        visited = [0 for _ in range(len(weak))]
        idx = 0
        for num in per:
            if visited[idx] == 0:
                visited[idx] = 1
                are = weak[idx] + num
                idx += 1
                for w in weak[idx:]:
                    if w <= are:
                        visited[idx] = 1
                        idx += 1
                    else:
                        break
        if 0 in visited:
            continue
        else:
            return 1


def build(cnt, dist):
    pers = permutations(dist, cnt)
    for per in pers:
        if check(per):
            return 1
    return 0


def solution6(n, weak, dist):
    make_weaks(n, weak)
    for cnt in range(1, len(dist) + 1):
        if build(cnt, dist):
            return cnt
    return -1


from itertools import permutations
import re

def solution9(expression):
    expressions = set(re.findall("\D", expression))
    prior = permutations(expressions)
    cand = []

    for op_cand in prior:
        temp = re.compile("(\D)").split('' + expression)
        for exp in op_cand:
            while exp in temp:
                idx = temp.index(exp)
                temp = temp[:idx-1] + [str(eval(''.join(temp[idx-1:idx+2])))] + temp[idx+2:]
        cand.append(abs(int(temp[0])))
    return max(cand)



from collections import deque, defaultdict

def solution10(gems):

    gem_set = set(gems)
    LEN = len(gem_set)
    get_set = set()
    get_dict = defaultdict(int)
    sidx, eidx = 1, 0
    que = deque(gems)
    get_que = deque([])
    cand = []
    min_len = 999999
    flag = False

    while que:
        item = que.popleft()
        get_que.append(item)
        get_set.add(item)
        get_dict[item] += 1
        eidx += 1
        while get_que and get_dict[get_que[0]] > 1:
            get_dict[get_que.popleft()] -= 1
            sidx += 1

        if flag or gem_set & get_set == gem_set:
            if min_len > eidx - sidx:
                cand = [sidx, eidx]
                min_len = eidx - sidx
                if min_len == LEN-1:
                    return cand
                if not flag:
                    flag = True
    return cand




dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def change(d, c):
    if (c == "L"):
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


def start():
    cnt = 0
    # 뱀 위치 표시
    x = 0
    y = 0
    arr[x][y] = 3
    d = 0
    idx = 0
    # 뱀의 꼬리 ~ 머리까지의 정보를 q에 담기
    q = []
    q.append((x, y))
    while (True):
        # 몇초에 방향 전환 하는지
        if (game[idx][0] == cnt):
            d = change(d, game[idx][1])
            idx += 1
        nx = x + dx[d]
        ny = y + dy[d]
        # 범위안에 있고, 자기자신이 아니라면
        if (0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 3):
            # 사과를 먹으면 꼬리는 그대로
            if (arr[nx][ny] == 1):
                arr[nx][ny] = 3
                q.append((nx, ny))
            # 사과를 못먹으면 꼬리 하나 떼기
            elif (arr[nx][ny] == 0):
                arr[nx][ny] = 3
                q.append((nx, ny))
                tx, ty = q.pop(0)
                arr[tx][ty] = 0
            x = nx
            y = ny
            cnt += 1
        else:
            cnt += 1
            break
    return cnt


n = int(input())
k = int(input())
arr = [[0] * n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1
l = int(input())
game = [[0, 0]] * 10000
for i in range(l):
    x, c = input().split()
    game[i] = [int(x), c]
res = start()
print(res)