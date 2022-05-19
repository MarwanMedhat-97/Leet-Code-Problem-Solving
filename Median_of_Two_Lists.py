class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
       # print(int(len(nums)-1)/2)
        if(len(nums)%2 == 0):
            print(nums[1:2])
            print(nums[int(((len(nums)/2)-1)):int(len(nums)/2)+1])
            median = sum(nums[int(((len(nums)/2)-1)):int(len(nums)/2)+1])/2
        else:
            median = nums[int((len(nums)-1)/2)]
        
        return median
        