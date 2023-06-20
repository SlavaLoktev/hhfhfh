import random
import time
import matplotlib.pyplot as plt


'''Каждый элемент a[i] массива заменить на сумму элементов исходного массива вплоть 
до него самого включительно, т.е. от 0 до i-го.'''


def sumArray(arr, size):
    if (size == 0):
        return 0
    else:
        return arr[size - 1] + sumArray(arr, size - 1)


def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum
        

def replaceArrayWithSum(lengthArray: int, leftRange: int, rightRange: int):
    a = []
    for i in range(lengthArray):
        n = random.randint(leftRange,rightRange)
        a.append(n)
    #print(a)

    b = []
    # for i in range(lengthArray):
    #     a[i] = sum_arr(a, lengthArray)
    #     b.append(a[i])

    # while (lengthArray != 0):
    #     a[i] = sum_arr(a, lengthArray)
    #     lengthArray -= 1

    # for i in a:
    #     a[i] = sum_arr(a, lengthArray)
    #     b.append(a[i])

    # for i in range(len(a) - 1):
    #     a[i + 1] = a[i + 1] + a[i]

    # for i in range(len(a)):
    #     b.append(sum_arr(a, lengthArray))
    firstTime = time.time()
    for i in range(len(a) + 1):
        sourceArray = a
        N = i
        newArray = sourceArray[:N]
        b.append(listsum(newArray)) #работает
        #b.append(sumArray(newArray, len(newArray)))#тоже работает, но упирается в макс. глубину рекурсии (1000)
        #фиксится sys.setrecursionlimit(50000) вроде
    b.remove(b[0])
        
    #print(b)
    lastTime = time.time()
    executionTime = lastTime - firstTime
    print("Execution Time: ", executionTime)
    return executionTime

#replaceArrayWithSum(5, -5, 5)

for i in range(3):
    timeArray = []
    x = []
    for i in range(10000, 60000, 10000):
        executionTime = replaceArrayWithSum(i, -25, 25)
        print(executionTime, i)
        timeArray.append(executionTime)
        x.append(i)
    print(timeArray)

    plt.plot(x, timeArray)
plt.xlabel("Input data amount")
plt.ylabel("Processor ticks")
plt.show()