year=eval(input("enter a year"))
if (year%4==0 and year%100!=0 ) or year%400==0:
    print("闰年没错  老铁")
else:
    print("平年没错  老铁")