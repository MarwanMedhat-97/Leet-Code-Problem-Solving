class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        x=re.search(p,s)
        if x == None:
            return False
        y=x.group()
        print(y)
        if y == s:
            return True
        else :
            return False