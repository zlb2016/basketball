# import struct
# import os
# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt
# if __name__ == '__main__':
#     filepath='./Filedepth_0.bin'
#     binfile = open(filepath, 'rb') #打开二进制文件
#     size = os.path.getsize(filepath) #获得文件大小
#     # print(size)
#     rowDepthPixel = 424
#     columnDepthPixel = 512
#     M = np.zeros((rowDepthPixel,columnDepthPixel))
#     arrayFrame = binfile.read()
#     # print(arrayFrame)
#     for r in range(1,rowDepthPixel):
#         for k in range(1,columnDepthPixel):
#             M[(r,k)] = arrayFrame(r)
#     # plt.savefig(M)
import struct
import os

def ReadFile():
    filepath='./Filedepth_0.bin'
    binfile = open(filepath, 'rb') #打开二进制文件
    size = os.path.getsize(filepath) #获得文件大小
    print(size)
    for i in range(size):
        data = binfile.read(1) #每次输出一个字节
        # print(data)
    binfile.close()
if __name__ == '__main__':
	ReadFile()

