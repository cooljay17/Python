#ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything
# but exactly 4 digits or exactly 6 digits.
# Your task is to create a function that takes a string
# and returns True if the PIN is valid and False if it's not.
def isPinValid(pin):
    for char in pin:
        if char.isalpha():
            return False
    if len(pin)=="" :
        return False
    elif len(pin)!=4:
        if len(pin)!=6:
            return False
        else :
            return True
    else :
        return True
pin="1234"
result=isPinValid(pin)
print(result)


#In this exercise you will have to:
# Take a list of names.
# Add "Hello" to every name.
# Make one big string with all greetings.
# The solution should be one string with a comma in between every "Hello (Name)".
def greet_people(str):
 answer=[]
 for i in str:
     answer.append("Hello "+ i)
 answerstr=','.join(answer)
 return answerstr
qn=["Jay","Rahul","Honey"]
output=greet_people(qn)
print(f"'"+output+"'")

