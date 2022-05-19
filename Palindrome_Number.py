class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        n=0
        l=list()
        if x <0 :
            return False
        while temp>0:
            n+=1
            l.append((temp%10))
            temp=temp//10
        for i in range (int(len(l)/2)):
            if (l[i]!=l[len(l)-i-1]):
                return False
        return True