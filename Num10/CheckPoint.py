#10.1    [] [1,32,2]
#10.2    6   0   5   12  10
#10.3    [30,1,2,1,0,40] [30,43,1,2,1,0,40] [30,43,1,2,1,0,40,1,43] [30,1,2,1,0,40,1,43] [30,2,1,0,40,1,43] [30,2,1,0,40,1] [0,1,1,2,30,40] [40,30,2,1,1,0] 随机排序列表
#10.4    1   2   5   30  0   34
#10.5    [30,1,2,1,0,1,21,13]    [2,42,26]   [2,42,26]   [1,2] 1
#10.6    [30,2] [0, 2, 4, 6, 8] [10,8,6,4,2]
#print([x for x in range(0,10,2)])
#10.7   false   false false True true true
#10.8   false true true true
#list=["1",2,True]
#print(list)
#10.9   [22,43] [1,43]
#10.10  [22,43] [1,43]
'''
list1=[1,43]
list2=[x for x in list1]
print(list2)
'''

#10.11  通过split()   使用‘o’作为分隔符
#10.12  [Flase for i in range(100) ]    list[len(list)-1]=5.5   list[0]+list[1]     sum(list[:5])   min(list)   list[random.range(len(list))]
#10.13  indexError
#10.14  [1,1,2,3,4,5,6]

#10.15  [111,3,5,7,9]   [111,3,5,7,9]
'''
list1=list(range(1,10,2))
list2=[]+list1
list1[0]=111
print(id(list1))
print(id(list2))
print(id(list1[0]))
'''

#10.16  [111,3,5,7,9]   [1,3,5,7,9]
#10.17  假
#10.18  0，3     猜测是5,4,3,2,1  结果是1,2,3,4,5  ，通过下列测试可知，一旦传递到方法中的可变元素对原ID数据进行修改，那么原数组也会发生改变，否则不会对原有的数据有影响，可直接注释赋值运算区域进行测试
'''
def main():
    list=[1,2,3,4,5]
    print("原ID：",id(list),end=" ")
    reverse(list)
    print("方法执行完测试值：",list[0])

def reverse(list):
    print("传递后ID：",id(list),end=" ")
    newList=len(list)*[0]
    for i in range(len(list)):
        newList[i]=list[len(list)-1-i]
    print("新数组ID：",id(newList),end=" ")
    list=newList
    list[0]=5
    print("替换后ID：",id(list),end=" ")
    print("测试值：",list[0])
main()
'''
#10.19  1,2,3/2,3       1,2,3/1,2,3
#10.20-10.25    ……

