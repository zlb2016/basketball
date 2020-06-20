import json
import numpy as np
from numpy.lib.format import open_memmap

def jsontojson(filepath):#转化成对应格式的numpy文件
    dic = {}
    infodic = {}
    newdic = {}
    list = []
    newlist = []
    with open(filepath,encoding='utf-8') as f:
      line = f.readlines()
      for item in line:#视频帧数目
        print(line.index(item))
        d = json.loads(item)
        person=d['person']
        for i in range(len(person)):#遍历关节点坐标
          x=person[i][0]
          y=person[i][1]
          z=person[i][2]
          list.append((x, y, z))
        if len(list)!=0:
            print('list', list)
            dic['person_bbox'] = [136, 100, 165, 172, 1]
            dic['frame_index'] = line.index(item)#帧序号
            dic['id'] = 0
            dic['person_id'] = 'null'
            dic['keypoints'] = list
            newlist.append(dic)#"video_name": "skateboarding.mp4", "resolution": [340, 256], "num_frame": 300, "num_keypoints": 17, "keypoint_channels": ["x", "y", "score"], "version": "1.0"
            dic = {}    # 每次清空dic字典
            list = []  # 每次清空list
      infodic['video_name'] = "xxxx.mp4"
      infodic['resolution'] = [340, 256]
      infodic['num_frame'] = 300
      infodic['num_keypoints'] = 18#18个关节点
      infodic['keypoint_channels'] = ["x", "y", "score"]
      infodic['version'] = 1.0
      newdic['info'] = infodic
      newdic['category_id'] = 0
      newdic['annotations'] = newlist
      # dicJson = json.dumps(newdic)
      with open('3d2json.json', 'w') as f:
          json.dump(newdic, f)
      f.close()
def json2npy(jsonfile):#json文件转numpy
    xlist = []#x坐标
    xonelist = [] #一个视频帧的x坐标
    xmorelist = []  # 多个视频帧的x坐标
    ylist = []#y坐标
    yonelist = []#一个视频帧的y坐标
    ymorelist = []#多个视频帧的y坐标
    acclist = []#acc的值
    acconelist = []#一个视频帧的acc的值
    accmorelist = []#多个视频帧的acc的值

    with open(jsonfile, 'r') as f:#加载json文件
        data = json.load(f)
        data_info = data['info']
        data_category = data['category_id']
        data_annotations = data['annotations']
        fp = open_memmap('posejson2npy.npy',
                         dtype='float32',
                         mode='w+',
                         shape=(1, 3, len(data['annotations']), 18,
                                1))
        #print('annotations', len(data['annotations']))
        for i in range(0, len(data['annotations'])):#循环标注len(data['annotations']
            # print('iiiiiii', data['annotations'][i])
            frame_index = data['annotations'][i]['frame_index']
            for j in range(len(data['annotations'][i]['keypoints'])):#17个人体关键点
                print(len((data['annotations'][i]['keypoints'])[0]))
                x = ((data['annotations'][i]['keypoints'])[j])[0]
                y = ((data['annotations'][i]['keypoints'])[j])[1]
                z = ((data['annotations'][i]['keypoints'])[j])[2]
                xlist.append(x)
                ylist.append(y)
                acclist.append(z)
                # break
            xonelist.append(xlist)
            print('---onelist----', xonelist)
            # xmorelist.append(xonelist)
            yonelist.append(ylist)
            # ymorelist.append(yonelist)
            acconelist.append(acclist)
            # accmorelist.append(acconelist)
            print('xmorelist', ymorelist)
            fp[0, 0, i, :, 0] = np.array(xonelist)
            fp[0, 1, i, :, 0] = np.array(yonelist)
            fp[0, 2, i, :, 0] = np.array(acclist)
            xlist = []#将x坐标清空
            xonelist = []#将一个视频帧x坐标清空
            ylist = []  # y坐标
            yonelist = []  # 一个视频帧的y坐标
            acclist = []  # acc的值
            acconelist = []  # 一个视频帧的acc的值

if __name__ == '__main__':
    # jsontojson('record3d.json')
    json2npy('3d2json.json')
    pass
    