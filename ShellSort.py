# 谢尔排序
def shellSort(alist):
    # 间隔设定
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        # 子列表排序
        for startpos in range(sublistcount):
            # 带间隔的插入排序
            gapinsertionSort(alist, startpos, sublistcount)
        print("After increment of size", sublistcount, "The list is", alist)
        sublistcount = sublistcount // 2
    return alist


def gapinsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        pos = i
        while pos >= gap and alist[pos - gap] > currentvalue:
            alist[pos] = alist[pos - gap]
            pos = pos - gap
        alist[pos] = currentvalue


lista = [17, 26, 93, 44, 77, 31, 54, 55, 20]
lista1 = shellSort(lista)
print(lista1)
