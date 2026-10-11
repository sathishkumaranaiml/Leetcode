class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi=0
        i=0
        j=len(height)-1
        while(i<j):
            if height[i]<height[j]:
                maxi=max(maxi,height[i]*(j-i))
                i+=1
            elif height[i]>height[j]:
                maxi=max(maxi,height[j]*(j-i))
                j-=1
            else:
                maxi=max(maxi,height[j]*(j-i))
                j-=1
                i+=1
        return maxi



        