class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        closeToOpen = { "(" : ")", "[" : "]", "{" : "}" }

        for c in s:
            if c in closeToOpen:
                stack.append(c)
            
            elif not stack:
                return False

            else:
                if closeToOpen[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False

            
       
       
       
       
       
       
       
       
       
    #    for c in s: 
    #     if c in closeToOpen:  #c is the close bracket here
    #         if stack and stack[-1] == closeToOpen[c]: #stack[-1] is open bracket
    #             # if c == closeToOpen[stack[-1]]
    #             stack.pop()
    #         else:
    #             return False
    #     else:
    #          stack.append(c)
        
    #    return True if not stack else False
        



       


               