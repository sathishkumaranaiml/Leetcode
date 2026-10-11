class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        for i in range(1,len(arr)):
            arr[i]=arr[i-1]^arr[i]
        for l,r in queries:
            if l>0:
                res.append(arr[r]^arr[l-1])
            else:
                res.append(arr[r])
        return res