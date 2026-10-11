class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        while i<n:
            cidx=nums[i]-1
            if i<n and nums[i]!=nums[cidx]:
                nums[i],nums[cidx]=nums[cidx],nums[i]
            else:
                i+=1
        for i in range(n):
            if nums[i]!=i+1:
                return nums[i]