class Solution:


        

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        sub = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in row[i]  and  board[i][j] not in col[j] and board[i][j] not in (sub[(i // 3) * 3 + (j // 3)]):
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    sub[(i // 3) * 3 + (j // 3)].add(board[i][j])        
                else:
                    return False
        
        return True