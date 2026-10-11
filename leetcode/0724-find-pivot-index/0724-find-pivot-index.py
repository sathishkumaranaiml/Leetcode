class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=sum(nums)
        l=0
        r=0
        for i in range(len(nums)):
            r=s-l-nums[i]
            if(l==r):
                return i
            l+=nums[i]
        return -1