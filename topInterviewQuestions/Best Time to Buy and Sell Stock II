## Best Time to Buy and Sell Stock II   

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.   

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.   

Find and return the maximum profit you can achieve.   

```
class Solution {
    public int maxProfit(int[] prices) {
        // Start from day 1, check the neighboring day
        // if day[i + 1] - day[i] is positive and greater than max, then add to profit
        // return profit
        int profit = 0;
        for(int i = 0; i < prices.length - 1; i ++) {
            // positive profit
            int difference = prices[i+1] - prices[i];
            if(difference > 0) {
                // if profit is greater than 0
                profit +=  difference ;
            
            }
        }
        return profit;
    }
}
```   

**Code Explanation:**   
s
### I. Understanding the Problem   
  On first intuition, the problem seems to be a little complicated. We are trying to find the best strategy in a given array, and buying and selling stock. This allows the problem to potentially lead us to thinking about something that can get way too overcomplicated. Cleaning out all the noise, it can be generally identified, that this question is simply asking only for the positive profit. Since we do not really need to know the negative profits (ex: if price of day 2 - price of day 1 is negative), we can simply disregard that.   
### II. Code explanation    
   Since we know that the method needs to return an `int`, we will declare a variable `int profit = 0` to be returned later. We also know that we need two "pointers" (`[i] and [i+1]`), thus we will create a for-loop with `i < prices.length - 1`. Then we calculate the difference between day2 and day1. In this scenario, we wouldn't even need to create a max tracker (the question is not asking us to develop a strategy), as we are only interested in the positive profit. If the difference is greater than 0, then we will add that to our overall profit. Once we go through our whole array, then we have our total profit, and hence `return profit`.   

### III. Time and Space Complexity   
  The time and space complexity of this is `O(n)` for time complexity, and `O(n)` for space. The reason of this is that since we are going through the whole array, the space and time complexity is dependent on the `n` array size.