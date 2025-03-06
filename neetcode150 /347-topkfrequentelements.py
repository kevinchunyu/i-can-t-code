def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    # counter frequency 
    freq_list = {} 
    for num in nums: 
        if num not in freq_list: 
            freq_list[num] = 0
        freq_list[num] += 1 

    sorted_list = [[] for _ in range(len(nums) + 1)]
    for key,value in freq_list.items():
        # make list to deal with same frequency
        sorted_list[value].append(key)

    # iterate through list of list to get k elemetn 
    result = []
    for idx in range(len(sorted_list)- 1, 0, -1):
        list_item = sorted_list[idx]
        # if not empty
        if list_item: 
            for item in list_item: 
                result.append(item)
                if len(result) == k: 
                    return result 

    # top k elements 
    return result

# bucket sort approach - >  O(nlogn?)