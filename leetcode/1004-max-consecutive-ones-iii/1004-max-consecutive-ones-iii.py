class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi=l=maxlen=0
        m={}
        for i in range(len(nums)):
            m[nums[i]]=m.get(nums[i],0)+1
            maxi=max(maxi,m[nums[i]]) if nums[i]==1 else maxi
            while i-l+1-maxi>k:
                m[nums[l]]-=1
                if m[nums[l]]==0:
                    del m[nums[l]]
                l+=1
            maxlen=max(maxlen,i-l+1)
        return maxlen
