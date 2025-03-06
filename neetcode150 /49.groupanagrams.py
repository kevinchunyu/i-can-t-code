class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup_dict = {} 
        for s in strs: 
            sorted_list = sorted(s)
            sorted_s = "".join(sorted_list)
            if sorted_s not in lookup_dict: 
                lookup_dict[sorted_s] = []
            
            lookup_dict[sorted_s].append(s)

        return list(lookup_dict.values())
    
# 1. make dictionary
# 2. check if sorted strs[i] is in dict
#       if not then create new entry
#       otherwise, add strs[i] to key (sorted string)
# 3. return list of list of dict.values()