class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals,key=lambda x : x[1])
        prev_end=intervals[0][1]
        c=0
        for i in range(1,len(intervals)):
            if prev_end>intervals[i][0]:
                c+=1
                prev_end=min(prev_end,intervals[i][1])
            else:
                prev_end=intervals[i][1]
        return c