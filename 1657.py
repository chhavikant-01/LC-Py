class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if(len(word1)!=len(word2)):
            return False
        s1 = set(word1)
        s2 = set(word2)

        if s1!=s2:
            return False

        c1 = list()
        c2 = list()

        for letter in s1:
            c1.append(word1.count(letter))
        for letter in s2:
            c2.append(word2.count(letter))
        c1.sort()
        c2.sort()
        for i in range(len(c1)):
            if(c1[i]!=c2[i]):
                return False
        return True
        
        
        

        

        
