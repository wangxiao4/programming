import random
import time

questionNum=0
score=0
useTime=time.time()

while questionNum < 5:
    rand_num1=random.randint(1,100)
    rand_num2=random.randint(1,100)

    userNumber=eval(input("what is "+str(rand_num1)+" - "+str(rand_num2)+" ?"))
    if userNumber==rand_num1-rand_num2:
        score+=1

    questionNum+=1

useTime=(time.time()-useTime)//1
print("共回答",questionNum,"道题，答对",score,"道，用时",useTime,"秒")

