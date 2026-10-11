class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m={}
        for i in nums:
            m[i]=m.get(i,0)+1
        c=0
        res=[]
        for i,j in sorted(m.items(),key=lambda x:x[1],reverse=True):
            if c<k:
                res.append(i)
                c+=1
        return res


       
            
        