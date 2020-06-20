# -*- coding:utf-8 -*-
import numpy as np
import json
def as_num(x):#处理e-04
    print('x',x)
    s=[]
    for i in range(14):
        a=x[0][0]
        s.append([x[i][0],x[i][1],x[i][2]])
    print('s',s)
    return s
def _normal_skeleton(data):
        #  use as center joint,使用臀部中点作为root(test数据)
        print(data.shape)
        right_hip_joint = data[16, :]#右臀
        left_hip_joint = data[12, :]#左臀
        print(type(right_hip_joint[0]+left_hip_joint[0]))
        center_jointx = np.mean((right_hip_joint[0]+left_hip_joint[0])/2)
        center_jointy = np.mean((right_hip_joint[1]+left_hip_joint[1])/2)
        center_jointz = np.mean((right_hip_joint[2]+left_hip_joint[2])/2)

        print(center_jointx)
        print(center_jointy)
        print(center_jointz)
        center = np.array([center_jointx, center_jointy, center_jointz])
        print(data)
        data = data - center
        print('new_data',(data))
        return data
def cal_eucld(coords1,coords2):
    """ Calculates the euclidean distance between 2 lists of coordinates. """
    dd=np.sqrt(np.sum((coords1 - coords2)**2))
    print('123--',np.sqrt(np.sum((coords1 - coords2)**2)))
    return dd

def dealtest(file1,file2):#将test骨架各关节点减去臀部中点后
    newdic = {}
    with open(file1, 'r') as f:
        line = f.readlines()
        print('len--',type(line))
        for index,dic in enumerate(line):
            d = json.loads(dic)
            print(index)
            person=d['skeleton']
            print(len(person))#判断检测出的关键点是否是18个，不是的话舍弃
            if len(person)==18:#从中选择14个坐标画图
                print(len(person))
                d=_normal_skeleton(np.array(person))
                with open(file2, 'a') as fe:
                    newdic['person']='008'
                    newdic['frame_index']=index
                    newdic['skeleton']=as_num(d)
                    #计算欧氏距离每个关节点（test与true对比）
                    # cal_eucld(np.array(newdic['skeleton']),np.array(person))
                    dicJson = json.dumps(newdic)#存储视频帧和骨架
                    fe.write(dicJson+'\n')
        fe.close()
        print('frame_'+str(index)+' is done')
    f.close()

def json_to_numpy(file1,k):#读取json文件写入numpy数组
    with open(file1, 'r') as f:#打开json文件
        line = f.readlines()#读取所有数据行
        newnumpy=np.zeros((len(line),14,3))#初始化numpy数组
        for index,dic in enumerate(line):
            data = json.loads(dic)
            data_skeleton = data['skeleton']
            newskeleton=[]
            print(len(data_skeleton))
            if(k==1):#ntu_真实坐标25个，从中删除多余skeleton坐标，只保留14个
                # print(len(data_skeleton))
                newskeleton.append(data_skeleton[3])
                newskeleton.append(data_skeleton[20])
                newskeleton.append(data_skeleton[8])
                newskeleton.append(data_skeleton[9])
                newskeleton.append(data_skeleton[10])
                newskeleton.append(data_skeleton[4])
                newskeleton.append(data_skeleton[5])
                newskeleton.append(data_skeleton[6])
                newskeleton.append(data_skeleton[16])
                newskeleton.append(data_skeleton[17])
                newskeleton.append(data_skeleton[18])
                newskeleton.append(data_skeleton[12])
                newskeleton.append(data_skeleton[13])
                newskeleton.append(data_skeleton[14])
                data_skeleton=newskeleton
            for j in range(len(data_skeleton)):#循环骨架14个关节点坐标
                print(j)
                newnumpy[index,j,0]=data_skeleton[j][0]
                newnumpy[index,j,1]=data_skeleton[j][1]
                newnumpy[index,j,2]=data_skeleton[j][2]
        print('23131',len(newnumpy))
        print('23131',newnumpy)
    f.close()
    return newnumpy

