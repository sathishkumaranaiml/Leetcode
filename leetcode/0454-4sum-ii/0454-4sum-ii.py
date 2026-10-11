class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        m={}
        n=len(nums1)
        for i in range(n):
            for j in range(n):
                m[nums1[i]+nums2[j]]=m.get(nums1[i]+nums2[j],0)+1
        c=0
        for i in range(n):
            for j in range(n):
                s=nums3[i]+nums4[j]
                c+=m.get(-s,0)
        return c
        
        