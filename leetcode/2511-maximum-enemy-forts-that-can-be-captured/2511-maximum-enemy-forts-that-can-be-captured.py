class Solution:
    def captureForts(self, forts: List[int]) -> int:
        maxi=0
        l=0
        for r in range(len(forts)):
            if forts[r]!=0:
                if (forts[l]==1 and forts[r]==-1) or (forts[l]==-1 and forts[r]==1):
                    maxi=max(maxi,r-l-1)
                l=r
        return maxi