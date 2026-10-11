class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        m={}
        mini=float('inf')
        for i in range(len(cards)):
            if cards[i] in m:
                mini=min(mini,i-m[cards[i]]+1)
            m[cards[i]]=i
        return mini if mini!=float('inf') else -1