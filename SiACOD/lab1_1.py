import random
import time
import matplotlib.pyplot as plt


'''Удалить из массива все отрицательные значения, а оставшиеся уплотнить (сдвинуть) 
с сохранением исходного порядка к началу массива.'''


def deleteNegativeNumbers(lengthArray: int, leftRange: int, rightRange: int):
    a = []
    for i in range(lengthArray):
        #n = int(random()*10) - 5
        n = random.randint(leftRange,rightRange)
        a.append(n)
    #print(a)
    firstTime = time.time()
    i = 0
    m = lengthArray
    while i < m:
        if a[i] < 0:
            del a[i]
            m -= 1
        else:
            i += 1
    #print(a)
    lastTime = time.time()
    executionTime = lastTime - firstTime
    print("Execution Time: ", executionTime)
    return executionTime
    

# deleteNegativeNumbers(10000, -25, 25)
# deleteNegativeNumbers(20000, -25, 25)
# deleteNegativeNumbers(30000, -25, 25)
# deleteNegativeNumbers(40000, -25, 25)
# deleteNegativeNumbers(50000, -25, 25)


# time = deleteNegativeNumbers(10, -25, 25)
# print(time)


# averageTimeArray = []
# for i in range(3):
#     timeArray = []
#     for i in range(10000, 60000, 10000):
#         executionTime = deleteNegativeNumbers(i, -25, 25)
#         print(executionTime, i)
#         timeArray.append(executionTime)
#     print(timeArray)
#     averageTimeArray.append(timeArray)
# print(averageTimeArray)

for i in range(3):
    timeArray = []
    x = []
    for i in range(10000, 60000, 10000):
        executionTime = deleteNegativeNumbers(i, -25, 25)
        print(executionTime, i)
        timeArray.append(executionTime)
        x.append(i)
    print(timeArray)

    plt.plot(x, timeArray)
plt.xlabel("Input data amount")
plt.ylabel("Processor ticks")
plt.show()