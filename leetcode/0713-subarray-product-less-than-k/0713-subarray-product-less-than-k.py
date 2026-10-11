class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        res=0
        j=0
        p=1
        for i in range(len(nums)):
            p*=nums[i]
            while p>=k:
                p//=nums[j]
                j+=1
            res+=i-j+1
        return res

