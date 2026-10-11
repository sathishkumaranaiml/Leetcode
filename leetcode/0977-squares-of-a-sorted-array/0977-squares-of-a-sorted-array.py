class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=0
        r=n-1
        res=[0]*n
        for i in range(n-1,-1,-1):
            if(nums[l]**2<nums[r]**2):
                res[i]=nums[r]**2
                r-=1
            else:
                res[i]=nums[l]**2
                l+=1

        return res
            


       

        