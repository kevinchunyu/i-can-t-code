class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall = r_wall = 0 
        n = len(height) 
        l = [0] * n 
        r = [0] * n 

        for i in range(n): 
            j = - i - 1 
            # populate each array 
            l[i] = l_wall 
            r[j] = r_wall 
            # update
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])

        # find answer 
        ans = 0 
        for i in range(n): 
            ans += max(0, min(l[i], r[i]) - height[i])

        return ans
        

# intuition 
# craft L and R of max height of looking left and looking right 
# using L and R, use the min and minus the height of that 
# add to sum 