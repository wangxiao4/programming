import random
num=eval(input("enter a lottery number\n"))%100
lottery_num=random.randint(10,100)
if num==lottery_num:
    print("bouns:10000")
elif num//10==lottery_num%10 and num%10==lottery_num//10:
    print("bonus:3000")
elif num//10==lottery_num//10 or num%10==lottery_num%10:
    print("bonus:1000")

print("your number:",num,"\nlottery number:",lottery_num)