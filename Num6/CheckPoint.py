#6.1    使代码具有高度重用性 有利于模块化
#6.2    def 函数名(参数)         调用 函数名(参数)
#6.3    我不行啦
#6.4    不一定  无返回函数也可以被用在表达式中，又返回的也可以直接使用名称调用本身
#6.5    可以有 不会
#6.6    ……
#6.7    ……
#6.8    书写格式注意缩进
#6.9    None
#6.10   TypeError: unorderable types: NoneType() < NoneType()
'''
def min(n1,n2):
    smallest=n1
    if n2<smallest:
        smallest=n2
def main():
    print(min(min(5,6),min(51,6)))
main()
'''

#6.11   因为python变量属于弱类型，所以调用函数的时候并没有任何检查，填入对应个数的参数叫做位置参数，使用name=value传递确保正确的传递叫做关键字参数
#6.12   对错错对对
#6.13   赋值操作只是将变量值的地址指向别传递的值的地址  这就是值传递
#6.14   可以
#6.15   ……
#6.16   ……
#6.17   2  3.4  2  4            3  6  5
#6.18   变量未定义（作用域错了）
#6.19   无法运行 变量y未定义
#6.20   1 2     5 2     1 24        4 5
#6.21   使用了位置参数 message=5 n为空  改为n=5
#6.22   调用最后出现的函数
#6.23   可以      14 4 45 1.6
#6.24   randint(33,55)      chr(randint(ord('B'),ord('M')))     (randint(65,565)+1)*0.1     chr(randint(ord('a'),ord('z')))