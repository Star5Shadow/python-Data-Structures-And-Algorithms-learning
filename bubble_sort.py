# 冒泡排序
def bubble_sort(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            return


li = [1,3,4,7,6,24,8,9]
bubble_sort(li)
print(li)