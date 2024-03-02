import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from scipy.integrate import odeint
from scipy.interpolate import interp1d


def dySEIR(y, t, alpha1, alpha2, beta1, beta2, gamma):  # SEIR 模型，导数函数
    s, e, i, r = y  # youcans
    ds_dt = -alpha1*s*i - alpha2*s*i  # ds/dt = -alpha1*s*i
    de_dt = alpha1*s*i - beta1*e - beta2*e  # de/dt = alpha1*s*i - alpha2*e
    di_dt = alpha2*s*i + beta1*e - gamma*i  # di/dt = alpha2*e - beta1*i
    dr_dt = beta2*e + gamma * i
    return np.array([ds_dt, de_dt, di_dt, dr_dt])

def to_percent(temp, position):
  return '%1.0f'%(100*temp) + '%'


if __name__=="__main__":
    # 设置模型参数
    number = 1000  # 总人数

    tEnd =21  # 预测日期长度
    t = np.arange(0.0, tEnd, 1)  # (start,stop,step)
    i0 = 1  # 患病者比例的初值
    e0 = 0  # 潜伏者比例的初值
    s0 = 999 # 易感者比例的初值
    r0 = 0
    Y0 = (s0, e0, i0, r0)  # 微分方程组的初值

    ySEIR1 = odeint(dySEIR, Y0, t, args=(0.11, 0.89, 0.05, 0.95, 0.23))  # SEIR 模型
    ySEIR2 = odeint(dySEIR, Y0, t, args=(0.72, 0.28, 0.05, 0.95, 0.23))  # SEIR 模3
    ySEIR3 = odeint(dySEIR, Y0, t, args=(0.31, 0.69, 0.87, 0.13, 0.23))  # SEIR 模型
    ySEIR4 = odeint(dySEIR, Y0, t, args=(0.72, 0.28, 0.87, 0.13, 0.23))  # SEIR 模型
    ySEIR5 = odeint(dySEIR, Y0, t, args=(0.72, 0.28, 0.87, 0.13, 0.67))  # SEIR 模型

    # 输出绘图

    # plt.title("α1={}, α2={}, β1={}, β2={}, γ={}".format(0.11, 0.89, 0.05, 0.95, 0.23))
    plt.title("I Changes")
    plt.xlabel('t')
    plt.ylabel('i(t)')
    plt.axis([0, tEnd, 0, 0.8])
    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
    cubic_interploation_model = interp1d(t, ySEIR1[:, 2], kind="cubic")
    xs1 = np.linspace(0, 20, 500)
    ys1 = cubic_interploation_model(xs1)
    cubic_interploation_model = interp1d(t, ySEIR2[:, 2], kind="cubic")
    xs2 = np.linspace(0, 20, 500)
    ys2 = cubic_interploation_model(xs2)
    cubic_interploation_model = interp1d(t, ySEIR3[:, 2], kind="cubic")
    xs3 = np.linspace(0, 20, 500)
    ys3 = cubic_interploation_model(xs3)
    cubic_interploation_model = interp1d(t, ySEIR4[:, 2], kind="cubic")
    xs4 = np.linspace(0, 20, 500)
    ys4 = cubic_interploation_model(xs4)
    cubic_interploation_model = interp1d(t, ySEIR5[:, 2], kind="cubic")
    xs5 = np.linspace(0, 20, 500)
    ys5 = cubic_interploation_model(xs5)
    #
    # # ffffb2#fecc5c#fd8d3c#f03b20#bd0026
    plt.plot(xs1, ys1 / number, color='#f1eef6', label='1')
    plt.plot(xs2, ys2 / number, color='#bdc9e1', label='2')
    plt.plot(xs3, ys3 / number, color='#74a9cf', label='3')
    plt.plot(xs4, ys4 / number, color='#2b8cbe', label='4')
    plt.plot(xs5, ys5 / number, color='#045a8d', label='5')
    #
    # plt.plot(t, ySEIR1[:, 0]/number,color='#feebe2', label='1')
    # plt.plot(t, ySEIR2[:, 0]/number,color='#fbb4b9', label='2')
    # plt.plot(t, ySEIR3[:, 0]/number,color='#f768a1', label='3')
    # plt.plot(t, ySEIR4[:, 0]/number,color='#c51b8a', label='4')
    # plt.plot(t, ySEIR5[:, 0]/number,color='#7a0177', label='5')


    plt.legend(loc='right')  # youcans
    plt.show()
