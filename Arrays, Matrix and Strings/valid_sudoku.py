'''
Given a sudoku in 2D Matrix, check if it is valid or not.
'''
class Solution:
    def isValidSudoku(self, board):
        for i in range(9):
            dic={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'.':0}
            for j in range(9):
                dic[board[i][j]]+=1
                if dic[board[i][j]]>1 and board[i][j]!='.':
                    return False
        for j in range(9):
            dic={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'.':0}
            for i in range(9):
                dic[board[i][j]]+=1
                if dic[board[i][j]]>1 and board[i][j]!='.':
                    return False
        for i in [1,4,7]:
            for j in [1,4,7]:
                dic={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'.':0}
                dic[board[i-1][j-1]]+=1
                dic[board[i][j-1]]+=1
                dic[board[i+1][j-1]]+=1
                dic[board[i-1][j]]+=1
                dic[board[i][j]]+=1
                dic[board[i+1][j]]+=1
                dic[board[i-1][j+1]]+=1
                dic[board[i][j+1]]+=1
                dic[board[i+1][j+1]]+=1
                for k,v in dic.items():
                    if v>1 and k!='.':
                        return False
        return True
sudoku = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
s = Solution()
print(s.isValidSudoku(sudoku))