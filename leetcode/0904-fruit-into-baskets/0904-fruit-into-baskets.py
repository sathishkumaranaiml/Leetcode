class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        m={}
        maxi=maxlen=l=0
        for i in range(len(fruits)):
            fr=fruits[i]
            m[fr]=m.get(fr,0)+1
            if len(m)>2:
                m[fruits[l]]-=1
                if m[fruits[l]]==0:
                    del m[fruits[l]]
                l+=1
            maxlen=max(maxlen,i-l+1)
        return maxlen