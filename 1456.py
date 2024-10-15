class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        max_num = 0
        s = list(s)
        numVowel = 0

        for i in range(0,k):
            if s[i] in vowels:
                numVowel = numVowel + 1
            if numVowel > max_num:
                max_num = numVowel
        
        for i in range(k, len(s)):
            print(s[i], end = " ")
            if s[i-k] in vowels:
                numVowel = numVowel - 1
            if s[i] in vowels:
                numVowel = numVowel + 1
                
            if numVowel > max_num:
                max_num = numVowel
        
        return max_num
