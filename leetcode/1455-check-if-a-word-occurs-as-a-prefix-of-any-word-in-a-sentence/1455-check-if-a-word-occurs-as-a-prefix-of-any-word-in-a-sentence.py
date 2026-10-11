class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s=sentence.split()
        c=1

        for i in range(len(s)):
            if s[i].startswith(searchWord):
                return c
            c+=1
        return -1

        