class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        l=sum(cardPoints[:k])
        r=0
        j=len(cardPoints)-1
        maxi=l
        for i in range(k-1,-1,-1):
            l-=cardPoints[i]
            r+=cardPoints[j]
            j-=1
            maxi=max(maxi,l+r)
        return maxi
        