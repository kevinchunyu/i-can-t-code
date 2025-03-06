class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # make set to get ride of duplicates
        nums_set = set(nums)
        max_count = 0
        for num in nums_set: 
            # this if condition is crucial (the differentiator for passing TLE)
            if num - 1 not in nums_set:
                count = 1 
                next_val = num + 1 

                while next_val in nums_set: 
                    count += 1 
                    next_val += 1
                
                # update max count 
                if count > max_count: 
                    max_count = count 
        
        return max_count
