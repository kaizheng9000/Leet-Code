
example1 = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

example2 = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]


def isValidSudoku(board):

    # For Rows
    for i in range(9):
        s = set()
        for j in range(9):
            num = board[i][j]
            if num in s:
                return False
            elif num != ".":
                s.add(num)

    # For Columns
    for i in range(9):
        s = set()
        for j in range(9):
            num = board[j][i]
            if num in s:
                return False
            elif num != ".":
                s.add(num)

    # For boxes
    left_corners = [(0, 0), (0, 3), (0, 6),
                    (3, 0), (3, 3), (3, 6),
                    (6, 0), (6, 3), (6, 6)]

    for i, j in left_corners:
        s = set()
        for row in range(i, i + 3):
            for col in range(j, j + 3):
                num = board[row][col]
                if num in s:
                    return False
                elif num != ".":
                    s.add(num)

    return True


print(isValidSudoku(example1))
print(isValidSudoku(example2))