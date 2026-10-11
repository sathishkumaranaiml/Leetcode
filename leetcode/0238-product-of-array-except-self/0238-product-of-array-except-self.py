class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        arr=[1]*n
        pre=1
        for i in range(n):
            arr[i]=pre
            pre*=nums[i]
        suf=1
        for i in range(n-1,-1,-1):
            arr[i]*=suf
            suf=suf*nums[i]
        return arr


        