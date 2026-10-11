class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        i=0
        j=n-1
        while(i<j):
            con=int(str(nums[i])+str(nums[j]))
            res+=con
            j-=1
            i+=1
        if(i!=j+1):
            res+=nums[n//2]
        return res


        