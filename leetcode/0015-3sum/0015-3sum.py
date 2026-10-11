class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        """
        res=[]
        n=len(nums)
        nums.sort()
        for i in range(n-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1] :
                continue
            l,r=i+1,n-1
            while(l<r):
                cs=nums[i]+nums[l]+nums[r]
                if cs>0:
                    r-=1
                elif cs<0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    r-=1
                    l+=1
                    while(l<r and nums[l]==nums[l-1]):
                        l+=1
                    while(l<r and nums[r]==nums[r+1]):
                        r-=1
        return res

                
           


        
                

        