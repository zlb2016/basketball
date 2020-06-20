# -*- coding:utf-8 -*-
import numpy as np
import scipy.misc
import cv2
import time
import json
def _preproc_color(image):
    """ Preprocessing the color image"""
    output_shape = np.array([376.0, 656.0], np.float32)

    # reshape by trafo
    ratio = np.min(output_shape / np.array(image.shape[:2], dtype=np.float32))
    M = np.array([[ratio, 0.0, 0.0], [0.0, ratio, 0.0]])
    image_s = cv2.warpAffine(image, M, (output_shape[1], output_shape[0]), flags=cv2.INTER_AREA)

    # subtract mean and rgb -> bgr
    image = image_s[:, :, 0:3].astype('float32')
    image = image[:, :, ::-1]
    image = image / 256.0 - 0.5
    image = np.expand_dims(image, 0)
    return image, image_s, ratio
def _show_openpose_det(image_s, person_det, name,pic_type,pnum,block=True):
        """ Shows the detections of openpose in the color image. """
        import matplotlib.pyplot as plt
        from utils.DrawUtil import draw_person_limbs_2d_coco
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.imshow(image_s)
        fmt_list = ['ro', 'go', 'co', 'mo']
        for anno, fmt in zip(person_det.values(), fmt_list):
            coords = np.zeros((18, 2))
            vis = np.zeros((18, ))
            for i, kp in enumerate(anno['kp']):
                if (kp is not None) and (kp[2] > 0.1):
                    # ax1.plot(kp[0], kp[1], fmt)
                    coords[i, :] = np.array([kp[0], kp[1]])
                    vis[i] = 1.0
            draw_person_limbs_2d_coco(ax1, coords, vis, color='sides', order='uv')
        plt.savefig('./2D_pictures/'+pic_type+'/'+pnum+'/'+name+'.png')
        print('2D姿态图片'+pic_type+'-'+name+'已生成')
        # plt.show(block=block)
        # plt.savefig('RGB.png')
def test(filepath):
    with open(filepath,encoding='utf-8') as f:#读取测试生成2D关键点坐标文件
        line = f.readlines()
        print('len',type(line))
        for index,dic in enumerate(line):
            d = json.loads(dic)
            kp=d['person_det']['person0']
            del kp['kp'][14:18]#删除4个关键点变为14个关键点
            d['person_det']['person0']=kp
            image='../../pictures/rgb/P008/frames_'+d['img_name']+'.png'
            color = scipy.misc.imread(image)  # color image
            color = scipy.misc.imresize(color, (1080, 1920))
            image_proc, image_s, scale_ratio =_preproc_color(color)
            _show_openpose_det(image_s,d['person_det'],d['img_name'],'test',d['person'])
def true_2D_pose(filepath):
    with open(filepath,encoding='utf-8') as f:#读取2D关键点坐标文件
            line = f.readlines()
            print('len',type(line))
            for index,dic in enumerate(line):
                d = json.loads(dic)
                person_2d=d['2D_skeleton']
                name=d['person']+'_'+str(d['frame_index'])#图片名称
                person_det={}
                di={}
                di['kp']=person_2d#关键点坐标
                di['conf']=1#置信度
                person_det['person0']=di
                if(d['frame_index']+1<10):#读取原始图片
                    dp='0'+str(d['frame_index']+1)
                else:
                    dp=str(d['frame_index']+1)
                image='../../pictures/rgb/P008/frames_000'+dp+'.png'
                color = scipy.misc.imread(image)  # color image
                image_s = scipy.misc.imresize(color, (1080, 1920))
                _show_openpose_det(image_s,person_det,name,'true','P'+d['person'])
if __name__ == "__main__":
    # image_proc, image_s, scale_ratio =_preproc_color(color)
    # person_det={'person0': {'kp': [
    #     [376.       ,  32.       ,   0.8929911],#0.鼻子
    #     [360.       ,  88.       ,   0.8367073],#1.脖子
    #     [328.        ,  80.        ,   0.63945055],#2.右肩
    #     [288.      , 120.      ,   0.805474],#3.右肘
    #     [256.        ,  88.        ,   0.72609437],#4.右腕
    #     [392.        ,  88.        ,   0.76638436],#5.左肩
    #     [408.       , 144.       ,   0.8374882],#6.左肘
    #     [456.       , 144.       ,   0.7570134],#7.左腕
    #     [328.        , 200.        ,   0.49084562],#8.右臀
    #     [344.       , 296.       ,   0.5863148],#右膝
    #     [344, 368, 0.19652022],#右踝
    #     [384.        , 200.        ,   0.40056953],#左臀
    #     [408.        , 272.        ,   0.67569005],#左膝
    #     [416, 336, 0.40510252],#左踝
    #     [360.       ,  24.       ,   0.7857645],#右眼
    #     [384.       ,  24.       ,   0.9599892],#左眼
    #     [352.        ,  40.        ,   0.89546907],#右耳
    #     [392.      ,  40.      ,   0.860474]#左耳
    #     ],
    #      'conf': 0.7197682335580649}}
    # filepath='./truth_14_008_2D.json'
    # true_2D_pose(filepath)
    test_path='./2D_keypoints/2D_keypoints_P008_1.json'
    test(test_path)
    # person_det={'person0': {'kp': [[1087.718, 360.6033,1], [1088.494, 437.8093,1], [1148.668, 448.2227,1], [1158.395, 526.946,1], [1126.084, 590.3838,1], [1027.991, 448.807,1], [1022.717, 528.879,1], [1057.385, 593.5451,1], [1115.745, 608.8664,1], [1124.162, 694.371,1], [1122.058, 783.7611,1], [1064.32, 608.9387,1], [1062.998, 690.1909,1], [1073.943, 776.9492,1]], 'conf': 0.7197682335580649}}
    
    # time_start=time.time()#计时开始
    # _show_openpose_det(image_s,person_det)
    # time_end=time.time()
    # print('done')
    # print('time cost',time_end-time_start,'s')
    pass