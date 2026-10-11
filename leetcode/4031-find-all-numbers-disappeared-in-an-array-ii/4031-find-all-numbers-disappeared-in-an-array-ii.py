class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        present = set(nums)
        res = []
        i = lower
        while i <= upper:
            if i not in present:
                start = i
                while i <= upper and i not in present:
                    i += 1
                res.append([start, i - 1])
            else:
                i += 1
        return res
                
                
            
        
        