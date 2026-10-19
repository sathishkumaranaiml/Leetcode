class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        i=0
        sidx=-1
        for i in range(len(nums)):
            if nums[i]==target:
                sidx=i
                break
        while i<len(nums) and nums[i]==target:
            i+=1
        eidx=i
        return [i for i in range(sidx,eidx)] if sidx!=-1 else []

