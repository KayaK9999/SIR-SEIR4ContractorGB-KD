import random
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import math

def counts(arr):
    count = [0, 0, 0, 0]
    for row in arr:
        for elem in row:
            count[int(elem) + 1] += 1
    return count

def rule1(array, record, iteration, mean, std_dev, colors):
    h, w = array.shape[0], array.shape[1]
    custom_cmap = ListedColormap(colors)
    position = [[0, 0], [0, int(h / 2)], [int(w / 2), int(h / 2)]]    # 初始直角，线，中心位置
    savePos = ['corner', 'edge', 'center']
    for p in range(3):
        plt.clf()  # 清空当前图形
        arr = array.copy()
        arr[position[p][0]][position[p][1]] = 1
        plt.imshow(arr, cmap=custom_cmap, interpolation='nearest')
        plt.clim(-1, 2)
        plt.colorbar()    
        plt.savefig('plot/rule1/' + savePos[p] + '/m' + str(0))
        for ir in range(iteration):
            newArray = np.zeros((h, w))
            for i in range(h):
                for j in range(w):
                    if arr[i][j] == -1:
                        newArray[i][j] = -1
                    elif arr[i][j] == 1:
                        newArray[i][j] = 2
                        dir = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]
                        for d in dir:
                            pos = [i + d[0], j + d[1]]
                            if pos[0] >= 0 and pos[0] < h and pos[1] >= 0 and pos[1] < w:
                                if newArray[pos[0]][pos[1]] == 0:
                                    p1 = np.random.normal(mean, std_dev, size=1)
                                    p2 = 1 / math.sqrt(d[0] * d[0] + d[1] * d[1])
                                    if p1 * p2 >= 0.6:
                                        newArray[pos[0]][pos[1]] = 1
                                    else:
                                        newArray[pos[0]][pos[1]] = -1
                    elif arr[i][j] == 2:
                        newArray[i][j] = 2
            record[:, ir + 1] = counts(newArray)
            arr = newArray
            plt.imshow(arr, cmap=custom_cmap, interpolation='nearest')
            plt.clim(-1, 2)
            plt.savefig('plot/rule1/' + savePos[p] + '/m' + str(ir + 1))
        fig, ax = plt.subplots(figsize=(10, 6))
        # colors = ['red', 'orange', 'yellow', 'green']
        for i in range(4):
            ax.plot(record[i], color = colors[i])
        plt.savefig('plot/rule1/line/' + savePos[p])


def rule2(arr, iteration):
    print('2')

def rule3(arr, iteration):
    print('3')

def rule4(arr, iteration):
    print('4')


if __name__ == '__main__':
    # 初始化元胞数组
    width, height = 20, 20              # 元胞空间宽高
    initRefuseRate = 0.01               # 初始条件拒绝状态比例
    iteration = 5                      # 迭代次数
    mean, std_dev = 0.7, 0.01           # 正态分布中的均值和标准差
    colors = ['#EC8AA4', '#F0C800', '#5CB3CC', '#7BCFA6']       # 颜色

    sum = width * height
    array = np.zeros((height, width))
    numbers = random.sample(range(sum), int(sum * initRefuseRate))
    len = len(numbers)
    print('len:', len)
    for i in range(len):
        num = numbers[i]
        array[num // height][num % width] = -1
    record = np.zeros((4, iteration + 1))
    record[:, 0] = [int(sum * initRefuseRate), sum - int(sum * initRefuseRate) - 1, 1, 0]

    # rule1 运行这个
    # rule1(array, record, iteration, mean, std_dev, colors)

    # rule2 修改
    # refuseRate = [0.001, 0.01, 0.05, 0.1]


