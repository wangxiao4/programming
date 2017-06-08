count=0
i=0
while i<100:
    i+=1
    if(i%2==0):
        continue
    count+=1
print("执行累加语句次数：",count)
