class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        rem={0:1}
        ps=0
        c=0
        for i in nums:
            ps+=i
            r=ps%k
            c+=rem.get(r,0)
            rem[r]=rem.get(r,0)+1
        return c
            
        