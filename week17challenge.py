#Given a list ["Elie", "Tim", "Matt"], create a variable called answer,
# which is a new list containing the first letter of each name in the list.
nameList=["Elie", "Tim", "Matt"]
answer=[]
for i in range(len(nameList)):
    word=nameList[i]
    answer.append(word[0])
print(answer)

#Given a list [1,2,3,4,5,6], create a new variable called answer2,
# which is a new list of all the even values. Another good candidate for a list comp.
num=[1,2,3,4,5,6]
answer2=[]
for i in range(len(num)):
    if num[i] % 2 == 0:
        answer2.append(num[i])
print(answer2)
