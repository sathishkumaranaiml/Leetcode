class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        cpy=sorted(nums)
        l=(n-1)//2
        r=n-1
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=cpy[l]
                l-=1
            else:
                nums[i]=cpy[r]
                r-=1
        return nums