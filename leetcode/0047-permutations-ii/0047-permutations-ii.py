class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
 
        res=[]
        res.append(nums[:])
        n=len(nums)
        for _ in range(math.factorial(len(nums))-1):
            p=-1
            n=len(nums)
            for i in range(n-2,-1,-1):
                if nums[i]<nums[i+1]:
                    p=i
                    break
            if p==-1:
                nums.reverse()
            else:
                for i in range(n-1,p,-1):
                    if nums[i]>nums[p]:
                        nums[i],nums[p]=nums[p],nums[i]
                        break
                nums[p+1:]=reversed(nums[p+1:])
            if  nums not in res:
                res.append(nums[:])
        return res
            