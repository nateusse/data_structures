class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]


         
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue

                # Check row
                if val in rows[i]:
                    return False
                rows[i].add(val)

                # Check column
                if val in cols[j]:
                    return False
                cols[j].add(val)

                # Check box
                box_index = (i // 3) * 3 + j // 3
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)

        return True

"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize an empty list to store seen elements in rows, columns, and subgrids.
        r = []

        # Iterate through the Sudoku board.
        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                # Check if the element is not '.' (empty cell).
                if ele != '.':
                    # Check for violations in the current row, column, and subgrid.
                    r += [(i, ele), (ele, j), (i // 3, j // 3, ele)]

        # Return True if there are no violations, i.e., the length of the list is equal to the length of the set.
        return len(r) == len(set(r))

"""

print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])) # true
print(Solution().isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])) # false