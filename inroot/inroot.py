#оптимальый код для нахождения корня числа
def inroot( num , stepen):

    min = 0
    max = num

    while min < max:
        mid = (min + max)//2
        if mid**stepen>num:
            max = mid
        else:
            min = mid + 1
 
    return mid