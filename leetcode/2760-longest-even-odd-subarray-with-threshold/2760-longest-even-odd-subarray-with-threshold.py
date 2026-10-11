class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        l=0
        maxi=0
        for r in range(len(nums)):
            if nums[r]%2==0 and nums[r]<=threshold:
                l=r
                while r+1<len(nums) and nums[r]%2!=nums[r+1]%2 and nums[r+1]<=threshold:
                    r+=1
                maxi=max(maxi,r-l+1)
        return maxi
