import math
import random
import numpy as np
import matplotlib.pyplot as plt

def updateTransMatrix():
    for i in range(0, length):
        for j in range(0, width):
            # 计算L1
            L1 = 0
            isCal = 0  # 是否出现最近的选项
            n = 0  # 同一距离中点的数量
            sumL1 = 0  # 方便求平均值
            if (initMatrix[i][(j + 1) % width]['value'] == 2):
                isCal = 1
                n = n + 1
                sumL1 = sumL1 + math.sqrt(initMatrix[i][j]['g'] * initMatrix[i][(j + 1) % width]['s'])
            if (initMatrix[i][(j + length - 1) % width]['value'] == 2):
                isCal = 1
                n = n + 1
                sumL1 = sumL1 + math.sqrt(initMatrix[i][j]['g'] * initMatrix[i][(j + length - 1) % width]['s'])
            if (initMatrix[(i + 1) % length][j]['value'] == 2):
                isCal = 1
                n = n + 1
                sumL1 = sumL1 + math.sqrt(initMatrix[i][j]['g'] * initMatrix[(i + 1) % length][j]['s'])
            if (initMatrix[(i + length - 1) % length][j]['value'] == 2):
                isCal = 1
                n = n + 1
                sumL1 = sumL1 + math.sqrt(initMatrix[i][j]['g'] * initMatrix[(i + length - 1) % length][j]['s'])
            if (isCal != 0):
                L1 = sumL1 / n
            else:
                if (initMatrix[(i + 1) % width][(j + 1) % width]['value'] == 2):
                    isCal = 1
                    n = n + 1
                    sumL1 = sumL1 + math.sqrt(
                        initMatrix[i][j]['g'] * initMatrix[(i + 1) % width][(j + 1) % width]['s'] / 2)
                if (initMatrix[(i + length - 1) % width][(j + 1) % width]['value'] == 2):
                    isCal = 1
                    n = n + 1
                    sumL1 = sumL1 + math.sqrt(
                        initMatrix[i][j]['g'] * initMatrix[(i + length - 1) % width][(j + 1) % width]['s'] / 2)
                if (initMatrix[(i + 1) % width][(j + length - 1) % width]['value'] == 2):
                    isCal = 1
                    n = n + 1
                    sumL1 = sumL1 + math.sqrt(
                        initMatrix[i][j]['g'] * initMatrix[(i + 1) % width][(j + length - 1) % width]['s'] / 2)
                if (initMatrix[(i + length - 1) % width][(j + length - 1) % width]['value'] == 2):
                    isCal = 1
                    n = n + 1
                    sumL1 = sumL1 + math.sqrt(
                        initMatrix[i][j]['g'] * initMatrix[(i + length - 1) % width][(j + length - 1) % width]['s'] / 2)
                if (isCal != 0):
                    L1 = sumL1 / n
                else:
                    if (initMatrix[i][(j + 2) % width]['value'] == 2):
                        isCal = 1
                        n = n + 1
                        sumL1 = sumL1 + math.sqrt(initMatrix[i][j]['g'] * initMatrix[i][(j + 2) % width]['s'] / 4)
                    if (initMatrix[i][(j + length - 2) % width]['value'] == 2):
                        isCal = 1
                        n = n + 1
                        sumL1 = sumL1 + math.sqrt(initMatrix[i][j]['g'] * initMatrix[i][(j + length - 2) % width]['s'] / 4)
                    if (initMatrix[(i + 2) % length][j]['value'] == 2):
                        isCal = 1
                        n = n + 1
                        sumL1 = sumL1 + math.sqrt(initMatrix[i][j]['g'] * initMatrix[(i + 2) % length][j]['s'] / 4)
                    if (initMatrix[(i + length - 2) % length][j]['value'] == 2):
                        isCal = 1
                        n = n + 1
                        sumL1 = sumL1 + math.sqrt(initMatrix[i][j]['g'] * initMatrix[(i + length - 2) % length][j]['s'] / 4)
                    if (isCal != 0):
                        L1 = sumL1 / n
                    else:
                        if (initMatrix[(i + 1) % width][(j + 2) % width]['value'] == 2):
                            isCal = 1
                            n = n + 1
                            sumL1 = sumL1 + math.sqrt(
                                initMatrix[i][j]['g'] * initMatrix[(i + 1) % width][(j + 2) % width]['s'] / 5)
                        if (initMatrix[(i + length - 1) % width][(j + 2) % width]['value'] == 2):
                            isCal = 1
                            n = n + 1
                            sumL1 = sumL1 + math.sqrt(
                                initMatrix[i][j]['g'] * initMatrix[(i + length - 1) % width][(j + 2) % width]['s'] / 5)
                        if (initMatrix[(i + 1) % width][(j + length - 2) % width]['value'] == 2):
                            isCal = 1
                            n = n + 1
                            sumL1 = sumL1 + math.sqrt(
                                initMatrix[i][j]['g'] * initMatrix[(i + 1) % width][(j + length - 2) % width]['s'] / 5)
                        if (initMatrix[(i + length - 1) % width][(j + length - 2) % width]['value'] == 2):
                            isCal = 1
                            n = n + 1
                            sumL1 = sumL1 + math.sqrt(
                                initMatrix[i][j]['g'] * initMatrix[(i + length - 1) % width][(j + length - 2) % width]['s'] / 5)
                        if (initMatrix[(i + 2) % width][(j + 1) % width]['value'] == 2):
                            isCal = 1
                            n = n + 1
                            sumL1 = sumL1 + math.sqrt(
                                initMatrix[i][j]['g'] * initMatrix[(i + 2) % width][(j + 1) % width]['s'] / 5)
                        if (initMatrix[(i + length - 2) % width][(j + 1) % width]['value'] == 2):
                            isCal = 1
                            n = n + 1
                            sumL1 = sumL1 + math.sqrt(
                                initMatrix[i][j]['g'] * initMatrix[(i + length - 2) % width][(j + 1) % width]['s'] / 5)
                        if (initMatrix[(i + 2) % width][(j + length - 1) % width]['value'] == 2):
                            isCal = 1
                            n = n + 1
                            sumL1 = sumL1 + math.sqrt(
                                initMatrix[i][j]['g'] * initMatrix[(i + 2) % width][(j + length - 1) % width]['s'] / 5)
                        if (initMatrix[(i + length - 2) % width][(j + length - 1) % width]['value'] == 2):
                            isCal = 1
                            n = n + 1
                            sumL1 = sumL1 + math.sqrt(
                                initMatrix[i][j]['g'] * initMatrix[(i + length - 2) % width][(j + length - 1) % width]['s'] / 5)
                        if (isCal != 0):
                            L1 = sumL1 / n
                        else:
                            if (initMatrix[(i + 2) % width][(j + 2) % width]['value'] == 2):
                                isCal = 1
                                n = n + 1
                                sumL1 = sumL1 + math.sqrt(
                                    initMatrix[i][j]['g'] * initMatrix[(i + 2) % width][(j + 2) % width]['s'] / 8)
                            if (initMatrix[(i + length - 2) % width][(j + 2) % width]['value'] == 2):
                                isCal = 1
                                n = n + 1
                                sumL1 = sumL1 + math.sqrt(
                                    initMatrix[i][j]['g'] * initMatrix[(i + length - 2) % width][(j + 2) % width]['s'] / 8)
                            if (initMatrix[(i + 2) % width][(j + length - 2) % width]['value'] == 2):
                                isCal = 1
                                n = n + 1
                                sumL1 = sumL1 + math.sqrt(
                                    initMatrix[i][j]['g'] * initMatrix[(i + 2) % width][(j + length - 2) % width]['s'] / 8)
                            if (initMatrix[(i + length - 2) % width][(j + length - 2) % width]['value'] == 2):
                                isCal = 1
                                n = n + 1
                                sumL1 = sumL1 + math.sqrt(
                                    initMatrix[i][j]['g'] * initMatrix[(i + length - 2) % width][(j + length - 2) % width]['s'] / 8)
                            if (isCal != 0):
                                L1 = sumL1 / n
                            else:
                                L1 = 0
            # 计算L2
            L2 = 0
            sMax = 0
            position = [-1, -1]
            for k1 in range(0, 5):
                for k2 in range(0, 5):
                    if (initMatrix[(i + k1 + length - 2) % length][(j + k2 + length - 2) % width]['value'] == 2):
                        if (initMatrix[(i + k1 + length - 2) % length][(j + k2 + length - 2) % width]['s'] > sMax):
                            sMax = initMatrix[(i + k1 + length - 2) % length][(j + k2 + length - 2) % width]['s']
                            position = [k1, k2]
            if (sMax != 0 and (position[0] != 2 or position[1] != 2)):
                L2 = math.sqrt(
                    initMatrix[i][j]['g'] * initMatrix[(i + k1 + length - 2) % length][(j + k2 + length - 2) % width]['s'] / (
                                math.pow((position[0] - 2), 2) + math.pow((position[1] - 2), 2)))
            # 计算L3
            L3 = 0
            for k1 in range(0, 5):
                for k2 in range(0, 5):
                    if (initMatrix[(i + k1 + length - 2) % length][(j + k2 + length - 2) % width]['value'] == 2 and (
                            k1 != 2 or k2 != 2)):
                        temp = math.sqrt(
                            initMatrix[i][j]['g'] * initMatrix[(i + k1 + length - 2) % length][(j + k2 + length - 2) % width]['s'] / (
                                        math.pow((k1 - 2), 2) + math.pow((k2 - 2), 2)))
                        if (temp > L3):
                            L3 = temp
            # 计算a
            lList = [L1, L2, L3]
            avg = (L1 + L2 + L3) / 3
            aMax = max(lList)
            aMin = min(lList)
            if ((aMax - aMin) != 0):
                transitionMatrix[i][j]['a1'] = (avg - aMin) / (aMax - aMin)
                transitionMatrix[i][j]['a2'] = 1 - (avg - aMin) / (aMax - aMin)
            else:
                transitionMatrix[i][j]['a1'] = 0
            # 更新b1,b2，y
            transitionMatrix[i][j]['b1'] = pow(initMatrix[i][j]['b1'], 1/(initMatrix[i][j]['count'] + 1))
            transitionMatrix[i][j]['b2'] = pow(initMatrix[i][j]['b2'], initMatrix[i][j]['count'] + 1)
            transitionMatrix[i][j]['y'] = pow(initMatrix[i][j]['y'], 1/(initMatrix[i][j]['keep'] + 1))

