### Group Anagrams   

Given an array of strings strs, group the anagrams together. You can return the answer in any order.   

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.   


```
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List> map = new HashMap<>();
        for(int i = 0; i < strs.length; i++) {
            String word = strs[i];
            char[] charArray = word.toCharArray();
            Arrays.sort(charArray);
            String key = String.valueOf(charArray);
            if(!map.containsKey(key)) {
                map.put(key, new ArrayList());
            }
            map.get(key).add(word);
        }
        return new ArrayList(map.values());   
    }
}
```

### Code Explanation:   

One thing to recognize is that we can return the answer in any order. Also, when we sort each individual string, we can see if it is an anagram or not. So our validation step of whether or not a word is an anagram would be first - sort each character of each string alphabetically, and then check it through a dictionary. Our answer would be all the values of the dictionary, returned as a List of Lists. Pretty straightforward!   

Time: O(NKlogK)   
Space: O(NK)   

