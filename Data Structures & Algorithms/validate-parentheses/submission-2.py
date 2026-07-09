class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = []

        for i in range(len(s)):
            if s[i] in ['[', '{', '(']:
                stack.append(s[i])
            if s[i] in [']', '}', ')']:
                if s[i] == ']' and len(stack)>0 and stack[-1] == '[':
                    stack.pop()
                elif s[i] == ')' and len(stack)>0 and stack[-1] == '(':
                    stack.pop()
                elif s[i] == '}' and len(stack)>0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        
        return False