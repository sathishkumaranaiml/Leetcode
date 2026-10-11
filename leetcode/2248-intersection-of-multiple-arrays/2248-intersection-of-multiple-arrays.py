class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n=len(nums)
        if n==1:
            return sorted(nums[0])
        s=sorted(nums[0])
        res=[]
        for i in range(1,n):
            s1=sorted(nums[i])
            k,h=0,0
            while(k<len(s) and h<len(s1)):
                if s[k]<s1[h]:
                    k+=1
                elif s[k]>s1[h]:
                    h+=1
                else:
                    res.append(s[k])
                    k+=1
                    h+=1
            s=res
            res=[]
        return s


            


            