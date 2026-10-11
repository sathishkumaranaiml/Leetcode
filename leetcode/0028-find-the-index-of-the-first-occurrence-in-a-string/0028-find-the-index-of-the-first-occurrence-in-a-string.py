class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k=len(needle)
        for i in range(len(haystack)):
            if haystack[i:min(i+k,len(haystack))]==needle:
                return i
        return -1