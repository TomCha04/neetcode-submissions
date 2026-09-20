class Solution: # Version 1: 2 for loops and 1 while loop
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        frequencies = defaultdict(int) # key = number, value = occurances
        
        for num in nums: 
            frequencies[num] += 1

        while k > 0:
            highest_freq = max(frequencies.values())
            for num in frequencies:
                if frequencies[num] == highest_freq:
                    result.append(num)
                    frequencies.pop(num)
                    break
            k -= 1
        return result
        