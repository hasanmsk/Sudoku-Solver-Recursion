sudoku = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]


def solve(sudoku):
    #Base case
    find = find_empty(sudoku)
    if not find:
        return True
    #Assign row and column
    else:
        row, col = find
    #Loop through possible numbers
    for i in range(1, 10):
        #Call is_valid function to detirmine if number is legal
        if is_valid(sudoku, i, (row, col)):
            #Assign number i to that index if legal
            sudoku[row][col] = i
            #Recursive call
            if solve(sudoku):
                return True

            sudoku[row][col] = 0

    return False

def is_valid(sudoku, num, pos):
    #checking if i is in the row
    for i in range(len(sudoku[0])):
        #If num is in the row, return False
        if sudoku[pos[0]][i] == num and pos[1] != i:
            return False
    #checking if i is in the column
    for i in range(len(sudoku)):
        #If num is in the column, return False
        if sudoku[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3
    #Check if i is in the 'box'
    for i in range(box_y *3, box_y *3 + 3):
        for j in range(box_x *3, box_x *3 + 3):
                #If num is in the box, return False 
            if sudoku[i][j] == num and (i, j) != pos:
                return False
    #Passes row, column, and box check, return True
    return True


def print_board(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print("-  -  -  -  -  -  -  -  -")

        for j in range(len(sudoku[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + " ", end="")


def find_empty(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i, j)
    return None

print_board(sudoku)

solve(sudoku)


print("""

________________________________________

""")

print_board(sudoku)
