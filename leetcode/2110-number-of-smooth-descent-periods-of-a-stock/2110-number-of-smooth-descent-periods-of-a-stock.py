class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # two pointer
        j=0
        res=1
        for i in range(1,len(prices)):
            if prices[i-1]-prices[i]!=1:
                j=i
            res+=i-j+1
        return res

        