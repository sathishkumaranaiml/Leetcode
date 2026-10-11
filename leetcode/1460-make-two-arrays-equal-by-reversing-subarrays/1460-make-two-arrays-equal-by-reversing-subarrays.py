class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arrfreq={}
        for i in arr:
            arrfreq[i]=arrfreq.get(i,0)+1
        for i in target:
            if i not in arrfreq:
                return False
            arrfreq[i]-=1
            if arrfreq[i]==0:
                del arrfreq[i]
        return len(arrfreq)==0

