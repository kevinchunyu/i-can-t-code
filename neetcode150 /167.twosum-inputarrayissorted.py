class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # regular two sum solution with slight modifications
            # complement_dict = {} 

            # for idx in range(len(numbers)): 
            #     complement = target - numbers[idx]
            #     if complement in complement_dict: 
            #         return [ complement_dict[complement] +  1, idx + 1]
                
            #     complement_dict[numbers[idx]] = idx

        #  with binary search: 
        for idx in range(len(numbers)): 
            find = target - numbers[idx]
            left = idx + 1 
            right = len(numbers) - 1 
            while left <= right:
                mid = left + (right - left) // 2  
                if numbers[mid] == find: 
                    return[idx + 1, mid + 1]
                elif numbers[mid] < find: 
                    left = mid + 1
                else:
                    right = mid - 1  

        return []

