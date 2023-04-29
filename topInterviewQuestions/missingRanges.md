### Missing Ranges   
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.   

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.   

Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.  

```
class Solution {
    public List<List<Integer>> findMissingRanges(int[] nums, int lower, int upper) {
        List<List<Integer>> result = new ArrayList<>();
        
        // top bound
        if(nums.length == 0) {
            result.add(Arrays.asList(lower, upper));
            return result; 
        }

        if(nums[0] > lower) {
            result.add(Arrays.asList(lower, nums[0] - 1));
        }
        
        for(int i = 0; i < nums.length - 1; i++) {
            int pointerA = nums[i];
            int pointerB = nums[i + 1];
            
            if(pointerB - pointerA > 1) {
                result.add(Arrays.asList(pointerA + 1, pointerB - 1));
            }
        }
        
        // check end
        if(upper - nums[nums.length - 1] != 0) {
            result.add(Arrays.asList(nums[nums.length - 1] + 1, upper));
        }
        return result;
    }
}
```

### Explanation:   

I started out with keeping in mind the output form - a list of lists. The thought process was that I should use a for-loop and look at each integer on each index, and keep track of both `i` and `i + 1`. In this way, I am able to know if the two numbers at a given index are next to each other, or have a gap in between (check for `pointer b - pointer a`). If the difference is more than 1, then we put that into our `result` (list of list), as saying that there is a range that exists in between these two integers. After that, the code would still not be correct because there is two "opnenings" or "cases" of the problem still. We need to deal with both the beginning and the end of the array. What if the first index is a number that is larger than the lower range? We would also have to include the range that goes up to the integer that exists at the first index. The same goes for the last index. What if the last index is smaller than upper? That means that between the last index and upper, we also need to include that list that contains the missing values.   

Space Complexity: O(1) - if we don't count the output (since we are constructing a list of list, but our method uses O(1) space)    
Time Complexity: O(n)   