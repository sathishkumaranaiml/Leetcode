class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total=sum(nums)
        target=total%p
        if target==0:
            return 0
        m={0:-1}
        mini=len(nums)
        ps=0
        for i,j in enumerate(nums):
            ps=(ps+j)%p
            need=(ps-target)%p
            if need in m:
                mini=min(mini,i-m[need])
            m[ps]=i
        return mini if mini!=len(nums) else -1

        