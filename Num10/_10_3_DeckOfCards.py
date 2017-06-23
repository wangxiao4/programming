import random
deck=[x for x in range(52)]
suits=['红桃','黑桃','方片','梅花']
ranks=['A','2','3','4','5','6','7','8','9','10','J','Q','K']

for i in range(13):
    value=random.randint(0,51)
    print(suits[int(value/13)],ranks[int(value%13)])