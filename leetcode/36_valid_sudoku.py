class Solution:
    # Time Complexity O(n^2)
    # Space Complexity O(n^2)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        uniqueRow = [set() for _ in range(9)]
        uniqueCol = [set() for _ in range(9)]
        uniqueSq = [set() for _ in range(9)]

        for r in range(N):
            for c in range(N):
                sudokuNum = board[r][c]
                
                if sudokuNum == ".":
                    continue

                if sudokuNum in uniqueCol[c]:
                    return False
                uniqueCol[c].add(sudokuNum)
                 
                if sudokuNum in uniqueRow[r]:
                    return False
                uniqueRow[r].add(sudokuNum)
                
                idx = (r // 3) * 3 + c // 3
                if sudokuNum in uniqueSq[idx]:
                    return False
                uniqueSq[idx].add(sudokuNum)  
                
        return True

    # Time Complexity O(n^2)
    # Space Complexity O(n)
    def isValidSudokuBitMasking(self, board: List[List[str]]) -> bool:
        N = 9
        # Use binary number to check previous occurrence
        rows = [0] * N
        cols = [0] * N
        boxes = [0] * N

        for r in range(N):
            for c in range(N):
                # Check if the position is filled with number
                if board[r][c] == ".":
                    continue

                pos = int(board[r][c]) - 1

                # Check the row
                if rows[r] & (1 << pos):
                    return False
                rows[r] |= (1 << pos)

                # Check the column
                if cols[c] & (1 << pos):
                    return False
                cols[c] |= (1 << pos)

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if boxes[idx] & (1 << pos):
                    return False
                boxes[idx] |= (1 << pos)

        return True
