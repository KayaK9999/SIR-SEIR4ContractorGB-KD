import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt



def SIR_model(y, t, a, b, v, lamuda, e):
    S, I, R = y
    dS_dt = -a * S - e*S+v*I+lamuda*R
    dI_dt = a * S - v * I-b*I
    dR_dt = b * I +e*S-lamuda*R
    return ([dS_dt, dI_dt, dR_dt])
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    S0 = 0.950  # ratio
    I0 = 0.05  # ratio
    R0 = 0 # ratio
    a = 0.75
    b = 0.4
    v = 0.3
    lamuda = 0.6
    e = 0.15

    # time vector
    t = np.linspace(0, 10, 10000)
    # result
    res1 = scipy.integrate.odeint(SIR_model, [S0, I0, R0], t, args=(a,b,v,lamuda,e))
    res1 = np.array(res1)

    # S0 = 0.125  # ratio
    # I0 = 0.25# ratio
    # R0 = 0.625  # ratio
    # a = 0.65
    # b = 0.1
    # v = 0.06
    # lamuda = 0.3
    # e = 0.12
    #
    # # time vector
    # t = np.linspace(0, 10, 10000)
    # # result
    # res2 = scipy.integrate.odeint(SIR_model, [S0, I0, R0], t, args=(a,b,v,lamuda,e))
    # res2 = np.array(res2)



    # plot
    plt.figure(figsize=[18, 12])
    plt.plot(t, res1[:, 0], linewidth=8.0,label='S(t)', color='blue')
    plt.plot(t, res1[:, 1], linewidth=8.0,label='I (t)', color='green')
    plt.plot(t, res1[:, 2], linewidth=8.0,label='R(t)', color='orange')

    # plt.plot(t, res2[:, 0], label='S(t)',color='blue')
    # plt.plot(t, res2[:, 1], label='I (t)',color='green')
    # plt.plot(t, res2[:, 2], label='R(t)',color='orange')



    # plt.text(10.25, res8[9999, 2] + 0.008, "30", color='black')
    # plt.text(10.5, res6[9999, 0], chr(949).lower() + "= 0.20", color='black', fontsize=12)

    plt.legend(loc='upper right')
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.grid()
    plt.xlabel('time',fontsize=20)
    plt.ylabel('proporty',fontsize=20)
    #前4组
    #plt.title('Start: Bold line: S = 0.95, I = 0.05, R = 0; Thin line: S = 0.65, I = 0.35, R = 0\nEnd: Bold line: S = '+"%.2f" % (res1[9999, 0])+ ', I = '+"%.2f" % (res1[9999, 1])+ ', R = '+"%.2f" % (res1[9999, 2])+'; Thin line: S = '+"%.2f" % (res2[9999, 0])+ ', I = '+"%.2f" % (res2[9999, 1])+ ', R = '+"%.2f" % (res2[9999, 2]),fontsize=20)
    #5-9组
    #plt.title('Start: S = 0.95, I = 0.05, R = 0, bold line: α = 0.65; thin line: α = 0.85\nEnd: Bold line: S = '+"%.2f" % (res1[9999, 0])+ ', I = '+"%.2f" % (res1[9999, 1])+ ', R = '+"%.2f" % (res1[9999, 2])+'; Thin line: S = '+"%.2f" % (res2[9999, 0])+ ', I = '+"%.2f" % (res2[9999, 1])+ ', R = '+"%.2f" % (res2[9999, 2]),fontsize=20)
    #10组
    plt.title('Start: S = 0.95, I = 0.05, R = 0, α = 0.75, ß = 0.4, γ = 0.3, λ = 0.6, ε = 0.15\nEnd: S = '+"%.2f" % (res1[9999, 0])+ ', I = '+"%.2f" % (res1[9999, 1])+ ', R = '+"%.2f" % (res1[9999, 2]),fontsize=20)
    plt.show()



