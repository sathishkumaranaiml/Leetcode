class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        arr=list(s)
        idx=0
        for i in range(len(s)):
            if y==arr[i]:
                arr[i],arr[idx]=arr[idx],arr[i]
                idx+=1
        return "".join(arr)