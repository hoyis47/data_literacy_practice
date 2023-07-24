import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# plt.rcParams['axes.unicode_minus']=False
# plt.rcParams['font.family']="D2Coding ligature"
# plt.rcParams['figure.figsize']=(10,8)

# plt.plot(np.arange(10), np.arange(10)*2)
# plt.plot(np.arange(10),np.arange(10)**2)
# plt.plot(np.arange(10), np.log(np.arange(10)))

# plt.title("범례설정", fontsize=20)

# plt.xlabel('X축', fontsize=20)
# plt.ylabel('Y축',fontsize=20)

# plt.xticks(rotation=90)
# plt.yticks(rotation=30)

# plt.legend(['10 * 2', '10 ** 2', 'log'], fontsize=15)

# plt.show()

df = pd.read_csv('https://bit.ly/2Vk0zLr')
print(df.head())


s = df['분양가'].plot(kind='line')
plt.show()

