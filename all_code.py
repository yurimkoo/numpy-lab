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
