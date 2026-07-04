class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        h=collections.defaultdict(set)
        c=collections.defaultdict(set)
        r=collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if(board[i][j]=="."):
                    continue
                if((board[i][j] in h[(i//3,j//3)]) or (board[i][j] in r[i]) or(board[i][j] in c[j])):
                    return False
                h[i//3,j//3].add(board[i][j])
                c[j].add(board[i][j])
                r[i].add(board[i][j])
        return  True            
        