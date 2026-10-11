class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xall=0
        for i in nums:
            xall^=i
        di=xall&(-xall)
        x=0
        for i in nums:
            if(i&di):
                x^=i
        return [x,xall^x]
            

        