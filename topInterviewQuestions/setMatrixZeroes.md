### Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

### Explanation:   

The problem starts off with me thinking the relation between i and j of a matrix. We can start off thinking about the changes that happen if we "detect" a 0 when reading into the given list of arrays.   
So let `[i,j]` be the coordinates where we will navigate through the matrix.   

## Method 1:    
Using a HashSet:   
- The question explicity says that you should do it in-place. But it doesn't hurt to approach this problem in a less efficient way first.   

Hashset code:   
```
class Solution {
    public void setZeroes(int[][] matrix) {
        Set<Integer> cols = new HashSet<>();
        Set<Integer> rows = new HashSet<>();
        int R = matrix.length;
        int C = matrix[0].length;

        // go through matrix and find zeroes to mark the location
        for(int i = 0; i < R; i++) {
            for(int j = 0; j < C; j++) {
                if(matrix[i][j] == 0) {
                    rows.add(j);
                    cols.add(i);
                }
            }
        }

        // go through matrix again and set zeroes in new positions
        for(int i = 0; i < R; i++) {
            for(int j = 0; j < C; j++) {
                if(cols.contains(i) || rows.contains(j)) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
}
```

But this code has the following, such that m and n represents rows and columns:    
Time Complexity: O(m x n)   
Space Complexity: O(m + n)   

## Method 2:   
Using the in-place method:   
- We use `matrix[i][0]` and `matrix[0][j]` as our indicators on whether or not that whole column or row should be changed to zero or not.   
- Our first for-loop going through the matrix would be:   
    1. Marking whether or not the first column and row should be all zeroes or not.   
    2. Marking the headers that need to be 0.   
- Our second for-loop going through the matrix would start from `matrix[1][1]`. Why? Because we are going to use `matrix[i][0]` and `matrix[0][j]` as the condition to see if our `matrix[i][j]` should be zero.   
- Our third and fourth conditions would be converting the column and row to 0 if required.   

```
class Solution {
    public void setZeroes(int[][] matrix) {
        int R = matrix.length;
        int C = matrix[0].length;
        boolean isCol = false;
        for(int i = 0; i < R; i++) {
            if(matrix[i][0] == 0) {
                isCol = true;
            }
            for(int j = 1; j < C; j++) {
                if(matrix[i][j] == 0) {
                    // set the marker
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }
        
        for(int i = 1; i < R; i++) {
            for(int j = 1; j < C; j++) {
                //check for markers
                if(matrix[0][j] == 0 || matrix[i][0] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }
        
        // first row
        if(matrix[0][0] == 0) {
            for(int j = 0; j < C; j++) {
                matrix[0][j] = 0;
            }
        }
        
        
        // first col
        if(isCol) {
            for(int i = 0; i < R; i++) {
                matrix[i][0] = 0;
            }
        }
        
    }
}
```

Time (O)M X N   
Space: O(1)   