class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d={}
        for i in range(len(board)):
            h=set()
            h2=set()
            for j in range(len(board[0])):
                if(board[i][j] in h and board[i][j]!="."):
                        print(1)
                        return False
                else:
                    if(board[i][j]!="."):
                            h.add(board[i][j])
                if(board[j][i] in h2 and board[j][i]!="."):
                    print(board[j][i])
                    return False
                else:
                    if(board[j][i]!="."):
                        h2.add(board[j][i]) 
                if((i//3,j//3) in d):
                    if(board[i][j] in d[(i//3,j//3)] and board[i][j]!="."):
                        print(board[i][j])
                        return False

                    else:
                        if(board[i][j]!="."):
                            d[(i//3,j//3)].append(board[i][j])
                else:
                    if(board[i][j]!="."):
                        d[(i//3,j//3)]=[board[i][j]]       
        return True                            

        