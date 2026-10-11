class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        c=1
        intervals.sort()
        s,e=intervals[0]
        for s1,e1 in intervals:
            if s1>s and e1>e:
                c+=1
                s=s1
            e=max(e1,e)
        return c

