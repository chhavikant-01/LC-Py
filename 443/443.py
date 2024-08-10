# beats 10% in time and 84% in space
class Solution:
    def compress(self, chars: List[str]) -> int:
        self.s = ""
        self.i = 0
        self.n = len(chars)

        while self.i < self.n:
            self.char = chars[self.i]
            self.count = 0
            while self.i < self.n and chars[self.i] == self.char:
                self.count+=1
                self.i+=1
            self.s = self.s + self.char
            if self.count>1:
                self.s = self.s + str(self.count)
        self.s = list(self.s)
        chars.clear()
        chars.extend(self.s)
        return len(chars)


# beats 98% in time and 84% in space
class Solution:
    def compress(self, chars: List[str]) -> int:

        write = 0
        temp = chars[0]
        siz = len(chars)
        count = 1

        for i in range(1, siz): 

            # iterating to get all the values from chars
            if (chars[i] != temp): # if the value changes the followong will be done

                # adding the new character for the temp for checking
                temp = chars[i] 

                # changing in place of char
                chars[write] = chars[i-1] 

                # pointing the next point the data must be changed
                write += 1 

                if (count > 1): 
                    #if count > 1 the digits are added

                    num = str(count)
                    chars[write : write+len(num)] = [*num]
                    write = write + len(num)
                count = 1
            else:
                count += 1

                
        chars[write] = temp #adding the remaing data
        write += 1
        if (count > 1):
            num = str(count)
            chars[write : write+len(num)] = [*num]
            write = write + len(num)

        return write # return the final size of the compressed array


        