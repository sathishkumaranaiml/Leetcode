class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        c=0
        m={0:-1}
        ps=0
        for i in range(len(nums)):
            ps+=nums[i]
            r=ps%k
            if r not in m:
                m[r]=i
            elif i-m[r]>1:
                return True
        return False

