class Solution:
    def removeDuplicates(self, nums: List[int]):
        
        res = []
        for i in nums:
            if i not in res:
                res.append(i)
        print(res)
        nums = res
        return len(res)
        
        # ANOTHER SOLUTION :
        
        #x=list(dict.fromkeys(nums))
        #y=len(x)
        #return y
        
                
                
        