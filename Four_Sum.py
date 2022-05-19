class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        x=list()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for l in range(k+1,len(nums)):
                        if (nums[i]+nums[j]+nums[k]+nums[l] == target ):
                            y = [nums[i],nums[j],nums[k],nums[l]]
                            y.sort()
                            if y in x :
                                break
                            x.append(y)
                        
                        
        return x
        