class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        n=len(arr1)
        res=n
        for i in range(n):
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    res-=1
                    break

        return res
                    
