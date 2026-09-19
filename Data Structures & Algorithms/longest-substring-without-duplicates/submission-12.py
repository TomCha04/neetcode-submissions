class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_indeces = {} # char-(last seen position) pair
        running_max = 0
        l = 0 #left pointer
        for r in range(len(s)): # r = right pointer
            if s[r] in chars_indeces:
                # move the left pointer 1 position after the last seen occurance
                l = max(chars_indeces[s[r]] + 1, l)
            chars_indeces[s[r]] = r 
            running_max = max(running_max, r-l+1) # pick between running max or current window size
        return running_max