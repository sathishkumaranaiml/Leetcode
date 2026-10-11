class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.extend([float("-inf"),float("inf")])
        heaters.sort()
        r=0
        j=1
        for i in houses:
            while heaters[j]<i:
                j+=1
            md=min(i-heaters[j-1],heaters[j]-i)
            r=max(r,md)
        return r

            



        