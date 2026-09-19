class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indices = {} # key = letter, value = last seen index of letter
        largest_size = 0
        left_p = 0 

        for right_p in range(len(s)): # left and right pointers start at index 0
            if s[right_p] in indices:
                left_p = max(left_p, indices[s[right_p]] + 1)
                indices[s[right_p]] = right_p
                largest_size = max(largest_size, right_p - left_p + 1)
            indices[s[right_p]] = right_p
            largest_size = max(largest_size, right_p - left_p + 1)
        return largest_size