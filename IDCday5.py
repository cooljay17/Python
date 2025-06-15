#Write a function that computes the sum and average of a list of numbers
def SumAvgList(lst):
    sum=0
    for i in range(len(lst)):
        sum=sum+lst[i]
    print("Sum of the items in the list:",sum)
    print("Average of the items in the list:",sum/len(lst))


def main():
    n=int(input("Enter the number of numbers to be added in the list: "))
    lst=[]
    for i in range(n):
        item=int(input("Enter the number to be added in the list: "))
        lst.append(item)
    print("List of numbers to find the sum and average",lst)
    SumAvgList(lst)

main()  

 