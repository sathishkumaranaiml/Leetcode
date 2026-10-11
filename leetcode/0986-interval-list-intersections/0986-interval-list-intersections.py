class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res=[]
        i=j=0
        while(i<len(firstList) and j<len(secondList)):
            s1,e1=firstList[i]
            s2,e2=secondList[j]
            instart=max(s1,s2)
            inend=min(e1,e2)
            if instart<=inend:
                res.append([instart,inend])
            if e1<e2:
                i+=1
            else:
                j+=1
        return res        