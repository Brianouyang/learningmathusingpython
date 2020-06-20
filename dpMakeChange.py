#找零兑换问题
##动态规划解法
def dpMakeChange(coinValueList,change,minCoins):
    #从1分开始到change逐个计算最少硬币数
    for cents in range(1,change+1):
        #初始化硬币数最大值
        coinCounts=cents
        #减去每个硬币类型，向后查最少硬币数，同时记录总的最少数
        for j in [c for c in coinValueList if c<=cents]:
            if minCoins[cents-j]+1<coinCounts:
                coinCounts=minCoins[cents-j]+1
        #得到当前最少硬币数，计入表中
        minCoins[cents]=coinCounts
    #返回最后一个结果
    return minCoins[change]
print(dpMakeChange([1,5,10,21,25],90,[0]*101))