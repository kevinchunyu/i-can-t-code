class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        # row col box 
        row = [set() for _ in range(N)]
        col = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        # iterate through the list 
        for r in range(N): 
            for c in range(N): 
                val = board[r][c]
                if val == '.': 
                    continue

                # if seen in row 
                if val in row[r]:  
                    return False 

                row[r].add(val)

                # if seen in col 
                if val in col[c]: 
                    return False 
                
                col[c].add(val)

                # check sub-boxes 
                box_idx = (r // 3) * 3 + c // 3
                if val in boxes[box_idx]:
                    return False 
                boxes[box_idx].add(val)
        
        return True