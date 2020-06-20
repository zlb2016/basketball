# coding=utf-8
import numpy as np
if __name__ == "__main__":
    data = np.load('./NTU/raw_npy120/S018C002P008R002A063.skeleton.npy',allow_pickle=True).item()  
    np.set_printoptions(threshold=np.inf)
    # for i in range(len(data['skel_body0'])):#解析三维坐标
    #     print(i)
    #     print('11--',data['skel_body0'][i])
    # pass