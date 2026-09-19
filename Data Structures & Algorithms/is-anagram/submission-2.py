class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # (variable 1, variable 2) = (value 1, value 2)
        count_s, count_t = {}, {}

        # iterate over indexes for a single pass
        for i in range(len(s)):
            # update the character count by 1 on both dicts
            # count_x.get(char, 0) = count of char in x (0 if not seen yet)
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        
        # comparison already returns boolean, so no need for if-else blocks
        return count_s == count_t