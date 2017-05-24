# 낮과 밤의 속도의 차이 plotting

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data2.txt')

day, night = data.T
print("day - night:", day-night)
print("|day - night|:", abs(day-night))

ID = np.arange(1, len(day)+1)

plt.plot(ID, day-night, 'k.') # 양과 음의 값
plt.title("Distribution of day-night")
plt.xlabel('ID')
plt.ylabel('day-night')
plt.text(20.5, -29, "* = day-night \no = |day-night|")
plt.plot(ID, abs(day-night), 'y*') # 절댓값 처리 
plt.show()
