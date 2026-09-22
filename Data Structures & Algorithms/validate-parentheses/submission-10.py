class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # store opening brackets on a STACK
        pairs = {')':'(', '}':'{', ']':'['} # approach can work without a hash map, but this is cleaner
        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
            # 3 CLOSING bracket cases to handle (first 2 result in invalid s)
            # 1) the stack is empty, i.e. no opening bracket to pair it with
            # 2) the stack is not empty, but its top element doesn't match the closing bracket, e.g. [)
            # 3) the stack is not empty, and its top element matches the closing bracket
            elif len(stack) == 0 or stack[-1] != pairs[bracket]:
                return False
            else: stack.pop()
        # if the stack is empty by the end, then all brackets were paired, so s is valid
        return len(stack) == 0

        