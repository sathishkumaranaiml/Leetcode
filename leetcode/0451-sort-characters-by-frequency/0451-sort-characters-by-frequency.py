from collections import defaultdict
from typing import List
class Solution:
    def frequencySort(self, s: str) -> str:
        m={}
        for i in s:
            m[i]=m.get(i,0)+1
        bucket=defaultdict(list)
        res=[]
        for char,freq in m.items():
            bucket[freq].append(char)
        for i in range(len(s),0,-1):
            if i in bucket:
                for j in bucket[i]:
                    res.append(i*j)
        return "".join(res)

