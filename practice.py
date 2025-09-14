#Task 1
for i in range(1,5):
    marks=int(input("Enter the marks: "))
    if marks>=91 and marks<=100:
        print("A")
    elif marks>=81 and marks<=90:
        print("B")
    elif marks>=71 and marks<=80:
        print("C")
    elif marks>=61 and marks<=70:
        print("D")
    elif marks>=50 and marks<=60:
        print("E")
    else:
        print("F")


#Task 2
num=int(input("Enter the number: "))
result=1

if num==0 or num==1:
    print("Factorial is 1")
else:
    for i in range(1,num+1):
        result=result*i
        

print("Factorial of a number: ",result)


#Task3
num=int(input("Enter a number\n "))
firstnum=0
secondnum=1
print("first number\n",firstnum)
print("second number\n", secondnum)
for i in range(2,num):
    nextnum=firstnum+secondnum
    firstnum=secondnum
    secondnum=nextnum
    print("Next number\n",nextnum)


