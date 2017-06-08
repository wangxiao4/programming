i=1
colCount=0
while i<100:
    i+=1
    j=1
    okCount=0;
    while j < i:
        j+=1
        if(i%j==0 and i!=j):
            okCount+=1
            break
    if okCount>0:
        continue
    else:
        if colCount>9:
            print("\n")
            colCount=0
        print(i,end="\t")
        colCount+=1
