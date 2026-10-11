class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        z=0
        maxilen=0
        for i in range(len(nums)):
            if nums[i]==0:
                z+=1
            while z>1:
                if nums[l]==0:
                    z-=1
                l+=1
            maxilen=max(maxilen,i-l)
        return maxilen
