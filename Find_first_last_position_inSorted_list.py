class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        
        if ( target not in nums):
            return [-1,-1]
        x = []   
        for i in range(len(nums)):
            
            if ( nums[i] == target):
               
                x.append(i)
        return [x[0],x[-1]]
        
        
        
#         if ( target not in nums):
#              return [-1,-1]
        
#         x = []
#         #if(target == nums[0]):
#            # x.append(0)
            
#         low = 0
#         high = len(nums)
#         while low<high:
#             mid = (low + (high-low)//2)
#             if nums[mid] == target:
#                 x.append(mid)
#             if nums[low]<=nums[mid]:
#                 if target >=nums[low] and target <nums[mid]:
#                     high = mid
#                 else:
#                     low = mid+1
#             else:
#                 if target<=nums[high-1] and target>nums[mid]:
#                     low = mid+1
#                 else:
#                     high = mid
            
#         return [x[0],x[-1]]
        