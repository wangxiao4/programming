#字符串的创建
s1=str()
s2=str("Welcome")
s3=""
s4="Welcome"
#内容一旦创建就不会再更改，并且具有相同值的变量引用的值是同一个（值ID相同）

#处理字符串函数
len("123")#返回字符个数
max("abc")#返回字符串中最大的字符
min("abc")#返回字符串中最小的字符

#下标运算符[]
#截取字符串[start:end]  返回下标start开始到下标end(不包含end)的字串         start:默认0  end:默认len(s)
s="Welcome"
s5=s[1:4] #'elc'
s6=s[1:-2]# end : len(s)+(-2)

#连接运算符 +  复制运算符 *
s7=s5+s6
s8=s5*3#相当于多个自加
#print(s8)
#in / not in 是否包含
print("c" in s8)
print("c" not in s8)

#比较字符串  == != < > <= >=     按位比较
#迭代字符串 for i in s
#测试字符串
#isalnum()  只有字符或数字且至少一个
#isalpha()  只有字母且至少一个
#isdigit()  只有数字
#isidentifier() 只有标识符
#islower()  全部小写
#isupper()  全部大写
#isspace()  只包含空格

#搜索字串
#endswith(s1)   是否以s1结尾
#startwith(s2)  是否以s2开头
#find(s1)       返回第一次出现的下标，无则返回-1
#rfind(s2)      返回最后一次出现的下标，无则返回-1
#count(s1)      返回s1的出现次数

#转换字符串
#capitalize()   返回首字母大写的字符串
#lower()        返回小写
#upper()        返回大写
#title()        返回每个首字母大写的字符串
#swapcase()     返回大小写转换后的字符串
#replace(old,new)   返回替换后的字符串

#删除空格
#lstrip()       返回去掉前端空格的字符串
#rstrip()       返回去掉尾端空格的字符串
#strip()        返回去掉两端空格的字符串

#格式化字符串
#center(width)       返回在给定宽度域居中的字符串
#ljust(width)        返回左对齐
#rjust(width)        返回右对齐
#format(items)       格式化字符串










