class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        c=0
        r=[]
        for i in range(n):
            if candyType[i] not in r and c<n//2:
                r.append(candyType[i])
                c+=1
        return c
        