class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res=float("inf")
        for i in range(l,r+1):
            sw=sum(nums[:i])
            l1=0
            if sw>0:
                res=min(res,sw)
            for r1 in range(i,len(nums)):
                sw=sw-nums[l1]+nums[r1]
                if sw>0:
                    res=min(res,sw)
                l1+=1
        return res if res != float("inf") else -1
























        