import numpy as np
import json

#处理ntu_rgbd数据集得到的25个关节点骨架json，变成14个关节点骨架
if __name__ == "__main__":
    dicss={}
    with open('./truth_14_008_2D.json','a') as fe:
        with open('../../truth_ntu_008_2d.json',encoding='utf-8') as f:
            line = f.readlines()
            print('len',type(line))
            for index,dic in enumerate(line):
                d = json.loads(dic)
                print(index)
                skeleton=d['2D_skeleton']
                dicss['person']=d['person_num']
                dicss['frame_index']=d['frame_index']
                print(len(skeleton))#判断检测出的关键点是否是25个，不是的话舍弃
                newskeleton=[]
                if len(skeleton)==25:
                    #选择14个关键点做图
                    newskeleton.append(skeleton[3])
                    newskeleton.append(skeleton[20])
                    newskeleton.append(skeleton[8])
                    newskeleton.append(skeleton[9])
                    newskeleton.append(skeleton[10])
                    newskeleton.append(skeleton[4])
                    newskeleton.append(skeleton[5])
                    newskeleton.append(skeleton[6])
                    newskeleton.append(skeleton[16])
                    newskeleton.append(skeleton[17])
                    newskeleton.append(skeleton[18])
                    newskeleton.append(skeleton[12])
                    newskeleton.append(skeleton[13])
                    newskeleton.append(skeleton[14])
                    dicss['2D_skeleton']=newskeleton
                    dicJson = json.dumps(dicss)#存储视频帧和骨架
                    fe.write(dicJson+'\n')
                print('frame_'+str(index)+' is done')
        f.close()
    fe.close()
    pass