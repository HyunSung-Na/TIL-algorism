def solution(board):
    n = len(board)
    dp = []
    columns = set()
    dfs(n, 0, columns, dp, board)
    answer = max(dp)
    return answer


def dfs(n, row, columns, dp, board):
    if row == n:
        return 0
    cnt = 0
    for col in range(n):
        if col in columns:
            continue
        columns.add(col)
        cnt = board[row][col]
        cnt += dfs(n, row + 1, columns, dp, board)
        if cnt != board[row][col] and cnt not in dp:
            dp.append(cnt)
        columns.remove(col)
    return cnt

board = [[1, 0, 0, 0, 0], [0, 2, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
print(solution(board))