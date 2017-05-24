# 남자와 여자의 콜레스테롤 양의 차이 plotting

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data1.txt')

male, female = data.T
print("male - female:", male-female)
print("|male - female|:", abs(male-female))

ID = np.arange(1, len(male)+1)

plt.plot(ID, male-female, 'yo') # 양과 음의 값
plt.title("Distribution of male-female")
plt.xlabel('ID')
plt.ylabel('male-female')
plt.text(14.5, -1.5, "o = male-female \n* = |male-female|")
plt.plot(ID, abs(male-female), 'c*') # 절댓값 처리 
plt.show()
