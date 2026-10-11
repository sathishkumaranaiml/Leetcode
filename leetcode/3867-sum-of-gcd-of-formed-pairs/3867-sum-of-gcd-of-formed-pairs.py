from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n=len(nums)
        res=[0]*n  
        maxi=nums[0]
        for i in range(n): 
            maxi=max(maxi,nums[i])
            res[i]=gcd(nums[i],maxi)
        s=0
        i=0
        j=len(res)-1
        res.sort()
        while(i<j):
            s+=gcd(res[i],res[j])
            i+=1
            j-=1
        return s


        