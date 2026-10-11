class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        res=[-1]*n
        sw=0
        j=0
        for i in range(0,n):
            sw+=nums[i]
            if i-j+1>=2*k+1:
                res[j+k]=sw//(2*k+1)
                sw-=nums[j]
                j+=1
        return res
            




        
        
            


        