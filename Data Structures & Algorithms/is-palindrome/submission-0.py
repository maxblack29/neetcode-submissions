import collections

class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join(char.lower() for char in s if char.isalnum())
        return self.helper(st, 0, len(st)-1)
                    
    def helper(self, s: str, left: int, right: int) -> bool:
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return self.helper(s, left+1, right-1)
