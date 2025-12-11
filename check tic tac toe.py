board = [
    ["X", "X", "X"],
    ["O", "-", "O"],
    ["-", "-", "-"]
]

def check(board):
    for row in board:
        if row.count(row[0]) == 3:
            return row[0]
    return "No winner"

print(check(board))
