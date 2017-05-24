# 남자와 여자의 콜레스테롤 양 데이터 기본 plotting

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data1.txt')

male, female = data.T
print("male:", male)
print("female:", female)

ID = np.arange(1, len(male)+1)

plt.plot(ID, male, '^')
plt.title("Distribution of male and female")
plt.xlabel('ID')
plt.ylabel('male \n female')
plt.text(14.5, 0.5, "^ = male \n* = female")
plt.plot(ID, female, '*')
plt.show()
