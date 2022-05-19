class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums)
        mid = 0
        
        if target not in nums:
            if target < nums[0]:
                return 0
            elif target > nums[-1]:
                return len(nums)  
            
            for i in range(1,len(nums)):
                if(nums[i-1]<target and nums[i]>target):
                    return i
        
        while low<high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            
            if target >=nums[low] and target <nums[mid]:
                high = mid
            else:
                low = mid+1
            
        
        