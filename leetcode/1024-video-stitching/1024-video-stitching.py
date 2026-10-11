class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        c=0
        clips.sort()
        currentend=nextend=0
        i=0
        while(currentend<time):
            while i<len(clips) and clips[i][0]<=currentend:
                nextend=max(nextend,clips[i][1])
                i+=1
            if nextend==currentend:
                return -1
            c+=1
            currentend=nextend
        return c