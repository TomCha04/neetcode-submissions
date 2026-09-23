class Solution: # Attempt 2
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # key = sorted word, value = list of corresponding anagrams
        for word in strs:
            # strings are immutable and sorted() returns a new object in memory
            sorted_word = "".join(sorted(word))
            anagrams[sorted_word].append(word)
        return list(anagrams.values())