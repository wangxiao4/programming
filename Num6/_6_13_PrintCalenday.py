import time
#主函数
def main():
    printCalenday()

#打印函数
def printCalenday():

    month=time.strftime("%m",time.localtime())
    year=time.strftime("%Y",time.localtime())
    printHead(month,year)
    printBody(int(month),int(year))

#打印头
def printHead(month,year):
    print("             ",year,"年",month,"月")
    print("-----------------------------------------")
    print("周日  周一  周二  周三  周四  周五  周六")
#打印主体
def printBody(month,year):
    #获取距离1800天总天数
    days=getDays(month,year)
    weekDay=getWeekDay(days)
    if weekDay!=7:
        printFormat()
        for i in range(1,weekDay):
            printFormat()
    temp=weekDay
    daysOfMonth=getDaysByMonth(month,year)
    for i in range(1,daysOfMonth+1):
        if temp>6:
            print()
            temp=0
        printFormat(i)
        temp+=1
    print()
#获取某年某月距离1800/01/01的天数
def getDays(month,year):
    days=0
    for i in range(1800,year):
        if isLeapYear(i):
            days+=366
        else:
            days+=365
    for i in range (1,month):
        days += getDaysByMonth(i,year)
    return days

def getDaysByMonth(month,year):
    days=0
    if month == 1 or month == 3 or month == 5 or month == 8 or month == 10 or month == 12:
        days += 31
    elif month == 2:
        if isLeapYear(year):
            days += 29
        else:
            days += 28
    else:
        days += 30
    return days

#获取某天是周几
def getWeekDay(days):
    return (days+3)%7

def isLeapYear(year):
    return year%400==0 or (year%4==0 and year%100!=0)

def printFormat(num1=" "):
    print(format(num1,"3"),end="   ")

main()