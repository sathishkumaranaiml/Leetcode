class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        i=0
        j=len(nums)-1
        res=0
        while(i<j):
            if nums[j]==0:
                j-=1
            elif nums[i]==0 and nums[j]!=0:
                nums[i],nums[j]=nums[j],0
                j-=1
                res+=1
            else:

                i+=1
        return res
        