class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "}" : "{", "]" : "["}

        for i in s:
            # if opening bracket
            if i in closeToOpen:
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()
            # if closing bracket
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

        # for i in range(len(s)):
        #     # if opening bracket
        #     if s[i] == "[" or s[i] == "{" or s[i] == "(":
        #         # push to stack 
        #         stack.append(s[i])
        #     # if closing bracket
        #     if s[i] == "]" or s[i] == "}" or s[i] == ")":
        #         # check stack is not empty
        #         if len(stack) == 0:
        #             return False
        #         #check top matches correct opening 
        #         if s[i] == "]" and stack[-1] == "[":
        #             stack.pop()
        #         elif s[i] == ")" and stack[-1] == "(":
        #             stack.pop()
        #         elif s[i] == "}" and stack[-1] == "{":
        #             stack.pop()
        #         else:
        #             return False
                
        # if len(stack) == 0:
        #     return True
        # else:
        #     return False
        
        