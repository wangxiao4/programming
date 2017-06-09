import _7_3_TV

t1=_7_3_TV.TV()
t1.turnOn()
t1.setChannel(10)
t1.setVolumeLevel(10)

t2=_7_3_TV.TV()
t2.turnOn()
t2.setChannel(11)
t2.setVolumeLevel(11)

t1.turnOff()
print("t1:",t1.on,t1.getChannel(),t1.getVolumeLevel())
print("t2:",t2.on,t2.getChannel(),t2.getVolumeLevel())