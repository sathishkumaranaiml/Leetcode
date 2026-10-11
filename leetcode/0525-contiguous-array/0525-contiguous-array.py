class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mxln=0
        m={0:-1}
        ps=0
        for i in range(len(nums)):
            ps+=1 if nums[i]==1 else -1
            if ps not in m:
                m[ps]=i
            else:
                mxln=max(mxln,i-m[ps])
        
        return mxln
