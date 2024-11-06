class Solution:
    def decodeString(self, s: str) -> str:
        #Create a stack to store the number and string which will be used later
        stack=[]
        #Create a empty string and num to store string and numbers in it respectively
        string,num='',0
        #iterate through the s until the end
        for i in s:
        #If i started pointing [ then the letter and number that you store in string and num variable respectively add it in the stack
            if i=="[":
                stack.append(string)
                stack.append(num)
        #After adding it to stack reset the string and num to empty
                string=""
                num=0
        #If i started pointing ] then remove the letter and number from the stack respectively and initialize the removed elements to the stack_num and prev_string
            elif i=="]":
                stack_num=stack.pop()
                prev_string=stack.pop()
        #Update the string by adding prev_string and stack_num number of time the current string
                string=prev_string+stack_num*string
        #If the current value is number then store it in num
            elif i.isdigit():
                num=num*10 + int(i)
        #Else store the letter to string
            else:
                string+=i
        #Return the string which will be your answer
        return string   
