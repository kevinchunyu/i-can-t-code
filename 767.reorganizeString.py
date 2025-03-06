class Solution:
    def reorganizeString(self, s: str) -> str:
        # counter 
        s_freq = Counter(s) 

        # get max key 
        max_freq = max(s_freq, key = s_freq.get)
        max_count = max(s_freq.values())
        if max_count > (len(s) + 1) // 2:
            return ""
        string_array = [''] * len(s)

        # place the most frequent character first 
        idx = 0 
        while s_freq[max_freq] > 0:
            string_array[idx] = max_freq 
            idx += 2
            s_freq[max_freq] -= 1

        for char, count in s_freq.items(): 
            while count > 0: 
                # reset index
                if idx >= len(s): 
                    idx = 1 
                
                # place 
                string_array[idx] = char 
                idx += 2
                count -= 1 
                
        
        return "".join(string_array)
