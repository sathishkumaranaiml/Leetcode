class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        l=0
        for i in range(len(nums)):
            r=s-l-nums[i]
            if r==l:
                return i
            l+=nums[i]
        return -1

        