def cellularAutomata(gauss):
    # 防止边缘扩撒
    originalValue = 100  # 初始时2占比


    # 初始化元胞矩阵
    for i in range(0, length):
        tmp = []
        for j in range(0, width):
            b = random.randint(0, 100)
            tmp.append({'value': 0, 'g': random.gauss(gauss, 0.01), 's': random.gauss(gauss, 0.01), 'b1': b / 100,
                        'b2': random.randint(0, 100 - b) / 100, 'count': 0, 'y': 0, 'keep': 0})
        initMatrix.append(tmp)
    slice = random.sample(range(0, 10000), originalValue)
    for k in range(0, originalValue):
        initMatrix[int(slice[k] / 100 + (length - 100) // 2)][slice[k] % 100 + (length - 100) // 2]['value'] = 2

    for i in range(0, length):
        tmp = []
        for j in range(0, width):
            # 计算L1
            L1 = 0
            isCal = 0  # 是否出现最近的选项
            n = 0  # 同一距离中点的数量
            sumL1 = 0  # 方便求平均值
            if (initMatrix[i][(j + 1) % width]['value'] == 2):
                isCal = 1
                n = n + 1
                sumL1 = sumL1 + math.sqrt(initMatrix[i][j]['g'] * initMatrix[i][(j + 1) % width]['s'])
            if (initMatrix[i][(j + length - 1) % width]['value'] == 2):
                isCal = 1
                n = n + 1
                sumL1 = sumL1 + math.sqrt(initMatrix[i][j]['g'] * initMatrix[i][(j + length - 1) % width]['s'])
            if (initMatrix[(i + 1) % length][j]['value'] == 2):
                isCal = 1
                n = n + 1
                sumL1 = sumL1 + math.sqrt(initMatrix[i][j]['g'] * initMatrix[(i + 1) % length][j]['s'])
            if (initMatrix[(i + length - 1) % length][j]['value'] == 2):
                isCal = 1
                n = n + 1
                sumL1 = sumL1 + math.sqrt(initMatrix[i][j]['g'] * initMatrix[(i + length - 1) % length][j]['s'])
            if (isCal != 0):
                L1 = sumL1 / n
            else:
                if (initMatrix[(i + 1) % width][(j + 1) % width]['value'] == 2):
                    isCal = 1
                    n = n + 1
                    sumL1 = sumL1 + math.sqrt(
                        initMatrix[i][j]['g'] * initMatrix[(i + 1) % width][(j + 1) % width]['s'] / 2)
                if (initMatrix[(i + length - 1) % width][(j + 1) % width]['value'] == 2):
                    isCal = 1
                    n = n + 1
                    sumL1 = sumL1 + math.sqrt(
                        initMatrix[i][j]['g'] * initMatrix[(i + length - 1) % width][(j + 1) % width]['s'] / 2)
                if (initMatrix[(i + 1) % width][(j + length - 1) % width]['value'] == 2):
                    isCal = 1
                    n = n + 1
                    sumL1 = sumL1 + math.sqrt(
                        initMatrix[i][j]['g'] * initMatrix[(i + 1) % width][(j + length - 1) % width]['s'] / 2)
                if (initMatrix[(i + length - 1) % width][(j + length - 1) % width]['value'] == 2):
                    isCal = 1
                    n = n + 1
                    sumL1 = sumL1 + math.sqrt(
                        initMatrix[i][j]['g'] * initMatrix[(i + length - 1) % width][(j + length - 1) % width]['s'] / 2)
                if (isCal != 0):
                    L1 = sumL1 / n
                else:
                    if (initMatrix[i][(j + 2) % width]['value'] == 2):
                        isCal = 1
                        n = n + 1
                        sumL1 = sumL1 + math.sqrt(initMatrix[i][j]['g'] * initMatrix[i][(j + 2) % width]['s'] / 4)
                    if (initMatrix[i][(j + length - 2) % width]['value'] == 2):
                        isCal = 1
                        n = n + 1
                        sumL1 = sumL1 + math.sqrt(
                            initMatrix[i][j]['g'] * initMatrix[i][(j + length - 2) % width]['s'] / 4)
                    if (initMatrix[(i + 2) % length][j]['value'] == 2):
                        isCal = 1
                        n = n + 1
                        sumL1 = sumL1 + math.sqrt(initMatrix[i][j]['g'] * initMatrix[(i + 2) % length][j]['s'] / 4)
                    if (initMatrix[(i + length - 2) % length][j]['value'] == 2):
                        isCal = 1
                        n = n + 1
                        sumL1 = sumL1 + math.sqrt(
                            initMatrix[i][j]['g'] * initMatrix[(i + length - 2) % length][j]['s'] / 4)
                    if (isCal != 0):
                        L1 = sumL1 / n
                    else:
                        if (initMatrix[(i + 1) % width][(j + 2) % width]['value'] == 2):
                            isCal = 1
                            n = n + 1
                            sumL1 = sumL1 + math.sqrt(
                                initMatrix[i][j]['g'] * initMatrix[(i + 1) % width][(j + 2) % width]['s'] / 5)
                        if (initMatrix[(i + length - 1) % width][(j + 2) % width]['value'] == 2):
                            isCal = 1
                            n = n + 1
                            sumL1 = sumL1 + math.sqrt(
                                initMatrix[i][j]['g'] * initMatrix[(i + length - 1) % width][(j + 2) % width]['s'] / 5)
                        if (initMatrix[(i + 1) % width][(j + length - 2) % width]['value'] == 2):
                            isCal = 1
                            n = n + 1
                            sumL1 = sumL1 + math.sqrt(
                                initMatrix[i][j]['g'] * initMatrix[(i + 1) % width][(j + length - 2) % width]['s'] / 5)
                        if (initMatrix[(i + length - 1) % width][(j + length - 2) % width]['value'] == 2):
                            isCal = 1
                            n = n + 1
                            sumL1 = sumL1 + math.sqrt(
                                initMatrix[i][j]['g'] * initMatrix[(i + length - 1) % width][(j + length - 2) % width][
                                    's'] / 5)
                        if (initMatrix[(i + 2) % width][(j + 1) % width]['value'] == 2):
                            isCal = 1
                            n = n + 1
                            sumL1 = sumL1 + math.sqrt(
                                initMatrix[i][j]['g'] * initMatrix[(i + 2) % width][(j + 1) % width]['s'] / 5)
                        if (initMatrix[(i + length - 2) % width][(j + 1) % width]['value'] == 2):
                            isCal = 1
                            n = n + 1
                            sumL1 = sumL1 + math.sqrt(
                                initMatrix[i][j]['g'] * initMatrix[(i + length - 2) % width][(j + 1) % width]['s'] / 5)
                        if (initMatrix[(i + 2) % width][(j + length - 1) % width]['value'] == 2):
                            isCal = 1
                            n = n + 1
                            sumL1 = sumL1 + math.sqrt(
                                initMatrix[i][j]['g'] * initMatrix[(i + 2) % width][(j + length - 1) % width]['s'] / 5)
                        if (initMatrix[(i + length - 2) % width][(j + length - 1) % width]['value'] == 2):
                            isCal = 1
                            n = n + 1
                            sumL1 = sumL1 + math.sqrt(
                                initMatrix[i][j]['g'] * initMatrix[(i + length - 2) % width][(j + length - 1) % width][
                                    's'] / 5)
                        if (isCal != 0):
                            L1 = sumL1 / n
                        else:
                            if (initMatrix[(i + 2) % width][(j + 2) % width]['value'] == 2):
                                isCal = 1
                                n = n + 1
                                sumL1 = sumL1 + math.sqrt(
                                    initMatrix[i][j]['g'] * initMatrix[(i + 2) % width][(j + 2) % width]['s'] / 8)
                            if (initMatrix[(i + length - 2) % width][(j + 2) % width]['value'] == 2):
                                isCal = 1
                                n = n + 1
                                sumL1 = sumL1 + math.sqrt(
                                    initMatrix[i][j]['g'] * initMatrix[(i + length - 2) % width][(j + 2) % width][
                                        's'] / 8)
                            if (initMatrix[(i + 2) % width][(j + length - 2) % width]['value'] == 2):
                                isCal = 1
                                n = n + 1
                                sumL1 = sumL1 + math.sqrt(
                                    initMatrix[i][j]['g'] * initMatrix[(i + 2) % width][(j + length - 2) % width][
                                        's'] / 8)
                            if (initMatrix[(i + length - 2) % width][(j + length - 2) % width]['value'] == 2):
                                isCal = 1
                                n = n + 1
                                sumL1 = sumL1 + math.sqrt(initMatrix[i][j]['g'] * initMatrix[(i + length - 2) % width][
                                    (j + length - 2) % width]['s'] / 8)
                            if (isCal != 0):
                                L1 = sumL1 / n
                            else:
                                L1 = 0
            # 计算L2
            L2 = 0
            sMax = 0
            position = [-1, -1]
            for k1 in range(0, 5):
                for k2 in range(0, 5):
                    if (initMatrix[(i + k1 + length - 2) % length][(j + k2 + length - 2) % width]['value'] == 2):
                        if (initMatrix[(i + k1 + length - 2) % length][(j + k2 + length - 2) % width]['s'] > sMax):
                            sMax = initMatrix[(i + k1 + length - 2) % length][(j + k2 + length - 2) % width]['s']
                            position = [k1, k2]
            if (sMax != 0 and (position[0] != 2 or position[1] != 2)):
                L2 = math.sqrt(
                    initMatrix[i][j]['g'] * initMatrix[(i + k1 + length - 2) % length][(j + k2 + length - 2) % width][
                        's'] / (math.pow((position[0] - 2), 2) + math.pow((position[1] - 2), 2)))
            # 计算L3
            L3 = 0
            for k1 in range(0, 5):
                for k2 in range(0, 5):
                    if (initMatrix[(i + k1 + length - 2) % length][(j + k2 + length - 2) % width]['value'] == 2 and (
                            k1 != 2 or k2 != 2)):
                        temp = math.sqrt(initMatrix[i][j]['g'] *
                                         initMatrix[(i + k1 + length - 2) % length][(j + k2 + length - 2) % width][
                                             's'] / (math.pow((k1 - 2), 2) + math.pow((k2 - 2), 2)))
                        if (temp > L3):
                            L3 = temp
            # 计算a
            lList = [L1, L2, L3]
            avg = (L1 + L2 + L3) / 3
            aMax = max(lList)
            aMin = min(lList)
            if ((aMax - aMin) != 0):
                a = (avg - aMin) / (aMax - aMin)
            else:
                a = 0
            # 计算b1,b2
            b1 = pow(initMatrix[i][j]['b1'], 1 / (initMatrix[i][j]['count'] + 1))
            b2 = pow(initMatrix[i][j]['b2'], initMatrix[i][j]['count'] + 1)
            # 更新initMatrix中y的值
            if ((L1 + L2 + L3) != 0):
                initMatrix[i][j]['y'] = L3 / (L1 + L2 + L3)
            else:
                initMatrix[i][j]['y'] = 0
            # 计算y
            y = pow(initMatrix[i][j]['y'], 1 / (initMatrix[i][j]['keep'] + 1))
            tmp.append({'L1': L1, 'L2': L2, 'L3': L3, 'a1': a, 'a2': 1 - a, 'b1': b1, 'b2': b2, 'y': y})
        transitionMatrix.append(tmp)

    zero = np.zeros((t,), dtype=int)
    one = np.zeros((t,), dtype=int)
    two = np.zeros((t,), dtype=int)
    three = np.zeros((t,), dtype=int)

    # 按轮数进行迭代
    for k in range(0, t):
        #     # 画图
        #     cell = np.zeros((100, 100), int)
        #     for i in range(50, length - 50):
        #         for j in range(50, width - 50):
        #             cell[i-50][j-50] = initMatrix[i][j]['value']
        #     plt.imshow(cell, vmin=0, vmax=3)
        #     plt.colorbar()
        #     plt.savefig('plot出图/100出图/图{}.png'.format(k))
        #     plt.show()

        key0 = 0
        key1 = 0
        key2 = 0
        key3 = 0
        for i in range(50, 150):
            for j in range(50, 150):
                if (initMatrix[i][j]['value'] == 0):
                    key0 += 1
                if (initMatrix[i][j]['value'] == 1):
                    key1 += 1
                if (initMatrix[i][j]['value'] == 2):
                    key2 += 1
                if (initMatrix[i][j]['value'] == 3):
                    key3 += 1

        zero[k] = key0
        one[k] = key1
        two[k] = key2
        three[k] = key3

        sumB1 = 0
        count2 = 0
        for i in range(0, length):
            for j in range(0, width):
                if (initMatrix[i][j]['value'] == 3):
                    sumB1 += transitionMatrix[i][j]['y']
                    count2 += 1
        if (count2 == 0):
            count2 = 1
        avgB1 = sumB1 / count2

        sumB2 = 0
        count3 = 0
        for i in range(0, length):
            for j in range(0, width):
                if (initMatrix[i][j]['value'] == 3):
                    sumB2 += transitionMatrix[i][j]['y']
                    count3 += 1
        if (count3 == 0):
            count3 = 1
        avgB2 = sumB2 / count3

        sumY = 0
        count1 = 0
        for i in range(0, length):
            for j in range(0, width):
                if (initMatrix[i][j]['value'] == 3):
                    sumY += transitionMatrix[i][j]['y']
                    count1 += 1
        if (count1 == 0):
            count1 = 1
        avgY = sumY / count1

        # 更新
        for i in range(0, length):
            for j in range(0, width):
                if (initMatrix[i][j]['value'] == 0):
                    if (transitionMatrix[i][j]['a1'] == 0):
                        initMatrix[i][j]['value'] = 0
                    else:
                        if (transitionMatrix[i][j]['a1'] > transitionMatrix[i][j]['a2']):
                            initMatrix[i][j]['value'] = 1
                        else:
                            initMatrix[i][j]['value'] = 2
                elif (initMatrix[i][j]['value'] == 1):
                    # if(transitionMatrix[i][j]['b1']>transitionMatrix[i][j]['b2'] and transitionMatrix[i][j]['b1']>(1-transitionMatrix[i][j]['b1']-transitionMatrix[i][j]['b2'])):
                    #     initMatrix[i][j]['value'] = 2
                    # elif(transitionMatrix[i][j]['b2']>transitionMatrix[i][j]['b1'] and transitionMatrix[i][j]['b2']>(1-transitionMatrix[i][j]['b1']-transitionMatrix[i][j]['b2'])):
                    #     initMatrix[i][j]['value'] = 3
                    if (transitionMatrix[i][j]['b1'] > avgB1):
                        initMatrix[i][j]['value'] = 2
                    elif (transitionMatrix[i][j]['b2'] > avgB2):
                        initMatrix[i][j]['value'] = 3
                elif (initMatrix[i][j]['value'] == 3):
                    if (transitionMatrix[i][j]['y'] > avgY - 0.01):
                        initMatrix[i][j]['value'] = 1
                        initMatrix[i][j]['count'] += 1
                        initMatrix[i][j]['keep'] = initMatrix[i][j]['count']
                    else:
                        initMatrix[i][j]['keep'] += 1
        updateTransMatrix()

    return [zero, one, two, three]


if __name__ == '__main__':
    length = 200
    width = 200
    initMatrix = []
    transitionMatrix = []
    t = 30  # 变化轮数
    a = cellularAutomata(0.5)
    initMatrix = []
    transitionMatrix = []
    b = cellularAutomata(0.7)
    initMatrix = []
    transitionMatrix = []
    c = cellularAutomata(0.9)


    plt.title("I Changes")
    plt.xlabel('t')
    plt.ylabel('i(t)')
    plt.plot(range(0, t), a[0], marker='^', color='#44045a', label='5-0')
    plt.plot(range(0, t), a[1], marker='^', color='#30688d', label='5-1')
    plt.plot(range(0, t), a[2], marker='^', color='#35b775', label='5-2')
    plt.plot(range(0, t), a[3], marker='^', color='#f8e620', label='5-3')
    plt.plot(range(0, t), b[0], marker='p', color='#44045a', label='7-0')
    plt.plot(range(0, t), b[1], marker='p', color='#30688d', label='7-1')
    plt.plot(range(0, t), b[2], marker='p', color='#35b775', label='7-2')
    plt.plot(range(0, t), b[3], marker='p', color='#f8e620', label='7-3')
    # plt.plot(range(0, t), c[0], marker='s', color='#44045a', label='9-0')
    # plt.plot(range(0, t), c[1], marker='s', color='#30688d', label='9-1')
    # plt.plot(range(0, t), c[2], marker='s', color='#35b775', label='9-2')
    # plt.plot(range(0, t), c[3], marker='s', color='#f8e620', label='9-3')
    plt.show()

