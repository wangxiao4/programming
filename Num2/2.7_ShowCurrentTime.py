import time
time_temp=int(time.time());
second=time_temp%60
minutes=time_temp/60%60
hour=time_temp/(60*60)%24+8
print(int(hour),":",int(minutes),":",int(second));

