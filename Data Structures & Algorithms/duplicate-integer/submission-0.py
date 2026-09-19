class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurances = set()
        for i in nums:
            if i in occurances:
                return True
            else:
                occurances.add(i)
        return False