### Count and Say   

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:    
 
countAndSay(1) = "1"   
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.   
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit.    
Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.    

```
class Solution {
    public String countAndSay(int n) {
        if(n == 1) {
            return "1";
        }
        String prevSeq = countAndSay(n - 1);
        int count = 1;
        char currentDigit = prevSeq.charAt(0);
        StringBuilder output = new StringBuilder();
        for(int i = 1; i < prevSeq.length(); i++) {
            if(prevSeq.charAt(i) == currentDigit) {
                count++;
            } else {
                output.append(count).append(currentDigit);
                count = 1;
                currentDigit = prevSeq.charAt(i);
            }
        }
        output.append(count).append(currentDigit);
        return output.toString();
    }
}

```

### Explanation:    

The description for this problem is pretty confusing at first. I could not really wrap my head around the idea of "speaking" and the numbers not really making sense with `n`. This problem though, heavily relies on past output, which makes me think if DP is better or really just recursion should be ok. The solution for this problem uses recursion, and is better to understand for me.     

First, I create a string variable that stores `countAndSay(n-1)`. This allows me to start from `countAndSay(1)` and build from there. We continue to build our string/output as we look at each previous string that is outputted for each `n`. So `countAndSay(2)`, `countAndSay(3)`, ... and so on. Using that, we can iterate through the index, compare current and the next one. If the character is the same, than means we will increase our count. The `count` variable is the variable that decides how many consecutive appearances a character has in that string. If it is different, then we update the output (stringbuilder), and then reset the counts and the currentDigit that we are tracking.   

Overall sounds really confusing, but as I went through the code step-by-step, it was rather refreshing and not that difficult to figure out!    


Time & Space Complexity: O(2^n)   