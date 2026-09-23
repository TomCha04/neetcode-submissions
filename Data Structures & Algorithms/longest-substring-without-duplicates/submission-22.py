class Solution: # Attempt 2
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        l = 0 # left pointer
        seen_chars = {} # key = letter, value = index
        for r in range(len(s)): # r = right pointer
            if s[r] in seen_chars:
                # move l one position after the 1st occurance; max() prevents l from staling/moving back
                l = max(l, seen_chars[s[r]]+1)
            seen_chars[s[r]] = r
            result = max(result, r-l+1) # +1 to account for 0-based indexing
        return result