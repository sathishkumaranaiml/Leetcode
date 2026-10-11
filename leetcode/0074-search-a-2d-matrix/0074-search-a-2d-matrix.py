class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m,n=len(matrix),len(matrix[0])
        l,r=0,n*m-1
        while(l<=r):
            mid=(l+r)//2
            rval=mid//n
            cval=mid%n
            val=matrix[rval][cval]
            if val==target:
                return True
            elif val<target:
                l=mid+1
            else:
                r=mid-1
        return False
