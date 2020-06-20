import matplotlib.pyplot as plt
from  mpl_toolkits.mplot3d import Axes3D
import numpy as np
human36m_connectivity_dict = [[0, 1, 0], [1, 2, 0], [2, 6, 0], [5, 4, 1], [4, 3, 1], [3, 6, 1], [6, 7, 0],
                              [7, 8, 0], [8, 16, 0],[9, 16, 0],
                              [8, 12, 0], [11, 12, 0], [10, 11, 0], [8, 13, 1], [13, 14, 1], [14, 15, 1]]

def draw3Dpose(pose, ax, lcolor="#3498db", rcolor="#e74c3c", add_labels=False):  # blue, orange
    for i in human36m_connectivity_dict:
        x, y, z = [np.array([pose[i[0], j], pose[i[1], j]]) for j in range(3)]
        ax.plot(x, y, z, lw=2, c=lcolor if i[2] else rcolor)

    RADIUS = 1  # space around the subject
    xroot, yroot, zroot = pose[5, 0], pose[5, 1], pose[5, 2]
    ax.set_xlim3d([-RADIUS + xroot, RADIUS + xroot])
    ax.set_zlim3d([0, 2 * RADIUS + zroot])
    ax.set_ylim3d([-RADIUS + yroot, RADIUS + yroot])

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

if __name__ == "__main__":
    # data=np.array([
    #                 [223.207,202.611,1077]#0.臀部中点-6
    #                 [224.747,114.517,1112]#1.臀部上部中点-7
    #                 [226.18,37.1176,1228]#2.脖子-8
    #                 [227.589,1.96397,1154]#3.头-9
    #                 [183.646,70.2274,1217]#4.左肩-13
    #                 [167.957,142.195,1266]#5.左肘-14
    #                 [159.034,198.601,1183]#6.左腕-15
    #                 [156.279,218.936,1155]#7.左手
    #                 [271.728,67.3031,1188]#8.右肩-12
    #                 [288.588,129.108,1163]#9.右肘-11
    #                 [279.357,189.911,1006]#10.右腕-10
    #                 [272.922,211.511,959]#11.右手
    #                 [200.722,201.658,1110]#12.左臀-3
    #                 [199.913,282.803,1116]#13.左膝-4
    #                 [9999,9999,9999]#14.左踝-5
    #                 [9999,9999,9999]#15.左脚
    #                 [245.916,203.577,1044]#16.右臀-2
    #                 [269.09,300.92,903]#17.右膝-1
    #                 [9999,9999,9999]#18.右踝-0
    #                 [9999,9999,9999]#19.右脚
    #                 [225.801,55.4233,1191]#20.肩部中点
    #                 [156.669,241.685,1129]#21.左手指尖
    #                 [159.041,232.202,1174]#22.左拇指
    #                 [270.098,236.888,971]#23.右手指尖
    #                 [259.334,205.22,993]#24.右拇指
    #             ])
    # data=np.array([
    #     [269.09,300.92,920],#18.右踝-0
    #     [269.09,300.92,903],#17.右膝-1
    #     [245.916,203.577,1044],#16.右臀-2
    #     [200.722,201.658,1110],#12.左臀-3
    #     [199.913,282.803,1116],#13.左膝-4
    #     [199.913,282.803,900],#14.左踝-5
    #     [223.207,202.611,1077],#0.臀部中点-6
    #     [224.747,114.517,1112],#1.臀部上部中点-7
    #     [226.18,37.1176,1228],#2.脖子-8
    #     [227.589,1.96397,1154],#3.头-9
    #     [279.357,189.911,1006],#10.右腕-10
    #     [288.588,129.108,1163],#9.右肘-11
    #     [200.722,201.658,1110],#12.左臀-3
    #     [199.913,282.803,1116],#13.左膝-4
    #     [167.957,142.195,1266],#5.左肘-14
    #     [159.034,198.601,1183]#6.左腕-15
    # ])
    data = np.array([[-60.70762, 403.8008, 109.0549],#0右脚腕
                    [-21.792213, 350.7608, 542.72705],#1右膝
                    [19.21995, 377.59323, 992.2105],#2右臀
                    [306.85883, 326.98297, 967.81555],#3左臀
                    [280.36816, 338.44727, 516.5916],#4左膝
                    [255.34781, 397.92474, 82.73034],#root节点5左脚腕
                    [163.04, 332.288, 980.013],#6臀部中点(骨盆)
                    [178.85904, 234.66092, 1240.1534],#7腰部(脊柱)
                    [164.37048, 211.85312, 1487.3542],#8颈部(胸部)
                    [164.81487, 211.43636, 1683.0452],#9头部
                    [-104.66232, 412.21793, 511.5632],#10右手腕
                    [4.860744, 460.55948, 1061.1226],#11右手肘
                    [34.860744, 360.55948, 1461.1226],#12右肩
                    [353.3462, 285.74405, 1454.4487],#13左肩
                    [440.2841, 285.90445, 1022.6831],#14左手肘
                    [408.4938, 280.56336, 562.1969],#15左手腕
                    [164.2095, 206.31268, 1568.9426]])#16鼻子
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    draw3Dpose(data, ax)
    plt.show()
    pass