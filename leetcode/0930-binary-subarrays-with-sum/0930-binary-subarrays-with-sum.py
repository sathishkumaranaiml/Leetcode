class Solution(object):
    def goala(self,nums,goal):
        ps=l=0
        res=0
        for i in range(len(nums)):
            ps+=nums[i]
            while l<=i and ps>goal:
                ps-=nums[l]
                l+=1
            res+=i-l+1
        return res
    def numSubarraysWithSum(self, nums, goal):
        return self.goala(nums,goal)-self.goala(nums,goal-1)
        
    