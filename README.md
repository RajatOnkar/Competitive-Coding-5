# Competitive-Coding-5

## Problem 1 - Greatest value in each row of the tree
# Initialize a queue and append the root to start with. 
# Take the size of the queue and iterate over it as that would be the elements at each level.
# Iterate over elements for each size queue and find the maximum value
# Append the values in the result array and return

## Problem 2 - Valid Sudoku
# Create a function to validate row, we continue for '.' and if a value exists we check if it is < 1 or
# > 9 (bounds check) or if the value exists in the Hashset (check duplicates)
# If value is not in Hashmap then we will increment that index by '1'
# Create a similar function to validate columns & validate block of 3x3 with the same conditions
# Once all these validations are complete we return True, else False