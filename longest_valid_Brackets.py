class Solution:
    def longestValidParentheses(self, s: str) -> int:
        Stack = []
        count = 0
        max_count = 0
        for c in s:
            if c == '(' :
                
                Stack.append(c)
                
            
                
            elif c == ')' and len(Stack) != 0 and Stack[-1] == '(':
                
                Stack.pop()
                count += 2
                if count > max_count :
                    max_count = count
                
            
       
            else:
                count = 0
            
        return max_count