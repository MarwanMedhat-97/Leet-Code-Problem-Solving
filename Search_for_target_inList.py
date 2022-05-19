class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #nums.sort()
        low = 0
        high = len(nums)
        while low<high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            if nums[low]<=nums[mid]:                      # not sorted
                if target >=nums[low] and target <nums[mid]:
                    high = mid
                else:
                    low = mid+1
            else:
                if target<=nums[high-1] and target>nums[mid]:
                    low = mid+1
                else:
                    high = mid
        return -1
            
            
            
            # if ( target not in nums):
            # return -1
            
            # for i in range(len(nums)):
            #     if ( nums[i] == target):
            #         return i
        