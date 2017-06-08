status=eval(input("enter your status(0:单身\t1:已婚\t2:离异\t3:户主)\n"))
taxLevel1,taxLevel2,taxLevel3,taxLevel4,taxLevel5=0,0,0,0,0
if status==0:
    taxLevel1=8350
    taxLevel2=33950
    taxLevel3=82250
    taxLevel4=171550
    taxLevel5=372950
elif status==1:
    taxLevel1=16700
    taxLevel2=67900
    taxLevel3=137050
    taxLevel4=208850
    taxLevel5=372950
elif status==2:
    taxLevel1=8350
    taxLevel2=33950
    taxLevel3=68525
    taxLevel4=104425
    taxLevel5=186475
elif status==3:
    taxLevel1=11950
    taxLevel2=45500
    taxLevel3=117450
    taxLevel4=190200
    taxLevel5=372950

'''
#可用 但不优雅
income=eval(input("enter your income\n"))
personal=0;
tax=0;
if income>taxLevel5:
    tax+=(income-taxLevel5)*0.35+taxLevel4*0.33+taxLevel3*0.28+taxLevel2*0.25+taxLevel1*0.15+taxLevel1*0.1
elif income>taxLevel4:
    tax+=(income-taxLevel4)*0.33+taxLevel3*0.28+taxLevel2*0.25+taxLevel1*0.15+taxLevel1*0.1
elif income>taxLevel3:
    tax+=(income-taxLevel3)*0.28+taxLevel2*0.25+taxLevel1*0.15+taxLevel1*0.1
elif income>taxLevel2:
    tax+=(income-taxLevel2)*0.25+taxLevel1*0.15+taxLevel1*0.1
elif income>taxLevel1:
    tax+=(income-taxLevel1)*0.15+taxLevel1*0.1
else:
    tax+=income*0.1

print("income:",income,"\tpersonal:",income-tax,"\ttax:",tax)
'''
income=eval(input("enter your income\n"))
temp_income=income
tax=0
if income>taxLevel5:
    temp_income-=taxLevel5
    tax+=temp_income*0.35
    temp_income=taxLevel5
if income>taxLevel4:
    temp_income-=taxLevel4
    tax+=temp_income*0.33
    temp_income=taxLevel4
if income>taxLevel3:
    temp_income-=taxLevel3
    tax+=temp_income*0.28
    temp_income=taxLevel3
if income>taxLevel2:
    temp_income-=taxLevel2
    tax+=temp_income*0.25
    temp_income=taxLevel2
if income>taxLevel1:
    temp_income-=taxLevel1
    tax+=temp_income*0.15
    temp_income=taxLevel1
tax+=temp_income*0.1
print("income:",income,"\tpersonal:",income-tax,"\ttax:",tax)