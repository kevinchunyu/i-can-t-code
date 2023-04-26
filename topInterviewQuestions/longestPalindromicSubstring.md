### Longest Palindromic Substring   

Given a string s, return the longest palindromic substring in s.   


``` 
class Solution {
    public String longestPalindrome(String s) {
        int start = 0;
        int end = 0;

        for(int i = 0; i < s.length(); i++) {
            int odd = expand(s, i, i);
            int even = expand(s, i, i+1);
            int len = Math.max(odd, even);

            if(len > end - start) {
                start = i - (len - 1)/2;
                end = i + len/2;
            }
        }
        return s.substring(start, end+1);
    }

    private int expand(String s, int left, int right) {
        while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }
}
```   

### Explanation:    

Personally, I think this problem is a good problem to know or reference when we are looking are similar problems. There are patterns and specific "tricks" to be able to figure out how to get a specific value. Initially, I would tackle the problem from a sliding window perspective. We should start looking for palindromes from "inside-out" and then expand from there. What this means is that we could look at an index, treat that index as the "center" of our search, and expand if the next neighboring characters are the same. We increase our search if it continues to satisfy the condition of a palindrome, and if not we make sure that we choose the max length. Once we have the max length, we know that we have two things: the length of the palindrome and the "center" point. We then just have to figure out how to update the start and end values using the length and our index of "center". The rest is pretty intuitive - although the code looks a little tedious at first!    


Time Complexity = O(n^2)   
Space Complexity = O(1)   