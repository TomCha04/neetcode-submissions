class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        hashed_nums = {} # key-value = element-index
        for index in range(len(nums)):
            complement = target - nums[index] #Find the complement of the current element
            if complement in hashed_nums:
                output.append(index)
                output.append(hashed_nums.get(complement))
                output.sort()
                return output
            else:
                #Add the current nums' element-index pair to the dictionary
                hashed_nums[nums[index]] = index
        output.sort()
        return output