class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        window = set() # track duplicates
        pl = 0 
        max_length = 0 # tracker for longest length

        for pr in range(len(s)):
            while s[pr] in window:
                window.remove(s[pl])
                pl += 1
            window.add(s[pr])
            max_length = max(max_length, pr-pl+1)

        return max_length