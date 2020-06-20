import json
def read_oks(filepath):
    with open(filepath,encoding='utf-8') as f:#读取oks文件:
        line = f.readlines()
        for index,dic in enumerate(line):
            d = json.loads(dic)
            frame=d['frame_id']
            frame
            if(frame==24):
                oks1=d['oks']
                print('oks-'+str(frame),format(oks1*100,'.1f'))
            elif(frame==25):
                oks2=d['oks']
                print('oks-'+str(frame),format(oks2*100,'.1f'))
            elif(frame==26):
                oks3=d['oks']
                print('oks-'+str(frame),format(oks3*100,'.1f'))
        print('mAP',format((oks1+oks2+oks3)*100/3,'.1f'))

def read_time(filepath):#图片处理时间
    with open(filepath,encoding='utf-8') as f:#读取oks文件:
        line = f.readlines()
        for index,dic in enumerate(line):
            d = json.loads(dic)
            if(index==25):
                time1=d['use_time']
                print('oks-'+str(index-1),format(time1,'.2f'))
            if(index==26):
                time2=d['use_time']
                print('oks-'+str(index),format(time2,'.2f'))
            if(index==27):
                time3=d['use_time']
                print('oks-'+str(index-1),format(time3,'.2f'))
        print('mTime',format((time1+time2+time3)/3,'.2f'))
if __name__ == "__main__":
    filee='./truth_008_5_OKS.json'
    tfile='./2D_keypoints/2D_keypoints_P008_5.json'
    read_oks(filee)
    read_time(tfile)
    pass