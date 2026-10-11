class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi=0
        for i in accounts:
            maxi=max(sum(i),maxi)
        return maxi