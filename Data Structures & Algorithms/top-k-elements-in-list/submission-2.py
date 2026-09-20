class Solution: # Version 2 (with explanation)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        frequencies = defaultdict(int) # track each num's frequency in nums
        counts = [[]for i in range(len(nums)+1)] # index = frequency, value = list of nums with that frequency

        for num in nums: # populate frequencies
            frequencies[num] += 1
        
        for num,freq in frequencies.items(): # populate counts
            counts[freq].append(num)
        
        for i in reversed(counts):
            for j in i:
                result.append(j)
            if len(result) == k:
                return result