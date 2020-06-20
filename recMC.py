#找零兑换问题
##递归解法
def recMC(coinValueList,change):#硬币体系和找零个数
    minCoins=change
    if change in coinValueList:#最小规模直接返回：正好等于某一硬币的币值
        return 1
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recMC(coinValueList,change-i)
            if numCoins<minCoins:
                minCoins=numCoins
    return minCoins
import time
print(time.clock())
print(recMC([1,5,10,20,50,100],63))
print(time.clock())