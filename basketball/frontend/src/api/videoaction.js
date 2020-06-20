import axios from '@/libs/api.request'

/*
    用户上传视频
*/
export const getVideoadd = (token,info) => {
    console.log('info',info)
    return axios.request({
      url: 'v1/videos/add',
      params: {
        token
      },
      data: info,
      method: 'post'
    })
  }
  /*
    用户分析视频之切分视频
  */
export const getVideocut = (token,info) => {
  console.log('info',info)
  return axios.request({
    url: 'v1/videos/cut',
    params: {
      token,
      info
    },
    method: 'get'
  })
}
/*
    获取分析视频的结果,获得分析结果图片的路径
  */
 export const getVideoresult = (token,info) => {
  console.log('info',info)
  return axios.request({
    url: 'v1/videos/results',
    params: {
      token,
      info
    },
    method: 'get'
  })
}
/*
    获取视频分析的文本结果
  */
 export const getVideoposeresult = (token,action_id,frame) => {
  return axios.request({
    url: 'v1/videos/poseresult',
    params: {
      token,
      action_id,
      frame
    },
    method: 'get'
  })
}
/*
    新增视频分析的文本结果
  */
 export const getVideoaddresult = (token,info) => {
  return axios.request({
    url: 'v1/videos/addposeresult',
    params: {
      token,
    },
    data:info,
    method: 'post'
  })
}