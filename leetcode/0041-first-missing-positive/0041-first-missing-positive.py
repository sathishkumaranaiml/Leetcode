class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        while i<len(nums):
            cidx=nums[i]-1
            if 0<nums[i]<=n and nums[i]!=nums[cidx]:
                nums[i],nums[cidx]=nums[cidx],nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return n+1