def test():#测试数据
    a=np.array([[0.000245663733811019, -0.5828365918063347, -0.22687500000000016], [0.018735164651953184, -0.3900084147864441, -0.061875000000000124], [-0.13527720032558604, -0.3900084147864441, -0.061875000000000124], [-0.1866146553180988, -0.2386974694323078, -0.061875000000000124], [0.04184704079963092, -0.3365816668898964, 0.1443749999999997], [0.14544866179675398, -0.33213592193379227, 0.10312499999999991], [0.22637379019067538, -0.0984195919466585, 0.26812499999999995], [0.09136184068725961, -0.29212421732885535, -0.26812499999999995], [-0.08393974533307297, 0.215235366630101, -0.061875000000000124], [-0.13781866821450917, 0.5110587602284855, -0.10312499999999991], [-0.09688016000958202, 0.7769298984201973, -0.22687500000000016], [0.018735164651953184, 0.215235366630101, -0.061875000000000124], [0.03260229034055989, 0.6169748328176485, 0.061875000000000124], [0.037224665570095405, 0.9437726856468873, 0.10312499999999991]])
    c=np.array(
            [[0.06700699545454541, 0.6702894868181818, -0.18759062121212056], [0.03541239545454544, 0.41677468681818186, -0.16763462121212092], [0.20227489545454547, 0.3481538868181818, -0.22090462121212084], [0.22664809545454545, 0.3552073868181818, -0.4534826212121206], [0.11221469545454543, 0.5174000868181818, -0.47787262121212093], [-0.09248410454545458, 0.4266818868181818, -0.19638362121212083], [-0.16615340454545455, 0.4720252868181818, -0.4177576212121208], [0.011102395454545444, 0.5357513868181818, -0.48689262121212096], [0.05778429545454544, -0.07045191318181818, -0.05581162121212069], [0.07088999545454544, -0.3336989131818182, -0.07126362121212093], [0.07685099545454543, -0.5963649131818182, 0.08160037878787918], [-0.09872450454545456, -0.04128941318181817, -0.03824862121212069], [-0.11036780454545456, -0.31674901318181825, 0.021085378787879083], [-0.03946690454545454, -0.5902369131818183, 0.19702437878787915]]
        )
    sum1=0
    for j in range(a.shape[0]):#按骨架循环
        dis=cal_eucld(a[j],c[j])
        sum1+=dis
    print(round(sum1/a.shape[0],3))
                         
if __name__ == "__main__":
    #读取关节点文件
    # file1='../test_data/test_008_3d.json'#test文件处理
    # savefile='./test_normal_008_3d.json'
    # dealtest(file1,savefile)
    #test()#测试欧式距离
    #计算欧拉距离
    true_file='../truth_data/truth_008.json'
    test_normal_file='./test_normal_008_3d.json'
    save_eucld_file='./frame_test_eucld_008.json'
    test_numpy=json_to_numpy(test_normal_file,0)
    trutn_numpy=json_to_numpy(true_file,1)
    #读取json文件写入numpy数组 
    print('11',test_numpy.shape)
    dicee = {}
    with open(save_eucld_file, 'a') as f:#打开存放欧式距离json文件
        for i in range(test_numpy.shape[0]):#按帧循环
            sum1=0
            for j in range(test_numpy.shape[1]):#按骨架循环
                dis=cal_eucld(test_numpy[i,j],trutn_numpy[i,j])
                sum1+=dis
            dicee['person_num']='008'
            dicee['frame_index']=i
            dicee['distance']=round(sum1/test_numpy.shape[1],3)
            dicJson = json.dumps(dicee)#存储视频帧和骨架
            f.write(dicJson+'\n')
            print(round(sum1/test_numpy.shape[1],3))#每个视频帧的欧式距离
    f.close()
    pass