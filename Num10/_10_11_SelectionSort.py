def selectionSort(lst):
    for i in range(len(lst)-1):
        currenMin=lst[i]
        currenMinIndex=i
        for j in range(i+1,len(lst)):
            if currenMin>lst[j]:
                currenMin = lst[j]
                currenMinIndex=j
        if currenMinIndex !=i:
            lst[currenMinIndex]=lst[i]
            lst[i]=currenMin
            #print(lst)
    return lst

lst=[5,6,1,7,-2,9,-8,3,4,8,32,-1];
print(selectionSort(lst))
