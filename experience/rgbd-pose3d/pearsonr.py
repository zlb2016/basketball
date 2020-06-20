import numpy as np
from scipy.stats import pearsonr
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cosine
from sklearn.preprocessing import StandardScaler
import scipy
 
# 设定向量长度，均为100
n = 2
# x = scipy.array([-60.70762, 403.8008, 109.0549])
# y = scipy.array([19.21995, 377.59323, 992.2105])
x = scipy.array([1, 2, 3])
y = scipy.array([2, 4, 6])

r_row, p_value = pearsonr(x, y)
print('r_row',round(r_row,2))#皮尔逊相关系数
# print(pearsonr(x, y))
# # x3 = [[19], [377], [992]]
# x_=x-np.mean(x)
# y_=y-np.mean(y)
# d1=np.dot(x_,y_)/(np.linalg.norm(x_)*np.linalg.norm(y_))
# print('d1',d1)

# print('x1',pearsonr(x1, x2))
# print('x2',x2)
# print('x3',x3)
 
# p12 = 1 - pearsonr(x1, x2)[0]
# p13 = 1 - pearsonr(x1, x3)[0]
# p23 = 1 - pearsonr(x2, x3)[0]
 
# d12 = (euclidean(x1, x2) ** 2) / (2 * n)
# d13 = (euclidean(x1, x3) ** 2) / (2 * n)
# d23 = (euclidean(x2, x3) ** 2) / (2 * n)
 
# c12 = cosine(x1, x2)
# c13 = cosine(x1, x3)
# c23 = cosine(x2, x3)
 
# print('原始数据，没有标准化')
# print('             x1&x2  x2&x3  x1&x3')
# print('pearson:    ', np.round(p12, decimals=4), np.round(p13, decimals=4),
#       np.round(p23, decimals=4))
# print('cos:        ', np.round(c12, decimals=4), np.round(c13, decimals=4),
#       np.round(c23, decimals=4))
# print('euclidean sq', np.round(d12, decimals=4), np.round(d13, decimals=4),
#       np.round(d23, decimals=4))
 
# # 标准化后的数据
# x1_n = StandardScaler().fit_transform(x1)
# x2_n = StandardScaler().fit_transform(x2)
# x3_n = StandardScaler().fit_transform(x3)
 
# p12_n = 1 - pearsonr(x1_n, x2_n)[0][0]
# p13_n = 1 - pearsonr(x1_n, x3_n)[0][0]
# p23_n = 1 - pearsonr(x2_n, x3_n)[0][0]
 
# d12_n = (euclidean(x1_n, x2_n) ** 2) / (2 * n)
# d13_n = (euclidean(x1_n, x3_n) ** 2) / (2 * n)
# d23_n = (euclidean(x2_n, x3_n) ** 2) / (2 * n)
 
# c12_n = cosine(x1_n, x2_n)
# c13_n = cosine(x1_n, x3_n)
# c23_n = cosine(x2_n, x3_n)
 
# print('标准化后的数据: 均值=0，标准差=1')
# print('             x1&x2  x2&x3  x1&x3')
# print('pearson:    ', np.round(p12_n, decimals=4), np.round(p13_n, decimals=4),
#       np.round(p23_n, decimals=4))
# print('cos:        ', np.round(c12_n, decimals=4), np.round(c13_n, decimals=4),
#       np.round(c23_n, decimals=4))
# print('euclidean sq', np.round(d12_n, decimals=4), np.round(d13_n, decimals=4),
#       np.round(d23_n, decimals=4))

# x=[-60.70,403.80]
# y=[-21.79, 350.76]
# print('x',x)
# print('y',y)
  
# #方法一：根据公式求解
# x_=x-np.mean(x)
# y_=y-np.mean(y)
# d1=np.dot(x_,y_)/(np.linalg.norm(x_)*np.linalg.norm(y_))
# pearsonr(x_, y_)
# print('d1',d1)
# print('pearsonr',pearsonr(x, y))