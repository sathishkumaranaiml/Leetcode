class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res=0
        m={}
        ps=0
        for i in nums:
            ps+=1 if i%2!=0 else 0
            if ps==k:
                res+=1
            if ps-k in m:
                res+=m[ps-k]
            m[ps]=m.get(ps,0)+1
        return res
                    
            
