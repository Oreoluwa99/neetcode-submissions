class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {'}':'{', ']':'[', ')':'('}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

# In the worst case, the stack list could store every variables in the
# s array. 
# Example: s = "((((((((("
# Since no closing bracktes yet, 
# the stack can keep growing like: stack = ["(", "(", "(", ...]
