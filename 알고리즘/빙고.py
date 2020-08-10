def solution(board, nums):
    N = len(board)
    row_bingo_counts = [0] * N
    col_bingo_counts = [0] * N
    diagonal_bingo_counts = [0] * 2

    nums = set(nums)
    for i, row in enumerate(board):
        for j, number in enumerate(row):
            if number in nums:
                row_bingo_counts[i] += 1
                col_bingo_counts[j] += 1

                if i == j:
                    diagonal_bingo_counts[0] += 1
                if i + j == N - 1:
                    diagonal_bingo_counts[1] += 1

    return (row_bingo_counts + col_bingo_counts + diagonal_bingo_counts).count(N)

board = [[11,13,15,16],[12,1,4,3],[10,2,7,8],[5,14,6,9]]
nums = [14,3,2,4,13,1,16,11,5,15]
print(solution(board,nums))