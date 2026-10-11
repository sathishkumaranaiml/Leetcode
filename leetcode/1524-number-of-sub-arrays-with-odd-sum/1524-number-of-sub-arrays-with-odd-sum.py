class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res=e=o=cur=0
        n=len(arr)
        mod=10**9+7
        for i in range(n):
            cur+=arr[i]
            if cur%2!=0:
                res=(res+e+1)%mod
                o+=1
            else:
                res=(res+o)%mod
                e+=1
        return res
        