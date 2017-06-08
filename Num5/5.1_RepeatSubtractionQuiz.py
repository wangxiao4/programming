import random
rand_num1=random.randint(0,100)
rand_num2=random.randint(0,100)
state=0

while state==0:
    user_value=eval(input("what is "+str(rand_num1)+"-"+str(rand_num2)+"?\n"))
    if user_value==rand_num1-rand_num2:
        print("you win")
        state=1
    else:
        print("loser again")
