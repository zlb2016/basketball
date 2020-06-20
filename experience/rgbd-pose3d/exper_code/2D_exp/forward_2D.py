#!/usr/bin/env python
# -*- coding:utf-8 -*-
import scipy.misc
import numpy as np
import matplotlib.pyplot as plt

from PoseNet2D import *
from utils.Camera import *
import os
import json
import time

# VALUES YOU MIGHT WANT TO CHANGE
OPE_DEPTH = 1  # in [1, 5]; Number of stages for the 2D network. Smaller number makes the network faster but less accurate
VPN_TYPE = 'fast'  # in {'fast', 'default'}; which 3D architecture to use
CONF_THRESH = 0.01  # threshold for a keypoint to be considered detected (for visualization)
GPU_ID = 0  # id of gpu device
GPU_MEMORY = None  # in [0.0, 1.0 - eps]; percentage of gpu memory that should be used; None for no limit
# NO CHANGES BEYOND THIS LINE
def dealpic(color_pic):
    """  APPROX. RUNTIMES (measured on a GTX 1080 Ti, frame with 4 people)
    VPN=fast, OPE=1: 0.51sec = 1.96 Hz
    VPN=fast, OPE=5: 0.56sec = 1.79 Hz
    VPN=default, OPE=1: 0.59sec = 1.70 Hz
    VPN=default, OPE=5: 0.64sec = 1.57 Hz

    APPROX. RUNTIMES (measured on a GTX 970, frame with 4 people)
    VPN=fast, OPE=1: 1.20 = 0.84 Hz
    VPN=fast, OPE=5: 1.30 sec = 0.77 Hz
    VPN=default, OPE=1: 1.41sec = 0.71 Hz
    VPN=default, OPE=5: 1.54sec = 0.65 Hz

    NOTE: Runtime scales with the number of people in the scene.
    """
    # create algorithm
    poseNet = PoseNet2D(ope_depth=OPE_DEPTH, vpn_type=VPN_TYPE,
                        gpu_id=GPU_ID, gpu_memory_limit=GPU_MEMORY)

    time_start=time.time()#计时开始
    # run algorithm
    for index,val in enumerate(rgb):
      color = scipy.misc.imread('./pictures/rgb/rgb_png/P045/frames_'+val+'.png')  # color image
      person_det, keypoint_det_fs = poseNet.detect(color)
    time_end=time.time()
    print('时间--',time_end-time_start,'s')
    print('时间--',(time_end-time_start)/len(rgb),'s')
    # dic={}
    # with open('2D_keypoints.json','a') as f:#将检测到的关键点和图片名称写入文件
    #    for i, val in enumerate(rgb_list):#遍历图片列表
    #        dic['img_name']=val
    #        dic['person_det']=person_det
    #        dicJson = json.dumps(dic)
    #        f.write(dicJson+'\n')
    #    f.close()
    # print('person_det',person_det)

def sortss(lists):#对图片列表排序
    j = 0
    while j < len(lists)-1:
        i = 0
        while i < len(lists)-(j+1):
            if lists[i] > lists[i+1]:
                a = lists[i]
                lists[i] = lists[i+1]
                lists[i+1] = a
            i += 1
        j += 1
    return lists

if __name__ == '__main__':
    rgb_list=[]
    for rgb_name in os.listdir(r"./pictures/rgb/rgb_png/P045/"):
        new_file_name = rgb_name.split(".png")[0].split("_")[1]
        rgb_list.append(new_file_name)
    rgb=sortss(rgb_list)
    time_start=time.time()#计时开始
    dealpic(rgb)#计时结束
    time_end=time.time()
    print('time cost',time_end-time_start,'s')
    pass
