## Remove Duplicates   

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.   

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.   

Return k after placing the final result in the first k slots of nums.   
    
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.    

```
class Solution {
    public int removeDuplicates(int[] nums) {
        int index = 1;
        for(int i = 0; i < nums.length - 1; i ++) {
            if(nums[i] != nums[i+1]) {
                nums[index++] = nums[i + 1];
            }
    
        }
        return index;
    }
}
```

**Code Explanation:**   

First, we declare an `index = 1` to differentiate between `i` in the for-loop when we loop through the array. By doing this, we can "continue" to check for the next values, whilst simultaneously update our next value in the array if we find the next element to be a different element. This will be useful when we want to look through the array if the first pointer and second pointer values are different. We loop through the array with `nums.length-1` so that we don't get an ArrayIndexOutofBounds error when we check the `i + 1` element later. The condition `nums[i] != nums[i + 1]` means that our value in the i-th position of the array is different from its neighbor. When this happens, we replace num at position index with the `i + 1` value.   

The code shown below shows what using `[index++]` inside the brackets for an array mean:   
```
// A:
nums[index++] = nums[i + 1];

// B:
nums[index] = nums[i + 1];
index++;
```   

As `i` increases, we will replace `num[index]` with the different, unique value. The final return will naturally be `index`, as it is the count of our index and also our number of unique values. The time complexity is O(n). The space complexity is O(1).    