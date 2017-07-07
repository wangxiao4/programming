def insertionSort(lst):
    for i in range(1,len(lst)):
        currentElement=lst[i]
        k=i-1
        while k>=0 and lst[k]>currentElement:
            lst[k+1]=lst[k]
            k-=1
        lst[k+1]=currentElement
        print(lst)

lst=[5,6,1,7,-2,9,-8,3,4,8,32,-1];
print(insertionSort(lst))