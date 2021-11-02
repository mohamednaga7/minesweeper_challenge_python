import random


def create_board(num):
    arr = []
    for i in range(num):
        row = []
        for j in range(num):
            row.append(random.choice(('X', 'O')))
        arr.append(row)
    return arr


def print_board(arr):
    for row in arr:
        row_text = ''
        for col in row:
            row_text += f'{col} '
        print(row_text)
    print('===========')


def minesweeper(arr):
    for i in range(len(arr)):
        row_text = ''
        for j in range(len(arr[i])):
            if arr[i][j] == 'X':
                row_text += 'X '
                continue
            neighbors = [
                (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                (i, j - 1), (i, j + 1),
                (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
            ]
            count_bomb = 0
            for row, col in neighbors:
                if row != -1 and col != -1 and row < len(arr) and col < len(arr[row]) and arr[row][col] == 'X':
                    count_bomb += 1
            row_text += f'{count_bomb} '
        print(row_text)


length = input('please enter the length of the board: ')
board = create_board(int(length))
print_board(board)
minesweeper(board)
