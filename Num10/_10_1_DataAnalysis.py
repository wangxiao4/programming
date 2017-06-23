NUMBERF_OF_ELEMENTS=5
numbers=[]
sum=0

for i in range(NUMBERF_OF_ELEMENTS):
    value=eval(input("enter a number:\n"))
    numbers.append(value)
    sum+=value

average=sum/NUMBERF_OF_ELEMENTS
count=0
for i in range(NUMBERF_OF_ELEMENTS):
    if numbers[i]>average:
       count+=1

print("average:",average)
print("number of elements above the average is",count)