class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_joined = ''.join(char for char in s if char.isalnum())
        processed_str = string_joined.lower()
        return processed_str == processed_str[::-1]