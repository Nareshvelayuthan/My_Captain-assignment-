#To print fibanacci series.
a= int(input("Number of fibonacci series need to be displayed:"))
i=0
num1=0
num2=1
print(0,1,end=',')
for i in range(a-2):
 i=num1+num2
 print(i,end=',')
 num1=num2
 num2=i
