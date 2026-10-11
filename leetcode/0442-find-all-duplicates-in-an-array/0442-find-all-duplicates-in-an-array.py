class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)):
            idx=abs(nums[i])-1
            if nums[idx]<0:
                res.append(idx+1)
            else:
                nums[idx]*=-1
        return res