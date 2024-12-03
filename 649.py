class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        #Convert string to deque and assign it variable s
        s=collections.deque(senate)
        #Make variable count to count how many times R or D has come 
        countR,countD=0,0
        #Make variables d and r to store the total count of D and S
        d,r=senate.count('D'),senate.count('R')
        #Iterate through the loop until total count of R don't become 0
        while(r!=0):
        #if total count of D is zero then return Radiant
            if d==0:
                return "Radiant"
        #if count of R is greater then 0 and first element of s is D then pop it from index 0 and decrease the value of R count and total D count
            elif countR>0 and s[0]=='D':
                s.popleft()
                countR-=1
                d-=1
        #if count of D is greater then 0 and first element of s is R then pop it from index 0 and decrease the value of D count and total R count
            elif countD>0 and s[0]=='R':
                s.popleft()
                countD-=1
                r-=1
        #if first element is R then increase the count of R and rotate the deque to left
            elif s[0]=='R':
                countR+=1
                s.rotate(-1)
        #else increase the count of D and rotate the deque to left
            else:
                countD+=1
                s.rotate(-1)
        #Return Dire if while loop doesn't run or completed
        return "Dire"

        
