day=0
question="1 3   5   7\n"+\
    "9  11  13  15\n"+\
    "17 19  21  23\n"+\
    "25 27  29  31\n"
answer=eval(input(question))
if answer==1:
    day+=1

question="2 3   6   7\n"+\
    "10 11  14  15\n"+\
    "18 19  22  23\n"+\
    "26 27  30  31\n"
answer=eval(input(question))
if answer==1:
    day+=2

question="4 5   6   7\n"+\
    "12 13  14  15\n"+\
    "20 21  22  23\n"+\
    "28 29  30  31\n"
answer=eval(input(question))
if answer==1:
    day+=4

question="8 9   10  11\n"+\
    "12 13  14  15\n"+\
    "24 25  26  27\n"+\
    "28 29  30  31\n"
answer=eval(input(question))
if answer==1:
    day+=8

question="16    17  18  19\n"+\
    "20 21  22  23\n"+\
    "24 25  26  27\n"+\
    "28 29  30  31\n"
answer=eval(input(question))
if answer==1:
    day+=16

print("your birthday is ",day)
'''
/*
 * 关于猜生日的一些说明：
 * 一个人的生日只能是[1,31]号中的某一天，31的二进制位11111=00001+00010+00100+01000+10000，也就是：
 * 		00001--------------1
 * 		00010--------------2
 * 		00100--------------4
 * 		01000--------------8
 * 	+	10000--------------16
 * ————————————————————————————
 *      11111--------------31
 * 然而我们知道，二进制只能由0或者1组成，所以一个数字[1,31]的各个位数只能是0或者1，所以由上面的数组合可以组合相加，可以得到任意一个数字。
 * 这样的话，我们任意取一个数字,其二进制表示为：abcde(注：分别为各个位上的数字，比如10110，则a=1，b=0,c=1,d=1,e=0)，
 * 则abcde可以由如下算式得到：
 * 		0000e
 * 		000d0
 * 		00c00
 * 		0b000
 * 	 +	a0000
 * ————————————————————————————
 * 		abcde
 * 显然这个abcde是任意的，并且a，b,c,d或者e要么为0要么为1。这样我们可以将一个数[1,31]放在5个集合的某个集合中，
 * 规则是：
 * 如果这个数的e=1(不限定其他位数字),那么就应该放在集合set1中。
 * 如果这个数的d=1(不限定其他位数字),那么就应该放在集合set2中。
 * 如果这个数的c=1(不限定其他位数字),那么就应该放在集合set3中。
 * 如果这个数的b=1(不限定其他位数字),那么就应该放在集合set4中。
 * 如果这个数的a=1(不限定其他位数字),那么就应该放在集合set5中。
 * 注：显然可能一个数字放在多个集合中。
 * 当将这些数放置在不同的集合中后，通过指定某个数存在于5个集合中的哪些集合。我们便可以轻易的得到这个数字。
 * 举个例子来说，比如23，其二进制为10111，那么我们会将它放置到set1，set2，set3，set5中。
 * 这样当你指定说某个数在集合set1，set2，set3，set5，那么我们便知道，你说的某数必然是a=1,b=0,c=1,d=1,e=1.
 * 很容易的我们便可以猜出你说的某数为16+4+2+1=23。
 */
 只能说，知道的多可以让生活变得很有意思
'''