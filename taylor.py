'''
已知：f(x0)和f(x0)的k阶导函数值
未知：f(x)和f(x)的k阶导函数表达式
需求：任意x近似计算f(x)
知识点：
1、f(x)函数值的taylor公式近似逼近
2、递归求解f(x0)的k阶导函数值
'''
import numpy as np
import matplotlib.pyplot as plt
from math import factorial
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def fx(x):
    return 2 * np.sin(x) + x
'''递归求fx的高阶导函数值'''
def dfx(x, h=0.001, deep=1):
    if deep == 1:
        return (fx(x=x + h) - fx(x=x - h)) / (2 * h)
    else:
        return (dfx(x=x + h, h=h, deep=deep-1) - dfx(x=x - h, h=h, deep=deep-1)) / (2 * h)
'''计算fx的N阶泰勒公式函数值'''
def taylorFx(xs, N=2):
    x0, h, ys = 0, 0.1, []
    for x in xs:
        dx, taylorValues = x - x0, 0
        for k in range(1, N + 1):
            taylorValues += 1 / factorial(k) * dfx(x=x0, h=h, deep=k) * (dx ** k)
        ys.append(fx(x=x0) + taylorValues)
    return ys
def draw():
    xs = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    fig = plt.figure()
    for i in range(1, 17):
        ax1 = fig.add_subplot(4, 4, i)
        ax1.plot(xs, fx(xs), color='#4876FF', linestyle='', marker='.', markersize=6, label='fx')
        ax1.plot(xs, taylorFx(xs=xs, N=i+1), color='#EE2C2C', label='taylor N={}'.format(i+1))
        ax1.legend()
    plt.show()
if __name__ == '__main__':
    draw()
