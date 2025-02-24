'''
// Time Complexity :
Problem 1: O(n)   no. of elements in the tree (BFS)
Problem 2: O(m*n) for parsing the entire matrix (we do it 3 times for validations)
// Space Complexity :
Problem 1: O(n) amortized - if only one side of the tree has elements, we will parse all those elements
Problem 2: O(1) as we lookup the hashmap
// Did this code successfully run on Leetcode :
# Yes, the code ran successfully.
// Any problem you faced while coding this :

// Your code here along with comments explaining your approach
'''
## Problem 1 - Greatest value in each row of the tree
# Initialize a queue and append the root to start with. 
# Take the size of the queue and iterate over it as that would be the elements at each level.
# Iterate over elements for each size queue and find the maximum value
# Append the values in the result array and return

from collections import deque
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        if root == None: return result
        queue = deque([root])

        while(len(queue) > 0):
            size = len(queue)
            max_val = float('-inf')
            for i in range(size):
                node = queue.popleft() #1
                max_val = max(node.val, max_val) #1 vs -inf
                if node.left is not None:
                    queue.append(node.left) #3
                if node.right is not None:
                    queue.append(node.right) #2
            result.append(max_val)
        return result
    
## Problem 2 - Valid Sudoku
# Create a function to validate row, we continue for '.' and if a value exists we check if it is < 1 or
# > 9 (bounds check) or if the value exists in the Hashmap (check duplicates)
# If value is not in Hashmap then we will increment that index by '1'
# Create a similar function to validate columns & validate block of 3x3 with the same conditions
# Once all these validations are complete we return True, else False

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        for i in range(0, m, 3):
            for j in range(0, n, 3):
                if not self.validBlock(i, j, board):
                    return False

        for i in range(m):
            if not self.validRow(i, board):
                return False
        
        for j in range(n):
            if not self.validCol(j, board):
                return False
        return True
            
    def validRow(self, r, board):
        dictnums = {}
        for c in range(9):
            if board[r][c] == '.':
                continue
            elif int(board[r][c]) < 1 or int(board[r][c]) > 9 or board[r][c] in dictnums:
                return False
            else:
                dictnums[board[r][c]] = 1
        return True
    
    def validCol(self, c, board):
        dictnums = {}
        for r in range(9):
            if board[r][c] == '.':
                continue
            elif int(board[r][c]) < 1 or int(board[r][c]) > 9 or board[r][c] in dictnums:
                return False
            else:
                dictnums[board[r][c]] = 1
        return True
    
    def validBlock(self, r, c, board):
        dictnums = {}
        for i in range(r, r+3):
            for j in range(c, c+3):
                if board[i][j] == '.':
                    continue
                elif int(board[i][j]) < 1 or int(board[i][j]) > 9 or board[i][j] in dictnums:
                    return False
                else:
                    dictnums[board[i][j]] = 1
        return True