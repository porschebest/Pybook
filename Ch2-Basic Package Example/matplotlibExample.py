# -*- coding: utf-8 -*
import numpy as np
import matplotlib.pyplot as plt

#解决中文标签问题，手动指定默认字体
plt.rcParams['font.sans-serif'] = ['SimHei']

#保存图像，负号显示问题
plt.rcParams['axes.unicode_minus'] = False

#作图变量的自变量
x = np.linspace(0, 10, 1000)
y = np.sin(x) + 1
z = np.cos(x**2) + 1

plt.figure(figsize = (8,4))

#作图，设置标签，线条颜色，线条大小
plt.plot(x,y,label = '$\sin x+1$', color = 'red', linewidth = 2)

#作图，线条类型，设置标签
plt.plot(x,z, 'b--', label = '$\cos x^2+1$')

#x轴名称
plt.xlabel('Time(s)')
#y轴名称
plt.ylabel('Volt')
plt.title('A simple Matplotlib Example')

#y轴限制
plt.ylim(0, 2.2)

#显示图例
plt.legend()

#显示结果
plt.show()

#保存图像
fig = plt.plot(x,y,label = '$\sin x+1$', color = 'red', linewidth = 2)
fig = plt.plot(x,z, 'b--', label = '$\cos x^2+1$')
plt.savefig('Matplotlib_SinCosExample.png')
