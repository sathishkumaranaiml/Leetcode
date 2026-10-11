class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max1,max2=-1,-1
        for i in range(len(nums)):
            nums[i]=abs(nums[i])
            if nums[i]>max1:
                max2=max1
                max1=nums[i]
            elif nums[i]>max2:
                max2=nums[i]
        return max2*max1*10**5