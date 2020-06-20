import axios from '@/libs/api.request'

/**
    动作类别列表
    输入：token
    返回：动作类别
*/
export const getActionList = (token) => {
    return axios.request({
      url: 'v1/actions/',
      params: {
        token
      },  
      method: 'get'
    })
  }
  /**
    动作类别信息
    输入：token, 
    返回：
*/
export const getActionView = (token,action_code) => {
    return axios.request({
      url: 'v1/actions/'+action_code,
      params: {
        token,
        action_code     
      }, 
      method: 'get'
    })
  }
/**
    动作新增
    输入：token, 
    返回：
*/
export const getActionadd = (token,info) => {
    return axios.request({
      url: 'v1/actions/add',
      params: {
        token
      },
      data: info,
      method: 'post'
    })
  }