class Solution:
    def isValid(self, s: str) -> bool:
        
        Stack = []
    
        for c in s:
            if c in ['(', '{', '[']:
                
                Stack.append(c)
                
            elif c == ')' and len(Stack) != 0 and Stack[-1] == '(':
                
                Stack.pop()
                
            elif c == '}' and len(Stack) != 0 and Stack[-1] == '{':
                
                Stack.pop()
            
            elif c == ']' and len(Stack) != 0 and Stack[-1] == '[':
                
                Stack.pop()
       
            else:
                return False
            
        if (len(Stack) == 0):
            return True