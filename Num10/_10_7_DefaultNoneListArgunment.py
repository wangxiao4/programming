

def add(x,list=None):
    if list==None:
        list=[]
    if x not in list:
        list.append(x)
    return list
def main():
    list1=add(1)
    print(list1)
    list2=add(2)
    print(list2)
    list3=add(3,[11,12,13,14])
    print(list3)
    list4=add(4)
    print(list4)

main()

