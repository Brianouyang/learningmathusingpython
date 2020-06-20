##改进代码
import time
def recDC(coinValueList,change,knownResults):#硬币体系和找零个数
    minCoins=change
    if change in coinValueList:#最小规模直接返回：正好等于某一硬币的币值
        knownResults[change]=1#记录最优解
        return 1
    elif knownResults[change]>0:
        return knownResults[change]#查表成功，直接用最优解
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recDC(coinValueList,change-i,knownResults)
            if numCoins<minCoins:
                minCoins=numCoins
                knownResults[change]=minCoins#最优解记录到表中
    return minCoins
memo=[0]*64
print(time.clock())
print(recDC([1,5,10,20,50,100],63,memo))
print(time.clock())
print(memo)
