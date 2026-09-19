class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # Create a sorted_word: list_of_anagrams hash map
        for word in strs:
            sorted_word = ''.join(sorted(word)) # build the key for the corresponding anagrams list
            result[sorted_word].append(word) # add the current word to the corresponding list
        return list(result.values()) # convert the values of result into an actual list of lists object


