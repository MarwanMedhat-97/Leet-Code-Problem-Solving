from itertools import permutations

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        result = []
        for perm in permutations(words):
            
            chained_string = ''.join(perm)
            
        
            n=len(chained_string)
            
            if n > len(s):
                break
        
            for i in range(0,len(s)):
            
                if (s[i:i+n] == chained_string):
                    if i not in result:
                        result.append(i)
                
        return result
        
           
            