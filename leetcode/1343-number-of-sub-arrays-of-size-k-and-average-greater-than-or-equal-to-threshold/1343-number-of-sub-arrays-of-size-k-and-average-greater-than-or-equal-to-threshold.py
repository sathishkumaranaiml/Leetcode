class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        sw=0
        j=0
        c=0
        for i in range(len(arr)):
            sw+=arr[i]
            windsz=i-j+1
            if windsz==k:
                if sw//k>=threshold:
                    c+=1
                sw=sw-arr[j]
                j+=1
        return c
        