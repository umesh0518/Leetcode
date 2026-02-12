class Solution:
    def isValid(self, s: str) -> bool:

        bracketPair = {']':'[', '}':'{', ')':'('}
        stack = []


        for c in s:
            if c in bracketPair.values():
                stack.append(c)
            elif c in bracketPair.keys():
                #when you see closing bracket checks its correspoiding open and see the stack pop 
                # is equal or not
                if not stack or bracketPair[c] != stack.pop():
                    return False
        return not stack
                
        