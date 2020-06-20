# -*- coding:utf-8 -*-
import numpy as np
import json
import math
oks = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
sigmas = np.array([.26, .25, .79,  .72, .62, .79, .72, .62, 1.07, .87,  .89, 1.07, .87, .89])/10.0
variances = (sigmas * 2)**2
def compute_kpts_oks(dt_kpts, gt_kpts, area):#计算OKS
    """
    this function only works for computing oks with keypoints，
    :param dt_kpts: 模型输出的一组关键点检测结果　dt_kpts.shape=[3,14],dt_kpts[0]表示14个横坐标值，dt_kpts[1]表示14个纵坐标值，dt_kpts[3]表示14个可见性，
    :param gt_kpts:　groundtruth的一组关键点标记结果　gt_kpts.shape=[3,14],gt_kpts[0]表示14个横坐标值，gt_kpts[1]表示14个纵坐标值，gt_kpts[3]表示14个可见性，
    :param area:　groundtruth中当前一组关键点所在人检测框的面积
    :return:　两组关键点的相似度oks
    """
    g = np.array(gt_kpts)
    xg = g[0::3]
    yg = g[1::3]
    vg = g[2::3]
    print('vg',vg)
    assert(np.count_nonzero(vg > 0) > 0)
    d = np.array(dt_kpts)
    xd = d[0::3]
    yd = d[1::3]
    dx = xd - xg
    dy = yd - yg
    print('variances',variances)
    e = (dx**2 + dy**2) /variances/ (area+np.spacing(1)) / 2#加入np.spacing()防止面积为零
    print('e',e)
    e=e[vg > 0]
    return np.sum(np.exp(-e)) / e.shape[0]

def dt_kp(filepath):#检测关键点数组
    with open(filepath,encoding='utf-8') as f:#读取测试生成2D关键点坐标文件
        line = f.readlines()
        frame_np=np.zeros((len(line),3,14))#初始化视频帧数组
        for index,dic in enumerate(line):
            d = json.loads(dic)
            kp=d['person_det']['person0']
            del kp['kp'][14:18]#删除4个关键点变为14个关键点
            #读取14个关键点
            dt_kpts=np.zeros((3,14))#初始化数组
            for i in range(len(kp['kp'])):
                dt_kpts[0,i]=np.array(kp['kp'][i][0])
                dt_kpts[1,i]=np.array(kp['kp'][i][1])
                dt_kpts[2,i]=np.array(kp['kp'][i][2])
            frame_np[index]=dt_kpts
    return frame_np
#真实关键点数组
def gt_kp(filepath):
    with open(filepath,encoding='utf-8') as f:#读取测试真实关键点坐标文件
        line = f.readlines()
        true_np=np.zeros((len(line),3,14))#初始化视频帧数组
        for index,dic in enumerate(line):
            d = json.loads(dic)
            kp=d['2D_skeleton']
            #读取14个关键点
            gt_kpts=np.zeros((3,14))#初始化数组
            for i in range(len(kp)):
                gt_kpts[0,i]=np.array(kp[i][0]/3)
                gt_kpts[1,i]=np.array(kp[i][1]/3)
                gt_kpts[2,i]=np.array(kp[i][2])
            true_np[index]=gt_kpts
    return true_np

if __name__ == "__main__":
    #COCO坐标
    """
    ["nose","left_eye","right_eye",
    "left_ear","right_ear",
    "left_shoulder","right_shoulder","left_elbow","right_elbow",
    "left_wrist","right_wrist","left_hip","right_hip",
    "left_knee","right_knee","left_ankle","right_ankle"]
    """
    # openpose-coco坐标
    """
    鼻子、颈部、
    右肩、右肘、右手腕、左肩、左肘、
    左手腕、右髋、右膝、右踝、
    左髋、左膝、左踝、右眼、左眼、右耳、左耳
    """
    #检测坐标
    filepath='./2D_keypoints/2D_keypoints_P008_5.json'
    frame_dt=dt_kp(filepath)#得到视频帧检测数组
    # dt_kpts=
    #真实坐标
    truefile='./truth_14_008_2D.json'
    true_gt=gt_kp(truefile)#得到真实关键点坐标数组
    # gt_kpts=
    # #人检测框的面积
    print(frame_dt.shape)
    print(true_gt.shape)
    dic={}
    with open('./truth_008_5_OKS.json','a') as fe:#将结果oks写入文件
        for i in range(true_gt.shape[0]):
            dic['frame_id']=i
            dt_kpts=frame_dt[i]
            gt_kpts=true_gt[i]
            print('dt_kpts',dt_kpts)
            print('gt_kpts',gt_kpts)
            # break
            w=abs((dt_kpts[0,3]-dt_kpts[0,6]))
            h=abs((dt_kpts[1,4]-dt_kpts[1,10]))
            area=w*h#计算人体检测框（）
            print('area',area)
            area=30000
            oks=compute_kpts_oks(dt_kpts,gt_kpts,area)
            dic['oks']=oks
            dicJson = json.dumps(dic)#存储视频帧和骨架
            fe.write(dicJson+'\n')
            print('area',area)
            print('i--',+i,'-oks',oks)
    fe.close
    pass