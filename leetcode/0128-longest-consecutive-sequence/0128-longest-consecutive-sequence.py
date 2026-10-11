class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=1
        lsm=float("-inf")
        nums.sort()
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i]-1 ==lsm:
                c+=1
                lsm=nums[i]
            elif nums[i]!=lsm:
                c=1
                lsm=nums[i]
            l=max(l,c)
        return l