class Solution:
    def isPalindromic(self, s: str) -> bool:
        pas=""
        for i in s:
            pas+=bin(ord(i))[2:].zfill(8)
        if pas[::-1]==pas:
            return True
        else:
            return False