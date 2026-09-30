class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for string in strs:
            encoded_string += str(len(string)) + '|' + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0 # 1st index, start at the 1st char of a string's length
        while i < len(s):
            j = i # 2nd index, start at i
            while s[j] != '|':
                j +=1 # move index j by 1 until we get to the delimiter
            length = int(s[i:j]) # get the length of the encoded string
            i = j + 1 # move i to the 1st char of the encoded string
            j = i + length # move j to the 1st char of the length of the next encoded string
            decoded_list.append(s[i:j]) # get the decoded word and add it to the List
            i = j # move i to the 1st char of the length of the next encoded string 
        return decoded_list