class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i=0
        n=len(nums)
        while(i<n):
            cind=nums[i]-1
            if nums[i]<=len(nums) and  nums[cind]!=nums[i]:
                nums[i],nums[cind]=nums[cind],nums[i]
            else:
                i+=1
        res=[]
        for i in range(n):
            if i+1!=nums[i]:
                res.append(nums[i])
                res.append(i+1)
        return res
            

