import numpy as np
from collections import namedtuple

from utils.Camera import Camera

VoxelTrafoParamsNew = namedtuple('VoxelTrafoParamsNew', ['voxel_root', 'voxel_scale'])


class VoxelizationUtil(object):
    def __init__(self):
        assert 0, "Abstract class"

    @classmethod
    def voxelize_person(cls, cam, depth_warped, mask,
                 coord2d, coord_vis,
                 root_z_value, grid_size, grid_size_m=None,
                 f=1.0, root_id=1, coord2d_root=None):
        """ Creates a voxelgrid from given input. 从输入中创建体素网格，cam为校准矩阵数据，
        depth_warped为变形深度图，coord2d为2D关节坐标，coord_vis为关节可见性，
        root_z_value为颈部关节点深度，grid_size为体素网格大小，grid_size_m为非对称网格
        coord2d_root为颈部关节点"""
        if grid_size_m is None:
            # cube around the neck, camera coord system
            grid_size_m = np.array([[-1.1, -0.4, -1.1],
                                    [1.1, 1.8, 1.1]])

        if coord2d_root is None:
            coord2d_root = coord2d[root_id, :]

        # randomly sample the cube a bit different in size随机抽取大小稍有不同的立方体样本
        grid_size_m *= f

        grid_size = np.reshape(grid_size, [1, 3]).astype('int32')
        root_xyz = cam.backproject(coord2d_root, root_z_value)  # neck world coordinates颈部世界坐标wr

        # get a voxel located at the root_xyz，获取位于root_xyz的体素
        voxel_grid, trafo_params = cls.voxelize(cam, depth_warped, mask, root_xyz, grid_size, grid_size_m, f)

        # 5. Calculate pseudo 2D coordinates at neck depth in voxel coords，在体素坐标中计算颈部深度处的伪2D坐标
        coord_pseudo2d = cam.backproject(coord2d, root_z_value)  # project all points onto the neck depth，将所有关节点投影到颈部深度，
        coord_pseudo2d_vox = cls.trafo_xyz_coords_to_vox_new(coord_pseudo2d, trafo_params)

        return voxel_grid, coord_pseudo2d_vox[:, :2], trafo_params

    @classmethod
    def voxelize(cls, cam, depth_warped, mask, voxel_root, grid_size, grid_size_m, f=1.0):
        """ Creates a voxelgrid from given input. 从输入中创建体素网格"""
        grid_size = np.reshape(grid_size, [1, 3]).astype('int32')

        # Copy inputs
        depth_warped = np.copy(depth_warped)
        mask = np.copy(mask)
        voxel_root = voxel_root.copy()

        # 1. Vectorize depth and project into world向量化深度并投射到世界中
        uv_vec = cam.get_meshgrid_vector(depth_warped.shape, mask)
        z_vec = np.reshape(depth_warped[mask], [-1]) / 1000.0
        pcl_xyz = cam.backproject(uv_vec, z_vec)
        # print('pcl_xyz', pcl_xyz.shape)

        # 2. Discard unnecessary parts of the pointcloud，丢弃点云不必要的部分
        pcl_xyz_rel = pcl_xyz - voxel_root
        cond_x = np.logical_and(pcl_xyz_rel[:, 0] < grid_size_m[1, 0], pcl_xyz_rel[:, 0] > grid_size_m[0, 0])
        cond_y = np.logical_and(pcl_xyz_rel[:, 1] < grid_size_m[1, 1], pcl_xyz_rel[:, 1] > grid_size_m[0, 1])
        cond_z = np.logical_and(pcl_xyz_rel[:, 2] < grid_size_m[1, 2], pcl_xyz_rel[:, 2] > grid_size_m[0, 2])
        cond = np.logical_and(cond_x, np.logical_and(cond_y, cond_z))
        pcl_xyz_rel = pcl_xyz_rel[cond, :]
        # print('pcl_xyz_rel', pcl_xyz_rel.shape)

        # 3. Scale down to voxel size and quantize缩小到体素大小并量化
        pcl_xyz_01 = (pcl_xyz_rel - grid_size_m[0, :]) / (grid_size_m[1, :] - grid_size_m[0, :])
        pcl_xyz_vox = pcl_xyz_01 * grid_size

        # 4. Set values in the grid，在网格中设置值
        voxel_grid = np.zeros((grid_size[0, :]))
        pcl_xyz_vox = pcl_xyz_vox.astype('int32')
        voxel_grid[pcl_xyz_vox[:, 0],
                   pcl_xyz_vox[:, 1],
                   pcl_xyz_vox[:, 2]] = 1.0

        # 7. Trafo params参数
        voxel_root += grid_size_m[0, :]
        voxel_scale = (grid_size_m[1, :] - grid_size_m[0, :]) / grid_size
        trafo_params = VoxelTrafoParamsNew(voxel_root=voxel_root, voxel_scale=voxel_scale)

        return voxel_grid, trafo_params

    @classmethod
    def trafo_xyz_coords_to_vox_new(cls, coord_xyz, trafo_param):
        """ Transforms xyz coordinates defined by trafo_param into voxelized coordinates.将由trafo_param定义的xyz坐标转换为体素化坐标 """
        assert len(coord_xyz.shape) == 2, "coord_xyz has a bad shape."
        assert coord_xyz.shape[1] == 3, "coord_xyz has a bad last dimension."

        coord_xyz_vox = (coord_xyz - trafo_param.voxel_root) / trafo_param.voxel_scale
        return coord_xyz_vox

    @classmethod
    def trafo_vox_coords_to_xyz_new(cls, coord_xyz_vox, trafo_param):
        """ Transforms from voxelized coords into real xyz.从体素化坐标到真实xyz的转换 """
        assert len(coord_xyz_vox.shape) == 2, "coord_xyz_vox has a bad shape."
        assert coord_xyz_vox.shape[1] == 3, "coord_xyz_vox has a bad last dimension."

        coord_xyz = coord_xyz_vox * trafo_param.voxel_scale + trafo_param.voxel_root
        return coord_xyz

