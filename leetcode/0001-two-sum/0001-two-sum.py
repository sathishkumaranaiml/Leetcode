class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values=sorted((num,idx) for idx,num in enumerate(nums))
        i=0
        j=len(nums)-1
        while(i<j):
            total=values[i][0]+values[j][0]
            if total<target:
                i+=1
            elif total>target:
                j-=1
            else:
                return [values[i][1],values[j][1]]
        return [-1,-1]