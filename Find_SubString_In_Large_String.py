class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if(len(needle) == 0):
            return 0
        
        if needle not in haystack :
            
            return -1
        
        n=len(needle)
        
        for i in range(0,len(haystack)):
            
            if (haystack[i:i+n] == needle):
                
                return i
        
        

        