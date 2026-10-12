class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        for j in range(i,5000):
            s=0
            pv=j
            for k in nums:
                s=k+pv
                if s<=0 or s==0:
                    break
                pv=s
            if s>0:
                return j
