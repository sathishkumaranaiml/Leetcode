class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        nb=0
        l=0
        people.sort()
        r=len(people)-1
        if len(people)==1:
            return 1
        while(l<=r):
            nb+=1
            if people[l]+people[r]<=limit:
                r-=1
                l+=1
            else:
                r-=1
        return nb

                
                


                

        