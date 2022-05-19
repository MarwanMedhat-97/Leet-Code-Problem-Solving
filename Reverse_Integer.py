class Solution:
    def reverse(self, x: int) -> int:
        val=0
        flag = 0
        if x < 0:
            flag =1
            x=abs(x)
        while x > 0:
            rem=x%10
            val=10*val+rem
            x=x//10
        if flag == 1:
            val=-1*val
        
        return val
            
        
        