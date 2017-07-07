def binarySearch(lst,key):
    low=0
    high=len(lst)-1
    while high>=low:
        mid=(low+high)//2
        if key<lst[mid]:
            high=mid-1
        elif key==lst[mid]:
            return mid
        else:
            low=mid+1
    return -low-1

#使用二分法的数组必须是已经排序好的数组
lst=[10,20,30,40,50,60,70,80,90]
print(binarySearch(lst,20))