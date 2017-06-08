#5.1    true true/false false
#5.2    无法进入循环体
#5.3    死环 死环 9
#5.4    死环 死环 缩进/死环
#5.5    5 0
#5.6    14 5
#5.7    认为可转    for更灵活，for循环是遍历元素  while是判断是否符合条件
#5.8
'''
sum=0
i=0
while i<1001:
    sum+=i
    i+=1

print(sum)
'''
#5.9
'''
sum=0
for i in range(10000):
    sum+=i
'''
#5.10   n n n-5 (n-5)//3
#5.11   0   01  012 0123    01234
'''
#由此可见 range（x,y,z） x通过步长z到y的遍历
i=0
while i<5:
    for j in range(i,1,-1):
        print(j,end=" ")
    print("******")
    i+=1
'''
#5.12   不确定是否n2>n1，true的情况下正确
#5.13   break作用是终止循环    continue作用是跳出本次循环       会 不会
#5.14   i+=1 上移到while下一行
#5.15和5.16  略……