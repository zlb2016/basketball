import numpy as np
import matplotlib.pyplot as plt
import scipy
import json
from scipy.stats import pearsonr
from dtw import dtw

#构建关节姿态向量
# /*
# 输入：人体关键点numpy数组
# 输出：人体姿态向量列表xlist
# */
def makevar(data):
    #左上臂向量
    left_up_hand=[data[3,0]-data[2,0],data[3,1]-data[2,1],data[3,2]-data[2,2]]
    #左下臂向量
    left_down_hand=[data[4,0]-data[3,0],data[4,1]-data[3,1],data[4,2]-data[3,2]]
    #右上臂向量
    right_up_hand=[data[6,0]-data[5,0],data[6,1]-data[5,1],data[6,2]-data[5,2]]
    #右下臂向量
    right_down_hand=[data[7,0]-data[6,0],data[7,1]-data[6,1],data[7,2]-data[6,2]]
    #左大腿向量
    left_up_leg=[data[9,0]-data[8,0],data[9,1]-data[8,1],data[9,2]-data[8,2]]
    #左小腿向量
    left_down_leg=[data[10,0]-data[9,0],data[10,1]-data[9,1],data[10,2]-data[9,2]]
    #右大腿向量
    right_up_leg=[data[12,0]-data[11,0],data[12,1]-data[11,1],data[12,2]-data[11,2]]
    #右小腿向量
    right_down_leg=[data[13,0]-data[12,0],data[13,1]-data[12,1],data[13,2]-data[12,2]]
    xlist=[]
    xlist.append(left_up_hand)
    xlist.append(left_down_hand)
    xlist.append(right_up_hand)
    xlist.append(right_down_hand)
    xlist.append(left_up_leg)
    xlist.append(left_down_leg)
    xlist.append(right_up_leg)
    xlist.append(right_down_leg)
    return xlist
#读取人体姿态点的json文件
# /*
# 输入：人体姿态关键点json文件
# 输出：视频帧中的人体姿态关节点向量numpy数组
# */
def inputdata(filepath):
    x=[]
    with open(filepath,encoding='utf-8') as f:#读取人体姿态点的json文件
      line = f.readlines()
      for dic in line:
        d = json.loads(dic)
        print(d)
        person=d['person']
        if len(person)==18:#判断检测出的关键点是否是18个，不是的话舍弃
            rlist=makevar(np.array(person))
            x.append(rlist)
    N=np.array(x)
    print('N',N)
    f.close()
    return N
#计算余弦距离
def cosine(vector1,vector2):
    d=np.dot(vector1,vector2)/(np.linalg.norm(vector1)*(np.linalg.norm(vector2)))
    return d

#计算pearsonr相关系数（每个姿态算,将图片中8个关节向量分别计算系数，相加得到姿态的相似性）
def pearsonred(s1, s2):
    cor=0
    print('s1',s1)
    print('s2',s2)
    for i in range(0,8):
        print('s1[i]',s1[i])
        print('s2[i]',s2[i])
        r_row,p_value=pearsonr(s1[i],s2[i])
        if np.isnan(r_row):
            print(11)
            r_row=0
        else:
            print(r_row)
            cor=cor+r_row#两个姿态的皮尔逊相关系数
    print('m-',i,'-cor',cor)
    # r_row, p_value = pearsonr(x, y)
    return cor

if __name__ == "__main__":
    # posefile='../rgbd-pose3d/output/new_skeleton/ntu_3d_P008.json'#x向量
    # anofile='../rgbd-pose3d/output/new_skeleton/ntu_3d_P041.json'#y向量
    posefile='../rgbd-pose3d/new42.json'
    anofile='../rgbd-pose3d/new008.json'
    x=inputdata(posefile)#获取标准动作的人体姿态关节向量数组(标准动作视频帧数少)
    y=inputdata(anofile)#获取标准动作的人体姿态关节向量数组(标准动作视频帧数少)
    # print('x',x,'--tt--',type(x[0]),'shape--',x.shape)
    # y=x[0:2,:]#取x数组前两行数据#获取测试动作的人体姿态关节向量数组(通常测试动作视频帧数多)
    # print('y',y)
    d, cost_matrix, acc_cost_matrix, path = dtw(x, y, dist=pearsonred)#添加路径计算方式
    print('cost_matrix',cost_matrix)#各个视频帧对应的距离矩阵，可以根据最后的规整路径得到对应的距离值作为相似度计算的结果
    print('d',d)#d为两个序列的最短路径，即最终的相似值
    print('path',path)#path中array[0]表示x的路径，array[1]表示y的规整路径
    plt.imshow(acc_cost_matrix.T, origin='lower', cmap='gray', interpolation='nearest')
    plt.plot(path[0], path[1], 'w')
    plt.show()
   
    pass

