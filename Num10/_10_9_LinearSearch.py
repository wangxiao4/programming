def linearSearch(list,key):
    for i in range(len(list)):
        if key == list[i]:
            return i
    return -1

list=[1,2,3,4,5,6,4,8,2]
print(linearSearch(list,1))
print(linearSearch(list,8))
print(linearSearch(list,2))