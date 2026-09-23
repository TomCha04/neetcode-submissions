class Solution: # Attempt 2
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        indices = {} # key = number, value = index
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in indices:
                result.append(i)
                result.append(indices[complement])
                result.sort()
                return result
            else:
                indices[nums[i]] = i
        return result