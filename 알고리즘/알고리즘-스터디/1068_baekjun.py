N = int(input())

tree = list(map(int, input().split(' ')))
root = -1
delete_node = int(input())

child = []
leaf = []

for j in range(N):
    child.append([])
    leaf.append([])

for i in range(len(tree)):

    if tree[i] == -1:
        root = i
        continue

    child[tree[i]].append(i)


def dfs(x, par):
    if not child[x]:
        leaf[x] += 1

    for y in child[x]:
        if y == par:
            continue
        dfs(y, x)
        leaf[x] += leaf[y]


def pro():

    for k in range(N):
        if delete_node in child[k]:
            child[k].remove(child[k].index(delete_node))

    if root == delete_node:
        dfs(root, -1)

    print(leaf)

pro()