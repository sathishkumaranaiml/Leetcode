class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        m={}
        l=0
        res=0
        maxi=0
        for r in range(len(answerKey)):
            m[answerKey[r]]=m.get(answerKey[r],0)+1
            maxi=max(maxi,m[answerKey[r]]) 
            while r-l+1-maxi>k:
                
                m[answerKey[l]]-=1
                if m[answerKey[l]]==0:
                    del m[answerKey[l]]      
                l+=1
            res=max(res,r-l+1)
        return res