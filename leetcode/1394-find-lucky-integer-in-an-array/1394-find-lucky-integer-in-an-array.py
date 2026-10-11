class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m={}
        for i in arr:
            m[i]=m.get(i,0)+1
        maxi=-1
        for i,j in m.items():
            if i==j:
                maxi=max(maxi,i)
        return maxi