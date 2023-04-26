### Increasing Triplet Subsequence    

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.   

``` 
class Solution {
    public boolean increasingTriplet(int[] nums) {
        int first = Integer.MAX_VALUE;
        int second = Integer.MAX_VALUE;
        for(int n : nums) {
            if(n <= first) {
                first = n;
            } else if (n <= second) {
                second = n;
            } else {
                return true;
            }
        }
        return false;
    }
}
```

### Explanation:   

This is a really, really fun problem. Simple, but really hard to notice. At first glance, I wanted to use a Stack and use the peek method to repeatedly check, and then add. Return if the size is greater or equal to 3. However, we can just use two "values" to keep track of two minimums. The first minimum is always looked at first. If it is a new minimum, we know that the next numbers being looked at will have to be greater than `first`, and won't satisfy our first if-statement. The second time we do it will keep track of the second minimum with the same intention. Once we reach the end, then we know that it will be true; otherwise the whole input will return false.   

Time Complexity: O(n)   
Space Complexity: O(1)    