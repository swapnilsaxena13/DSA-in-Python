"""Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solvePartialSudoku(0, 0, board)
        return board
        
    def solvePartialSudoku(self, row, col, board):
        currentRow = row
        currentColumn = col

        if currentColumn == len(board[row]):
            currentRow += 1
            currentColumn = 0
            if currentRow == len(board):
                return True
        
        if board[currentRow][currentColumn] == ".":
            return self.tryDigitsAtPosition(currentRow, currentColumn, board)

        return self.solvePartialSudoku(currentRow, currentColumn + 1, board)

    def tryDigitsAtPosition(self, row, column, board):
        for digit in range(1, 10):
            if self.isvalidAtPosition(str(digit), row, column, board):
                board[row][column] = str(digit)
                if self.solvePartialSudoku(row, column + 1, board):
                    return True

        board[row][column] = "."
        return False

    def isvalidAtPosition(self, value, row, column, board):
        rowIsValid = value not in board[row]
        columnIsValid = value not in [r[column] for r in board]

        if not rowIsValid or not columnIsValid:
            return False
        
        subgridRowStart = (row // 3) * 3
        subgridColumnStart = (column // 3) * 3

        for rowidx in range(3):
            for columnidx in range(3):
                rowToCheck = subgridRowStart + rowidx
                colToCheck = subgridColumnStart + columnidx
                existingValue = board[rowToCheck][colToCheck]

                if existingValue == value:
                    return False
        return True
