class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        j=0
        for i in range(len(nums)):
            if j<k or nums[j-k]!=nums[i]:
                nums[j]=nums[i]
                j+=1
        return nums[:j]



