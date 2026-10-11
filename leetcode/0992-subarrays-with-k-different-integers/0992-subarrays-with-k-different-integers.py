class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def allsak(k):
            m={}
            l=0
            c=0
            for i in range(len(nums)):
                m[nums[i]]=m.get(nums[i],0)+1
                while len(m)>k:
                    m[nums[l]]-=1
                    if m[nums[l]]==0:
                        del m[nums[l]]
                    l+=1
                c+=i-l+1
            return c
        return allsak(k)-allsak(k-1)