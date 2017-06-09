class TV:
    def __init__(self):
        self.channel=1
        self.volumeLevel=1
        self.on=False
    def turnOn(self):
        self.on=True
    def turnOff(self):
        self.on=False
    def getChannel(self):
        return self.channel
    def setChannel(self,value):
        self.channel=value
    def getVolumeLevel(self):
        return self.volumeLevel
    def setVolumeLevel(self,value):
        self.volumeLevel=value

    def channelUp(self):
        self.channel+=1
        if self.channel>45:
            self.channel=1
    def channelDown(self):
        self.channel-=1
        if self.channel<1:
            self.channel=45
    def volumeLevelUp(self):
        if self.volumeLevel<100:
            self.volumeLevel+=1
    def volumeLevelDown(self):
        if self.volumeLevel>0:
            self.volumeLevel-=1
