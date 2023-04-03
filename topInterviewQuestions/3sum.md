## 3Sum   

Solution:   
``` 
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        // sort first:
        Arrays.sort(nums);
        for(int i = 0; i < nums.length - 2; i++) {
            int low = i + 1;
            int high = nums.length - 1;
            // two pointer approach
            // check conditions
            if(i == 0 || nums[i] != nums[i - 1]) {
                while(low < high) {
                    int sum = nums[i] + nums[low] + nums[high];

                    if(sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[low], nums[high]));
                    // skip duplicates
                        while(low < high && nums[low + 1] == nums[low]) {
                            low++;
                        }
                        while (low < high && nums[high - 1] == nums[high]) {
                            high--;
                        }
                        low++;
                        high--;
                    } else if (sum < 0) {
                        low++;
                    } else {
                        high--;
                    }
                }
            }
        }
        return result;
    }
}
```

### Code Explanation:

The main things to know before coding this problem was to understand that all the indexes cannot be duplicates. A good intuition to get is that once this happens, I can know that I can do a two pointer approach, and skip duplicates // or do something in the form of a HashSet.    

The solution does a two-pointer approach, where we take one number at index a, and then check b and c. In the for loop, we check if `a + b + c == 0`. If it is, then we add it to our result, after that we will check if there are duplicates - both for the high and low pointers. We index or decrement to symbolize the skipping part. If the sum is less than 0, we know we need a bigger number for b, hence `low++`, and vice versa for the high. 

Time: O(n^2)
Space: O(n)







