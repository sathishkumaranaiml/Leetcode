class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s=set()
        l=0
        maxi=0
        for i in range(len(nums)):
            while nums[i] in s:
                s.discard(nums[l])
                l+=1
            s.add(nums[i])
            maxi=max(sum(s),maxi)
        return maxi
            
            
