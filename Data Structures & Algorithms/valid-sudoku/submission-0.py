class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def validRow():

            print("running validRow")

            for i in range(0,9):
                dups = set()
                for j in range(0,9):
                    if board[i][j] != "." and board[i][j] in dups:
                        return False
                    dups.add(board[i][j])

            return True

        def validCol():

            print("running validCol")

            for i in range(0,9):
                dups = set()
                for j in range(0,9):
                    if board[j][i] != "." and board[j][i] in dups:
                        return False
                    dups.add(board[j][i])

            return True

        def validBox():

            print("running validBox")

            # Loop through the top-left corner of each 3x3 sub-box
            for box_row in range(0, 9, 3):
                for box_col in range(0, 9, 3):
                    
                    dups = set()
                    
                    # Iterate through the 9 cells within this specific sub-box
                    for i in range(3):
                        for j in range(3):
                            val = board[box_row + i][box_col + j]
                            
                            # LeetCode standard uses "." for empty slots
                            if val != "." and val in dups:
                                    return False  # Duplicate found in this sub-box
                            dups.add(val)
            return True



        return validRow() and validCol() and validBox()