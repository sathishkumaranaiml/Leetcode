class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        start=intervals[0][0]
        end=intervals[0][1]
        res=[]
        for i in range(1,len(intervals)):
            nextstart=intervals[i][0]
            nextend=intervals[i][1]
            if nextstart<=end:
                end=max(end,nextend)
            else:
                res.append([start,end])
                start=nextstart
                end=nextend
        res.append([start,end])
        return res
        