### Longest Substring without Repitition   

Given a string s, find the length of the longest substring without repeating characters.   

```
class Solution {
    public int LengthOfLongestSubstring(String s) {
        int left = 0;
        int right = 0;
        int max = 0;

        HashSet<String> set = new HashSet<>();
        while(right < s.lenth()) {
            if(!set.contains(s.charAt(right))) {
                set.add(s.charAt(right));
                right++;
                max = Math.max(set.size(), max);
            } else {
                set.remove(s.charAt(left));
                left++;
            }
        }
        return max;
    }
}
```

### Explanation/Notes:    

One of the first things that we can see is that a Set should be nice to deal with repetitive characters. From there, we will take a "sliding window" approach. Starting from the beginnning, we will increment our "right side" if the set does not contain the character. If it does, then we will remove the left character in the set, and then increment our left pointer.    

One of the things to know here is that a sliding window appraoch works well in similar problems too.   

Time = O(n)
Space = O(n)