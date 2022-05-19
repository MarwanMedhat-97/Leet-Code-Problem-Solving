class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = list()
        n=len(height)
        if(n>10000):
            return 0
        for i in range(len(height)):
            for j in range(i,len(height)):
                x = j-i
                min_H = min(height[i],height[j])
                area.append(x*min_H)
        
        max_area = max(area)
        return max_area
        