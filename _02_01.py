# 낮과 밤의 속도 데이터 기본 plotting

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data2.txt')

day, night = data.T
print("day:", day)
print("night:", night)

ID = np.arange(1, len(day)+1)

plt.plot(ID, day, 'm.')
plt.title("Distribution of day and night")
plt.xlabel('ID')
plt.ylabel('day \n night')
plt.text(20.5, 95, "o = day \n+ = night")
plt.plot(ID, night, '+')
plt.show()
