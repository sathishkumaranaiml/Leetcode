class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        if not nums:
            return res
        for i in range(len(nums)):
            if len(nums)%(i+1)==0:
                res+=nums[i]*nums[i]
        return res
    