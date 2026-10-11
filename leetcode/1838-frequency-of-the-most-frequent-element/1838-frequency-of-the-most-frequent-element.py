class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        res=0
        l=0
        cur=frq=0
        for i in range(len(nums)):
            frq=nums[i]
            cur+=nums[i]
            while (i-l+1)*frq-cur>k:
                cur-=nums[l]
                l+=1
            res=max(res,i-l+1)
        return res
        
        
        