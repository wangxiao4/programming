weight=eval(input("your weight\n"))
height=eval(input("your height\n"))/100
bmi=weight/(height**2)
if bmi>=30:
    print("痴胖")
elif bmi>=25:
    print("超重")
elif bmi>=18.5:
    print("标准")
else:
    print("超轻")