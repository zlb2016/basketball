#!/usr/bin/env python
# -*- coding:utf-8 -*-
import scipy.misc
import numpy as np
import matplotlib.pyplot as plt

from PoseNet3D import *
from utils.Camera import *
import os
import json
import time

# VALUES YOU MIGHT WANT TO CHANGE
OPE_DEPTH = 3  # in [1, 5]; Number of stages for the 2D network. Smaller number makes the network faster but less accurate
VPN_TYPE = 'fast'  # in {'fast', 'default'}; which 3D architecture to use
CONF_THRESH = 0.01  # threshold for a keypoint to be considered detected (for visualization)
GPU_ID = 0  # id of gpu device
GPU_MEMORY = None  # in [0.0, 1.0 - eps]; percentage of gpu memory that should be used; None for no limit
# NO CHANGES BEYOND THIS LINE
def dealpic(color_pic,depth_pic):
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

    # intrinsic calibration data
    ratio = np.array([1920.0/512.0, 1080.0/424.0])
    K = np.array([[3.7132019636619111e+02 * ratio[0], 0.0, 2.5185416982679811e+02 * ratio[0]],
                   [0.0, 3.7095047063504268e+02 * ratio[1], 2.1463524817996452e+02 * ratio[1]],
                   [0.0, 0.0, 1.0]])
    cam = Camera(K)

    # create algorithm
    poseNet = PoseNet3D(ope_depth=OPE_DEPTH, vpn_type=VPN_TYPE,
                        gpu_id=GPU_ID, gpu_memory_limit=GPU_MEMORY, K=K)

    
    # run algorithm
    for index,val in enumerate(color_pic):
      time_start=time.time()#计时开始
      # load data
      color = scipy.misc.imread('./picture/rgb/rgb_png/P008/frames_'+color_pic[index]+'.png')  # color image
      color = scipy.misc.imresize(color, (1080, 1920))
      depth_w = scipy.misc.imread('./picture/depth/S018C002P008R002A063/MDepth-'+depth_pic[index]+'.png').astype('float32')  # depth map warped into the color frame
      # loop
      mask = np.logical_not(depth_w == 0.0)#逻辑非
      coords_pred, det_conf = poseNet.detect(color, depth_w, mask)
      time_end=time.time()
      # visualize##视频帧的数目(需要在存储姿态json文件时将多个帧的姿态存放在同一json文件中)
      json_results = []
      dic = {}
      import matplotlib.pyplot as plt
      fig = plt.figure()
      ax = fig.add_subplot(111)
      ax.imshow(color)
      with open("./ntu_test_P008_3d.json", "a") as f:#3D坐标
        for i in range(coords_pred.shape[0]):
            coord2d = cam.project(coords_pred[i, :, :])
            vis = det_conf[i, :] > CONF_THRESH
            json_results.append(coord2d[vis])
            dic['person_num'] = '008'
            dic['frame_index'] = index
            dic['3D_skeleton'] = coords_pred[i, :, :].tolist()#3D坐标
            dic['time'] = time_end-time_start
            print('json_results', json_results)
            dicJson = json.dumps(dic)
            f.write(dicJson+'\n')
            ax.plot(coord2d[vis, 0], coord2d[vis, 1], 'ro')
        #plt.savefig('./res/res_'+color_pic+'.png')
        pass
    #plt.show()
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
    depth_list=[]
    for rgb_name in os.listdir(r"./picture/rgb/rgb_png/P008"):
        new_file_name = rgb_name.split(".png")[0].split("_")[1]
        rgb_list.append(new_file_name)
    for rdepth_name in os.listdir(r"./picture/depth/S018C002P008R002A063"):
        rdepth=rdepth_name.split(".png")[0].split("-")[1]
        depth_list.append(rdepth)
    rgb=sortss(rgb_list)
    depth=sortss(depth_list)
    print(depth)
    dealpic(rgb,depth)
    
    pass
