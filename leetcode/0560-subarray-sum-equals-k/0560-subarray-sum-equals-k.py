class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m={0:1}
        c=0
        ps=0
        for i in nums:
            ps+=i
            if ps-k in m:
                c+=m[ps-k]
            m[ps]=m.get(ps,0)+1
        return c