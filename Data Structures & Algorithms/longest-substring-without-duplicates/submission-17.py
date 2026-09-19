class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indices = {} # key = letter, value = last seen index of letter
        largest_size = 0
        l = 0 # left pointer

        for r in range(len(s)): # r = right pointer
            if s[r] in indices:
                # move the left pointer to the position right after the duplicate
                # max() prevents l from moving backward
                l = max(l, indices[s[r]] + 1)
            indices[s[r]] = r
            # +1 accounts for 0-based indexing
            largest_size = max(largest_size, r-l+1)
        return largest_size