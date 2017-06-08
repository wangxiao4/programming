count=eval(input("enter count:"))
#100 50 20 10 5 1 5 1 5 1 5
print(count//100,"张100元，",count%100//50,"张50元，",count%50//20,"张20元,",count%50%20//10,"张10元,",count%10//5,"张5元",count%5//1,"张1元",count*10%10//5,"张5毛",count*10%10%5//1,"张1毛",count*100%10//5,"张5分",count*100%5,"张1分")