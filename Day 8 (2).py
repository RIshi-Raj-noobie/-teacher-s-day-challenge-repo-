matrix = [list(map(int, input().split())) for _ in range(5)]
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row_moves = abs(i - 2)
            col_moves = abs(j - 2)
            print(row_moves + col_moves)
            exit()